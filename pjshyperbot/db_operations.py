# coding=utf-8
from datetime import datetime
import sqlite3
import os
from pathlib import Path
import numpy as np


class databaseContact():  

    #Data that is displayed in the frontend is extracted from the database in this method
    def getDataFrontend(self, filename):

        #Get the path of the database with the required information.
        fpath=os.path.dirname(__file__)
        dfile=Path(fpath + '\\' + filename) 

        try:
            #connect to sqlite3
            cons=sqlite3.connect(dfile,check_same_thread=False)
            curs=cons.cursor()
        except sqlite3.Error as e:
            print(e)
            exit


        #Query the data displayed in the frontend from the database. More detailed information is needed about the recorder records of the fields of type "Bearbeiten", "Suchfeld" and "Telefonnummer", as information is entered via the keyboard that is not recorded for data protection reasons. 
        sqltype='''SELECT DISTINCT e_id, u_name,  a_url, a_applicationname, automationid, a_windowtitle FROM logger WHERE u_type="Bearbeiten" OR u_type="Suchfeld" OR u_type="Telefonnummer"''' 
        
        
        data = curs.execute(sqltype).fetchall()
        

        curs.close()
        return(data)

    #In this method, the entries for the names of the variables from the frontend are saved in the database. 
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


    #This method checks whether it is necessary to specify the path in the frontend. This is necessary when working with Excel or Word.
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


    #In this method, the values extracted from Weclapp with the help of the HTML_Extraction class are stored in the variables table.
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

        #At the beginning the table must be empty 
        curs.execute("DELETE FROM variables")




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
        #Removing brackets, commas and quotes
        for a in data:
            a = str(a).replace("(","").replace(")","").replace("'","").replace(",","")
            values.append(a)
            i = i+1

        curs.close()
        return(values)



"""
if __name__ == '__main__':
    main()"""