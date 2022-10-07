"""
Definition of views.
"""

from datetime import datetime
from tabnanny import filename_only
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import sqlite3
from datetime import datetime
import sys
import sqlite3
import shutil
import os
from Hauptprogramm import hauptprogramm
from HTML_Extraktion import HTMLExtraction
from pathlib import Path
from tarfile import ENCODING
import json
import psycopg2
from rpa_prepare import databaseContact
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy as np
from django.core.files.storage import FileSystemStorage
#import Hauptprogramm 
#def getUType():
 #   db = databaseContact()
  #  type = db.getType()
   # return(type)


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

def about(request):
   
    
    #extractor = HTMLExtraction()
    #combined,variableName, value = extractor.getVariables()
    #db.insertInputWeclapp(variableName)

    #DataFrontend[0][3] = "test"

    #print(type(DataFrontend))
    
         #urlparse(str(col)
   
    #data = db.getDataFrontend()
    #db.getData(dfile)
    #db.createTable(conp, curs, cons)
    #relevantData = db.getRelevantDataFrontend(curs)
    #print(relevantData)

   
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

    
        #read json File f?r Extraktion der userid und intallationtime (f?r filename)
    jfile="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json"

    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()

        #Wenn eine Datei mit gleichem Namen schon vorhanden ist, dann wird sie geloescht 
        if fs.exists(uploaded_file.name):
            fs.delete(uploaded_file.name)
        fs.save(uploaded_file.name, uploaded_file)


    filename = uploaded_file.name

    db = databaseContact()
    task = request.POST.get("useCase")
    extractor = HTMLExtraction()
    combined,variableName, value = extractor.getVariables(task)

    db.insertInputWeclapp(variableName, filename)

    variables = db.getVariables(filename)

    DataFrontend, a = db.getDataFrontend(filename)
    #print("Type" + str(type))
    assert isinstance(request, HttpRequest)
    DataFrontend = np.array(DataFrontend)
    i = 0
    for row in DataFrontend:

        DataFrontend[i][3] = str(urlparse(str(row[3])).hostname)
        i=i+1
   
    #db = databaseContact()
    
    


    #for key, value in input:
        
        #print('Key: %s' % (key) ) 
    
        #print('Value %s' % (value) )

    #content = request.POST.get("vname")
    #print(content)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/input.html',
        {
            'title':'Hyperbot',
            'message': DataFrontend, #'Guten Tag!',
            'a':a,
            'year':datetime.now().year,
            'variables': variables,
            'filename': filename,
        }
    )

def nextSteps(request):
    db = databaseContact()
    myinput = request.POST.items()
    filename = request.POST.get("filename")
    #print("Typ" + str(type(input)))
    db.insertInput(myinput, filename)

    fpath=os.path.dirname(__file__)
    filename = request.POST.get("filename")

    dbname = Path(fpath + '\\' + filename)
    myhauptprogramm = hauptprogramm()
    myhauptprogramm.main(filename)


    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/nextSteps.html',
        {
            'title':'Hyperbot',
            'year':datetime.now().year,
        }
    )
