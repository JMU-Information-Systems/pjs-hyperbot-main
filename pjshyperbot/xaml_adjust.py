
# EXTRACT uilog from Logger DB
# coding=utf-8
from asyncore import read
from pathlib import Path
from datetime import datetime
import sys
import sqlite3
import shutil
import os
from pathlib import Path
from tarfile import ENCODING
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gew?nschte Datenbank zu implementieren und SQL Befehle auszuf?hren
import json


from xml.etree import cElementTree as ET





class xaml():
    jfile="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json"
    with open(jfile, "r") as json_datei:
        json_liste= json.load(json_datei)
        userid=(str(json_liste['AnonymousUserId']))
        filename=str(json_liste['InstallationTimeUtc']).replace('-','').replace(':','').replace('T','_')[:15]    


    filenametxt = filename + ".txt"
    filename = filename + ".xaml"
    pathxaml = Path(filename)


    #XAML Datei koennen wir nicht einlesen, deshalb als txt speichern
    if (pathxaml.is_file()):
        os.rename(filename, filenametxt)

        #myxaml = open(filenametxt,"w", encoding="utf-8")

    with open(filenametxt) as text_file:
        mytext = text_file.read()

    #print("TXT")
    print(repr(mytext))

    def replaceVariables(self, inputArray):
        #print(repr(xaml.text))
        myfile = xaml.mytext
        for i in inputArray:
            #i = i.tolist
            myfile = myfile.replace(i[0],i[1])
            print("1. Wert")
            #print(str(i))
            print(str(i[0]))

            print("1. Wert")
            print(str(i[1]))
        pathtxt = Path(xaml.filenametxt)

        #txt wieder in XAML umbenennen 
        if (pathtxt.is_file()):
            myxaml = open(xaml.filenametxt,"w", encoding="utf-8")
            myxaml.write(myfile)
            myxaml.close()
            os.rename(xaml.filenametxt, xaml.filename)
        



    


    

    #xaml_file = File.OpenRead(Path.GetFullPath(filename))
    #Content = XamlReader.Load(xaml_file)

    #print(str(xaml))

    #filenametxt = filename + ".txt"

    #xaml = open(filename,"w", encoding="utf-8")

    #txt = open(filenametxt,"w", encoding="utf-8")
    #txt.write()


