# Generate UIPath XAML from Logger DB
import sys
import sqlite3
from tkinter.tix import COLUMN
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gewünschte Datenbank zu implementieren und SQL Befehle auszuführen
import pandas
import urllib
import xaml as xaml
import lib_bausteine
import lib2_bausteine #Bausteine werden aus seperatem Skript importiert, bessere Übersichtlichkeit,
import json

#read json File, wichtig um UserID zu bekommen
path="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json" #liegt es auch auf der VM hier?

#Auslesen der UserID nach der gefiltert werden muss
#with open(path, "r") as json_datei:
 #   json_liste= json.load(json_datei)
  #  userid=(str(json_liste['AnonymousUserId']))
   # print(userid)


#leonie def main(dbname):    # argument is the name of the database as produced by the recorder plus additional table for input/output links
def main():
    """" Leonie
    filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml

    #filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml
    #xaml = open(filename,"w", encoding="utf-8")
    """
    #Declaration Section
    v_zaehler=0
    v_a_applicationname="x" #Initialer Wert, nicht verändern, wird unten abgefragt

    xaml = open("C:\\Users\\trist\\PycharmProjects\\output\\meine.xaml", "w", encoding="utf-8") #anpassen auf VM
    lib_bausteine.writehead(xaml) #Schreibe Header
    lib_bausteine.a_comment(xaml,"2", "Für den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, ggf. sind Modifikationen notwendig")

    try:
       # #Connect to postgres
        #con=psycopg2.connect(
         #   host="132.187.102.173", #Host-IP
          #  database="processanalyzer", #Name der DB
           # user="postgres", #user
            #password="postgres") #password
        #cursor=con.cursor()

        #Ausführung des SQl Statements, userid wird aus json ausgelesen, automtationid und a_applicationname darf nicht leer sein, Order by timestamp
        #cursor.execute("Select * from public.th_alles where uilog_userid=%s and automationid != '' and automationid is not Null and a_applicationname !='' and a_applicationname is not null order by timestamp;",[userid]) #sql statement

    #Sodass nicht auf einzelne Spaltennummern zugegriffen werden muss, sondern der Zugriff über den Spaltennamen erfolgt
        def matching(cursor):
            results = {}
            column = 0
            for x in cursor.description:
                results[x[0]] = column
                column = column + 1
            return results

        column = matching(cursor)
        for row in cursor:
            
         #Anpassen der URL, trimmen  einfügen von * sodass Selektor für alle Seiten dieser URL gilt
            
         from urllib.parse import urlparse
            a= urlparse(str(row[column[a_url]]))
            website_name = a.hostname
            url = "*https://" + website_name + "*"

            #Abfrage auf Applikationen

            #Browser: Wenn der a_applicationname "Edge"  ist, handelt es sich um Browseraktivitäten, deshalb hier andere Bausteine verwenden

            if (row[column['a_applicationname']]) == "msedge":

                #Abfrage auf Aktivitäten über Spalte Type:
                if (row[column['u_type']]) == "Schaltfläche": #dann ist es eine Klickakitivität

                    if str.__contains__(str(row[column['u_name']]), (("Minimieren") or ("Maximieren"))): #Ausschluß, dies wird nicht automatisiert
                        pass

                    #Art des Klicks:Linksklick?
                    if (row[column['u_eventtype']]) == "Left-Down":
                        
                        lib2_bausteine.a_sequence_browser_click_start(xaml, str(row[column['u_name']]))
                        
                        lib2_bausteine.a_click_left_browser_schaltfläche(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                        # Baustein mit Tag+Type=Button in Kombination mit Abfrage nach Name des Feldes
                        lib2_bausteine.a_click_left_browser_schaltfläche_var_2(xaml, str(row[column['a_applicationname']]), url, str(row[column['u_name']]))
                        
                        #Baustein mit Tag=Button, Type=Submit in Kombination mit Abfrage nach Name des Feldes
                        lib2_bausteine.a_click_left_browser_schaltfläche_var_3(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        # Baustein der keine Tags enthält, sondern nur Name des Feldes
                        lib2_bausteine.a_click_left_browser_schaltfläche_var_4(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        lib2_bausteine.a_click_left_browser_schaltfläche_var_5(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        lib2_bausteine.a_click_left_browser_schaltfläche_var_6(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                        lib2_bausteine.a_sequence_browser_click_end(xaml)

                    #Rechtsklick?
                    if (row[column['u_eventtype']]) == "Right-down":
                        lib2_bausteine.a_click_right_browser_schaltfläche(xaml,str(row[column['a_applicationname']]),url,str(row[column['automationid']]))
                    
                    #Schließen des aktuellen Fensters
                    if (row[column['u_name']])=="Schließen" or "schließen" or "tab schließen": #name
                        lib2_bausteine.a_close_window(xaml)
                
                
                #Abfrage auf andere Eventtypen im Browser
                        
                if (row[column['u_type']]) == "checkbox":
                    lib2_bausteine.a_click_left_browser_checkbox(xaml, str(row[column['a_applicationname']]),url,str(row[column['automationid']]))

                if (row[column['u_type']]) == "Kombinationsfeld":
                    lib2_bausteine.a_click_kombinationsfeld(xaml, str(row[column['a_applicationname']), url, str(row[column['u_name'])) 
                                                                      
                if (row[column['u_type']])== "Option":
                    lib2_bausteine.a_click_single_browser_optionsfeld(xaml,str(row[column['a_applicationname']]), str(row[column['u_name']]), str(row[column['name']]))
                    lib_bausteine.a_comment_optionsfeld(xaml)
               
                #Wird ein Kalenderpicker verwendet? Dann Kommentar mit Hinweis
                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)
                    
                #Notwendige Texteingaben werden aus dem UI genommen, nicht direkt aus der Aufzeichnung, daher Text ausschließen
                if (row[column['u_type']])=="Text":
                    pass
                
                #Wen Type ein Link ist, dann wird zu diesem Link navigiert
                if (row[column['u_type']]) == "Link":
                    lib_bausteine.a_navigate_to(xaml, url)  # row 19= value, hier steht Link zu dem navigiert wird



                # Abfrage der Keystroke Aktivitäten im Browser

                if (row[column['u_type']]) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivität, bzw. Texteingabe
                    
                    if (row[column['u_eventtype']]) == "Left-Down":
                        lib2_bausteine.a_try_catch_try_start(xaml)
                        #try:
                        lib2_bausteine.a_type_into_browser (xaml, str(row[column['a_applicationname']]),url,str(row[column['automationid']])) #xaml, application_name, url, id
                        lib2_bausteine.a_try_catch_try_end(xaml)
                        #catch:
                        lib2_bausteine.a_try_catch_all_catches_start(xaml)
                        #wenn keine automationID
                        lib2_bausteine.a_try_catch_catch_start(xaml)
                        lib2_bausteine.a_type_into_browser_var2(xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        lib2_bausteine.a_try_catch_catch_end(xaml)
                        #wenn weder automationID noch name
                        lib2_bausteine.a_try_catch_catch_start(xaml)
                        lib2_bausteine.a_type_into_browser_var3(xaml, str(row[column['a_applicationname']]),url)
                        lib2_bausteine.a_try_catch_catch_end(xaml)
                        lib2_bausteine.a_try_catch_all_catches_end(xaml)

                    #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                    if (row[column['u_eventtype']]) == "CTRL + C":
                        lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['automationid']]))

                    #es wird etas eingefügt, Send Hotkey Strg+V
                    if (row[column['u_eventtype']]) == "CTRL + V":
                        lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['automationid']]))

                    if (row[column['u_eventtype']]) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)


            else: #dann keine Browseraktivität, sondern innerhalb Applikation -> gesonderte Bausteine, dann muss mit uia Tags gearbeitet werden

                #Explorer, wiederum gesonderte Bausteine da keine automationid, sondern name
                if (row[column['a_applicationname']])=="explorer": #dann ist es eine Aktivität im Explorer

                    if (row[column['u_type']]) == "Bearbeiten": #dann Keystroke
                        lib2_bausteine.a_type_into_explorer(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['role']]))  # xaml, application_name, title, id, name
                    
                    else: #dann immer Klick
                        if (row[column['u_eventtype']])=="Left-Down":
                            lib2_bausteine.a_click_left_in_explorer (xaml, str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['type']])) #xaml, windowtitle, Name des Feldes, role
                        else:
                            lib2_bausteine.a_click_right_in_explorer(xaml, str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['type']]))
                    
                    if (row[column['u_eventtype']]) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)



                else: #dann ist es eine Applikation

                #  gesonderte Bausteine für Klicks in Applikation
                    if (row[column['u_type']])=="Element":
                        if (row[column['u_eventtype']])=="Left-Down":
                            lib2_bausteine.a_click_single_in_application_element(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))
                        if (row[column['u_eventtype']]) == "Right-Down":
                            lib2_bausteine.a_click_right_in_application_element(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))
                        if (row[column['u_eventtype']])=="CTRL + C":
                            lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))
                        if (row[column['u_eventtype']])=="CTRL + V":
                            lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                    if (row[column['u_type']])=="Schaltfläche":
                        if (row[column['u_eventtype']]) == "Left-Down":
                            lib2_bausteine.a_click_single_in_application_schaltfläche(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))
                        else:
                            lib2_bausteine.a_click_right_in_application_schaltfläche(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                    if (row[column['u_type']]) == "Bearbeiten":
                        if (row[column['u_eventtype']]) == "Left-Down":
                            lib2_bausteine.a_type_into_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                        if (row[column['u_eventtype']]) == "CTRL + C":
                            lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                        if (row[column['u_eventtype']]) == "CTRL + V":
                            lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)


              #  v_a_applicationname=str(row[2])

        """ Leonie
        while row:                                            # process actions as recorded
           rowstr = ','.join(str(v) for v in row)
           if row[2] == "chrome" and row[0] == 3:
              a_chrome(xaml,"https://www.bahn.de",str(row[0]))
           else:
              a_comment(xaml,str(row[0]),rowstr)
           #xaml.write(rowstr + '\n')
          # row = cursor.fetchone()
        """
        lib_bausteine.writefoot(xaml) #schreibe Footer

    except psycopg2.Error as error:  # Fehlerhandling
        print("DB-Error ", error)
   # finally:
    #    if con():
     #       cursor.close()
      #      con.close()  # close connection to database



#Leonie
#if __name__ == '__main__':
 #   main(sys.argv[1]) #?

if __name__ == '__main__': #Main ausführen
    main()
