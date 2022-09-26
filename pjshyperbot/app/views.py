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
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy as np
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
    DataFrontend, a = db.getDataFrontend()
    #print("Type" + str(type))
    assert isinstance(request, HttpRequest)
    DataFrontend = np.array(DataFrontend)
    i = 0
    for row in DataFrontend:

        DataFrontend[i][3] = str(urlparse(str(row[3])).hostname)
        i=i+1
    

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
            'message': DataFrontend, #'Guten Tag!',
            'a':a,
            'year':datetime.now().year,
        }
    )

def input(request):

    db = databaseContact()
    
    input = request.POST.items()
    print("Typ" + str(type(input)))
    db.insertInput(input)


    for key, value in input:
        
        print('Key: %s' % (key) ) 
    
        print('Value %s' % (value) )

    #content = request.POST.get("vname")
    #print(content)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/input.html',
        {
            'title':'Hyperbot',
        
            'year':datetime.now().year,
        }
    )
    
 
