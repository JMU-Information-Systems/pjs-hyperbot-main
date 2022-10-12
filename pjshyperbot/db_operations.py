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


class databaseContact():  
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
        #Pfad aus Frontend ?bergeben 
        sqltype='''SELECT DISTINCT e_id, u_type, u_name, a_url, a_applicationname, a_windowtitle FROM logger WHERE u_type="Bearbeiten" OR u_type="Suchfeld" OR u_type="Telefonnummer"''' # + str("pjshyperbot." + databaseContact.filename + '.sqlite3')
        
        #curs f?r "neue" DB aus Frontend anlegen
        
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

        for key, value in input:
            

            key = key.replace("[","")
            key = key.replace("'", "")
            if key.isnumeric():


                sqlupdate = '''UPDATE logger SET input_variables = "''' + value + '''" WHERE e_id = ''' + key 
                curs.execute(sqlupdate)
                cons.commit()
        curs.close()


    def pathRequired(self, filename):
        fpath=os.path.dirname(__file__)
        dfile=Path(fpath + '\\' + filename)

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit

        sqlPath = '''SELECT * FROM logger WHERE a_applicationname="excel" OR a_applicationname="msword"'''
        data = curs.execute(sqlPath).fetchall()
        curs.close()


        return(len(data))


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