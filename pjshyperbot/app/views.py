"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
import os
import Hauptprogramm
from HTML_Extraktion import HTMLExtraction
from pathlib import Path
from db_operations import databaseContact
from urllib.parse import urlparse
import numpy as np
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def register(request):
    """Renders the register page."""
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "app/register.html", context)



def home(request):
    """Renders the home page."""
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Members of the Team.',
            'year':datetime.now().year,
        }
    )

#This page can only be reached if you are logged in.
@login_required
def about(request):
    """Renders the about page."""

    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/about.html',
        {
            'title':'Hyperbot',
            'year':datetime.now().year,
        }
    )

def input(request):
    #As soon as the values from the frontend are transferred from the Hyperbot page via POST, you can access the inputs via views.py.
    if request.method == 'POST':
        #Access the uploaded file 
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()

        #If a file with the same name already exists, it will be deleted. 
        if fs.exists(uploaded_file.name):
            fs.delete(uploaded_file.name)

        #Saving the uploaded database in the same folder as the programme
        fs.save(uploaded_file.name, uploaded_file)


    filename = uploaded_file.name

    db = databaseContact()
    task = request.POST.get("useCase")
    extractor = HTMLExtraction()

    #Extract the variables from the task template in Weclapp
    combined,variableName, value = extractor.getVariables(task)

    #write the extracted variables from Weclapp into the database to display them in the dropdown.on the next page
    db.insertInputWeclapp(variableName, filename)

    #Querying the variables in the database in order to be able to display them in the frontend in the drop-down menu.
    variables = db.getVariables(filename)

    #Extraction of the recording data from the database, to which the variables must be assigned in the frontend.
    DataFrontend = db.getDataFrontend(filename)

    #Read out the number of variables to know how many values to display in the drop-down menu.
    len = db.pathRequired(filename)

    assert isinstance(request, HttpRequest)
    DataFrontend = np.array(DataFrontend)
    i = 0

    #The URL is cut for display in the frontend.
    for row in DataFrontend:

        DataFrontend[i][2] = str(urlparse(str(row[2])).hostname)
        i=i+1
   

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/input.html',
        {
            'title':'Hyperbot',
            'message': DataFrontend, 
            'len':len,
            'year':datetime.now().year,
            'variables': variables,
            'filename': filename,
            'task': task,
        }
    )

def nextSteps(request):
    """Renders the nextSteps page."""

    db = databaseContact()

    #As soon as the input from the input page has been sent to the frontend, it can be accessed in views.py.
    myinput = request.POST.items()
    filename = request.POST.get("filename")
    task = request.POST.get("task")

    dataScraping = request.POST.get("switch")

    path = request.POST.get("path")

    db.insertInput(myinput, filename)

    filename = request.POST.get("filename")

    #Generate the XAML
    Hauptprogramm.main(filename, task, dataScraping, path)


    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/nextSteps.html',
        {
            'title':'Hyperbot',
            'year':datetime.now().year,
        }
    )
