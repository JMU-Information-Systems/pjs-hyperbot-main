# EXTRACT uilog from Logger DB
# coding=utf-8
from datetime import datetime
import sys
import sqlite3
import shutil
import os
from pathlib import Path
from tarfile import ENCODING
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gew?nschte Datenbank zu implementieren und SQL Befehle auszuf?hren
import json
import numpy as np



"""def main():
    #Lesen der Information zu einer Aufzeichnung (userid) aus postgres in einen cursor
    database()"""


class databaseContact():
    print("Test")
    sqlread='''WITH al AS (
           SELECT DISTINCT applog.id, applog.userid, applog.applicationname, applog.windowtitle, applog.url, applog.analysisid
           FROM processanalyzer.applog WHERE applog.applicationname IS NOT NULL AND applog.applicationname::text <> ''::text
           )
           SELECT DISTINCT uilog.clickpositionx, uilog.clickpositiony, uilog.userid AS uilog_userid,
                  uilog.appid AS uilog_appid, uilog.automationid, uilog.name, uilog.type, uilog.eventtype,
                  uilog.positionx, uilog.positiony, uilog.width, uilog.height, uilog."timestamp" AS eventtime,
                  uilog.analysisid, uilog.relativeclickx, uilog.relativeclicky, 0, uilog.unifiedlabel,
                  uilog.value, uilog.elementclass, al.userid AS applog_userid, al.applicationname, al.windowtitle, al.url
           FROM processanalyzer.uilog
           LEFT JOIN al ON uilog.userid::text = al.userid::text AND uilog.appid = al.id AND uilog.analysisid = al.analysisid
           WHERE uilog.userid='%s' 
           ORDER BY uilog."timestamp"; '''
    sqlinsert='''INSERT INTO logger (clickpositionx, clickpositiony, u_userid, u_appid, automationid, u_name, u_type, u_eventtype,
    positionx, positiony, u_width, u_height, eventtime, analysisid, relativeclickx, relativeclicky, u_time, unifiedlabel, u_value, elementclass, 
    a_userid, a_applicationname, a_windowtitle, a_url) VALUES
    (''' 

    #read json File f?r Extraktion der userid und intallationtime (f?r filename)
    jfile="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json"

    #Auslesen der UserID und Installationtime
    with open(jfile, "r") as json_datei:
        json_liste= json.load(json_datei)
        userid=(str(json_liste['AnonymousUserId']))
        filename=str(json_liste['InstallationTimeUtc']).replace('-','').replace(':','').replace('T','_')[:15]    
    sqlread = sqlread.replace('%s',userid)
    fpath=os.path.dirname(__file__)
    sfile=Path(fpath + '\\' + 'rpatemplate.sqlite3') #templatedb in sqlite (Quelle)
    dfile=Path(fpath + '\\' + filename + '.sqlite3') #Aufzeichnungsdb in sqlite (Ziel)
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
        cons=sqlite3.connect(dfile,check_same_thread=False)
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
        row = cursor.fetchone()

    cursor.close
    

    #def getType(self):
     #   sqltype='''SELECT DISTINCT u_type FROM logger''' # + str("pjshyperbot." + databaseContact.filename + '.sqlite3')
      #  u_type = databaseContact.curs.execute(sqltype).fetchall()
       # return(u_type)


    #Daten, die im Frontend angezeigt werden, werden in dieser Methode aus der Datenbank extrahiert
    def getDataFrontend(self, filename):
        fpath=os.path.dirname(__file__)
        dfile=Path(fpath + '\\' + filename) #Aufzeichnungsdb in sqlite (Ziel)

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit
        #Pfad aus Frontend übergeben 
        sqltype='''SELECT DISTINCT e_id, u_type, u_name, a_url, a_applicationname, a_windowtitle FROM logger WHERE u_type="Bearbeiten" OR u_type="Suchfeld" OR u_type="Telefonnummer"''' # + str("pjshyperbot." + databaseContact.filename + '.sqlite3')
        
        #curs für "neue" DB aus Frontend anlegen
        
        data = curs.execute(sqltype).fetchall()
        
        #Hier wird geschaut, ob ein Pfad abgefragt werden muss (wenn mit Excel oder Word gearbeitet wurde)
        sqlneedpath = '''SELECT a_applicationname FROM logger WHERE a_applicationname="excel" OR a_applicationname="ms.word"'''
        needpath = len(curs.execute(sqlneedpath).fetchall())
        if needpath > 0:
            a = 1
        else:
            a = 0

        curs.close()
        return(data, a)

    #In dieser Methode werden die Eingaben zu den Namen der Variaben aus dem Frontend in der Datenbank gespeichert. 
    #Dafuer wird eine neue Spalte input_variables angelegt 
    def insertInput(self, input, filename):
        fpath=os.path.dirname(__file__)
        
        dfile=Path(fpath + '\\' + filename) 

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit
        sqlalter = '''ALTER TABLE logger ADD input_variables TEXT'''
        curs.execute(sqlalter)

        for key, value in input:
            

            key = key.replace("[","")
            key = key.replace("'", "")
            if key.isnumeric():


                sqlupdate = '''UPDATE logger SET input_variables = "''' + value + '''" WHERE e_id = ''' + key 
                curs.execute(sqlupdate)
                cons.commit()
        curs.close()


    #In dieser Methode werden die mit Hilfe der HTML_Extraktion Klasse aus Weclapp extrahierten Werte in der Tabelle variables abgespeichert
    def insertInputWeclapp(self, variableName, filename):
        fpath=os.path.dirname(__file__)
        dfile=Path(fpath + '\\' + filename)

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit

        #Zu Beginn muss die Tabelle leer sein 
        curs.execute("DELETE FROM variables")
        #sqlupdate = '''INSERT INTO variables (v_id, vname, vtype, vinit) VALUES ('''



        i = len(variableName)
        n = 1
        v_id = []
        vtype = []
        vinit = []
        while n <= i:
            sqlupdate = '''INSERT INTO variables (v_id, vname, vtype, vinit) VALUES (''' + str(n) + ", " +'\''+ variableName[n-1]+'\''+ ", "+'\'' + 'String'+'\'' + ", "+'\'' + ''+'\'' + ')'
            #print(str(sqlupdate))
            curs.execute(sqlupdate)
            cons.commit()
            v_id.append(n)
            vtype.append("String")
            vinit.append("")
            n = n+1
        curs.close()
        combined = np.column_stack((v_id, variableName, vtype, vinit))

        print(str(combined))

    #Abfrage der verschiedenen Variablen aus der Datenbank. 
    def getVariables(self, filename):
        fpath=os.path.dirname(__file__)
        dfile=Path(fpath + '\\' + filename) #Aufzeichnungsdb in sqlite (Ziel)

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit
        sqlselect = '''SELECT DISTINCT vname FROM variables'''
        data = curs.execute(sqlselect).fetchall()
        values = []
        i = 0
        for a in data:
            a = str(a).replace("(","").replace(")","").replace("'","").replace(",","")
            values.append(a)
            i = i+1

        curs.close()
        return(values)



"""
if __name__ == '__main__':
    main()"""