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
##from rpa_backend import *
from rpa_prepare import databaseContact

def getUType():
    db = databaseContact()
    type = db.getType()
    return(type)


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
    assert isinstance(request, HttpRequest)
    #type = db.getType()
    #Lesen der Information zu einer Aufzeichnung (userid) aus postgres in einen cursor
    """sqlread='''WITH al AS (
           SELECT DISTINCT applog.id, applog.userid, applog.applicationname, applog.windowtitle, applog.url, applog.analysisid
           FROM processanalyzer.applog WHERE applog.applicationname IS NOT NULL AND applog.applicationname::text <> ''::text
           )
           SELECT DISTINCT uilog.clickpositionx, uilog.clickpositiony, uilog.userid AS uilog_userid,
                  uilog.appid AS uilog_appid, uilog.automationid, uilog.name, uilog.type, uilog.eventtype,
                  uilog.positionx, uilog.positiony, uilog.width, uilog.height, uilog."timestamp" AS eventtime,
                  uilog.analysisid, uilog.relativeclickx, uilog.relativeclicky, uilog."time", uilog.unifiedlabel,
                  uilog.value, uilog.elementclass, al.userid AS applog_userid, al.applicationname, al.windowtitle, al.url
           FROM processanalyzer.uilog
           LEFT JOIN al ON uilog.userid::text = al.userid::text AND uilog.appid = al.id AND uilog.analysisid = al.analysisid
           WHERE uilog.userid='%s' 
           ORDER BY uilog."timestamp"; '''
    sqlinsert='''INSERT INTO logger (clickpositionx, clickpositiony, u_userid, u_appid, automationid, u_name, u_type, u_eventtype,
    positionx, positiony, u_width, u_height, eventtime, analysisid, relativeclickx, relativeclicky, u_time, unifiedlabel, u_value, elementclass, 
    a_userid, a_applicationname, a_windowtitle, a_url) VALUES
    ('''
    sqldelete='DELETE FROM logger AS log1 WHERE log1.u_time = 0 AND EXISTS (SELECT * FROM logger AS log2 WHERE log2.e_id = log1.e_id +1 AND log2.u_time > 0)'

    #read json File f?r Extraktion der userid und intallationtime (f?r filename)
    jfile="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json"

    #Auslesen der UserID und Installationtime
    with open(jfile, "r") as json_datei:
        json_liste= json.load(json_datei)
        userid=(str(json_liste['AnonymousUserId']))
        filename=str(json_liste['InstallationTimeUtc']).replace('-','').replace(':','').replace('T','_')[:15]    
    sqlread = sqlread.replace('%s',userid)
    fpath=os.path.dirname(__file__)
    sfile=Path(fpath.strip('app') + 'rpatemplate.sqlite3') #templatedb in sqlite (Quelle)
    dfile=Path(fpath + '\\' + filename + '.sqlite3') #Aufzeichnungsdb in sqlite (Ziel)
    print(dfile)
    shutil.copy(sfile,dfile)

    try:
        #Connect to postgres
        conp=psycopg2.connect(
            host="132.187.102.173", #Host-IP
            database="processanalyzer", #Name der DB
            user="postgres", #user
            password="postgres") #password
        cursor=conp.cursor()
    except psycopg2.Error as error:  #Fehlerhandling
        print("DB-Error ", error)
        exit


        ###########################
    try:
        #connect to sqlite3
        cons=sqlite3.connect(dfile)
        curs=cons.cursor()
    except sqlite3.Error as e:
        print(e)
        exit
        #############################

    #F?llen des cursors aus postgres f?r die Aufzeichnung
    cursor.execute(sqlread) 

    #Einf?gen der Zeilen aus dem cursor in die sqlitedb(Aufzeichnung)
    row = cursor.fetchone() 
    while row:
        sqlcmd=sqlinsert
        for i in range(24):
            if i > 0:
                sqlcmd=sqlcmd+','
            if str(row[i]).isnumeric():
                sqlcmd=sqlcmd+str(row[i])
            else:
                sqlcmd=sqlcmd+'\''+str(row[i])+'\'' 
        sqlcmd=sqlcmd+')'
        try:
            curs.execute(sqlcmd)
            cons.commit()
            curs.close
        except sqlite3.Error as e:
            print(e)
            exit
        row = cursor.fetchone()"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Hyperbot',
            'message':'Guten Tag!',
            'year':datetime.now().year,
        }
    )
def Dateneingabe(request):
    context = {}
    content = request.POST.get("vname")
    print(content)
    if request.POST.get("vfurther")=="ja":
        return render(request,'app/about.html', {
            'title':'Hyperbot',
            'message':'Guten Tag!',
            'year':datetime.now().year,
        })
    else:
        HTML_String = f"""
        <h1>Danke fuer deine Eingabe<h1>
        """
        return HttpResponse(HTML_String,'app/about.html')
    
   #if request.method=="POST":
    #     return render(request,'about/Dateneingabe.html', {'name': request.POST['v']})
  # else:
   #    return HttpResponse("HELLO WORLD IS TRUE")
