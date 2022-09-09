"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import sqlite3
from datetime import datetime
import sys
import sqlite3
import shutil
import os
from pathlib import Path
from tarfile import ENCODING
import json
import psycopg2
from rpa_prepare import databaseContact

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
    db = databaseContact()
    DataFrontend = db.getDataFrontend()
    #print("Type" + str(type))
    assert isinstance(request, HttpRequest)
   
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
            'message': str(DataFrontend), #'Guten Tag!',
            'year':datetime.now().year,
        }
    )
def Dateneingabe(request):
  
    #content = request.POST.get("vname")
    #print(content)
    if request.POST.get("vfurther")=="ja":
        return render(request,'app/about.html', {
            'title':'Hyperbot',
            'message':'Guten Tag!',
            'year':datetime.now().year,
        })
    else:
        return HttpResponse("<html><body>Danke fuer deine Eingabe</body></html>")
    
 
