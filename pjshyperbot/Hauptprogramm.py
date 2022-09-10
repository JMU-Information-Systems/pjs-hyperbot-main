# Generate UIPath XAML from Logger DB
from aifc import Error
import sys
import sqlite3
from tkinter.tix import COLUMN
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gew�nschte Datenbank zu implementieren und SQL Befehle auszuf�hren
import pandas as pd
import urllib
import xaml as xaml
import lib_bausteine
import lib2_bausteine #Bausteine werden aus seperatem Skript importiert, bessere �bersichtlichkeit,
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
    v_a_applicationname="x" #Initialer Wert, nicht ver�ndern, wird unten abgefragt

    xaml = open("C:\\Users\\trist\\PycharmProjects\\output\\meine.xaml", "w", encoding="utf-8") #anpassen auf VM
    lib_bausteine.writehead(xaml) #Schreibe Header
    lib_bausteine.a_comment(xaml,"2", "F�r den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, ggf. sind Modifikationen notwendig")

    try:
       #Connect to postgres
       con=psycopg2.connect(
       host="132.187.102.173", #Host-IP
       database="processanalyzer", #Name der DB
       user="postgres", #user
       password="postgres") #password
       cursor=con.cursor()
    
        #Ausf�hrung des SQl Statements, userid wird aus json ausgelesen, automtationid und a_applicationname darf nicht leer sein, Order by timestamp
        #cursor.execute("Select * from public.th_alles where uilog_userid=%s and automationid != '' and automationid is not Null and a_applicationname !='' and a_applicationname is not null order by timestamp;",[userid]) #sql statement

    #Sodass nicht auf einzelne Spaltennummern zugegriffen werden muss, sondern der Zugriff �ber den Spaltennamen erfolgt
       def matching(cursor):
           results = {}
           column = 0
           for x in cursor.description:
               results[x[0]] = column
               column = column + 1
           return results

       column = matching(cursor)
       
       for row in cursor:
            
         #Anpassen der URL, trimmen  einf�gen von * sodass Selektor f�r alle Seiten dieser URL gilt
            
        from urllib.parse import urlparse
        a= urlparse(str(row[column['a_url']]))
        website_name = str(a.hostname)
        url = "*https://" + website_name + "*"

        
            #Abfrage auf Applikationen

            #Browser: Wenn der a_applicationname "Edge"  ist, handelt es sich um Browseraktivit�ten, deshalb hier andere Bausteine verwenden

        if (row[column['a_applicationname']]) == "msedge":

                #Abfrage auf Aktivit�ten �ber Spalte Type:
                if (row[column['u_type']]) == "Schaltfl�che" or "Kombinationsfeld": #dann ist es eine Klickakitivit�t

                    if str.__contains__(str(row[column['u_name']]), (("Minimieren") or ("Maximieren"))): #Ausschlu�, dies wird nicht automatisiert
                        pass

                    #Art des Klicks:Linksklick?
                    if (row[column['u_eventtype']]) == "Left-Down":
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, str(row[column['u_name']]))
                        
                        #Baustein Variante 1, �ber automationid, tag=Input, type=text
                        lib2_bausteine.a_click_left_browser_schaltfl�che(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                        # Baustein Variante 2, nur automationid 
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_2(xaml, str(row[column['a_applicationname']]), url, str(row[column['u_name']]), str(row[column['automationid']])))
                        
                        #Baustein Variante 3, mit  mit Tag+Type=Button in Kombination mit Abfrage nach Name (aaname) des Feldes 
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_3(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        # Baustein Variante 4, Tag=Button, Type=Submit in Kombination mit Abfrage nach Name des Feldes (aaname)
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_4(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        #Baustein Variante 5, aaname und Tag=A 
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_5(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        #Baustein Variante 6, nur aaname
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_6(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                        #Variante 7, Baustein mit Name & Tag=SPAN
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_7(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                        #Variante 8, �ber aaname und tag=Input
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_8(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        #Variante 9, �ber aaname und tag= Select
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_9(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                        #Variante 10, �ber name
                        lib2_bausteine.a_click_left_browser_schaltfl�che_var_9(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                        #Ende der Sequenz, alles zwischendrin wird ausprobiert
                        lib2_bausteine.a_sequence_end(xaml)


                    #Rechtsklick?
                    if (row[column['u_eventtype']]) == "Right-down":
                        lib2_bausteine.a_click_right_browser_schaltfl�che(xaml,str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                    
                    #Schlie�en des aktuellen Fensters
                    if (row[column['u_name']])=="Schlie�en" or "schlie�en" or "tab schlie�en": #name
                        lib2_bausteine.a_close_window(xaml)
                
                
                #Abfrage auf andere Eventtypen im Browser
                        
                if (row[column['u_type']]) == "checkbox":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_click_checkbox_start(xaml,str(row[column['u_name']]))

                    #Variante 1, �ber ID
                    lib2_bausteine.a_click_left_browser_checkbox(xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']]), str(row[column['automationid']]))

                    #Variante 2, �ber name
                    lib2_bausteine.a_click_left_browser_checkbox_var2((xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']])))

                    #Variante 3, �ber aaname
                    lib2_bausteine.a_click_left_browser_checkbox_var3((xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']])))
                    
                    lib2_bausteine.a_sequence_end(xaml)


                                                                          
                if (row[column['u_type']])== "Option":
                    lib2_bausteine.a_click_single_browser_optionsfeld(xaml,str(row[column['a_applicationname']]), url, str(row[column['u_name']]), str(row[column['automationid']]))
                    lib_bausteine.a_comment_optionsfeld(xaml)
               
                #Wird ein Kalenderpicker verwendet? Dann Kommentar mit Hinweis
                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)
                    
                #Notwendige Texteingaben werden aus dem UI genommen, nicht direkt aus der Aufzeichnung, daher Text ausschlie�en
                if (row[column['u_type']])=="Text":
                    pass
          
                #Wen Type ein Link ist, dann wird zu diesem Link navigiert
                if (row[column['u_type']]) == "Link":
                    lib_bausteine.a_navigate_to(xaml, str(row[column['u_value']]))  # row 19= value, hier steht Link zu dem navigiert wird

                # Abfrage der Keystroke Aktivit�ten im Browser

                if (row[column['u_type']]) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivit�t, bzw. Texteingabe
                    
                    if (row[column['u_eventtype']]) == "Left-Down":
                        
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml, str(row[column['u_name']]))
                        
                        #Variante 1, Suche �ber ID, tag=Input, type=Text
                        lib2_bausteine.a_type_into_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                        #Variante 2,wenn keine ID, Suche �ber Name und Tag=Input, Type=Text
                        lib2_bausteine.a_type_into_browser_var2 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))
                        
                        #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_type_into_browser_var3 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        #Variante 4, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_type_into_browser_var4 ((xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']])))

                        #Ende der Sequenz, alles zwischendrin wird ausprobiert
                        lib2_bausteine.a_sequence_end (xaml)


                    #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                    if (row[column['u_eventtype']]) == "CTRL + C":
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_start(xaml, str(row[column['u_name']]))

                        #Variante 1, Suche �ber ID, tag=Input, type=Text
                        lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))

                        #Variante 2,wenn keine ID, Suche �ber Name und Tag=Input, Type=Text
                        lib2_bausteine.a_send_hotkey_strg_c_browser_var2(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_send_hotkey_strg_c_browser_var3(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        #Variante 4, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_send_hotkey_strg_c_browser_var4 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        lib2_bausteine.a_sequence_end(xaml)

                    #es wird etas eingef�gt, Send Hotkey Strg+V
                    if (row[column['u_eventtype']]) == "CTRL + V":
                        
                        lib2_bausteine.a_sequence_send_hotkey_start(xaml, str(row[column['u_name']]))

                        #Variante 1, Suche �ber ID, tag=Input, type=Text
                        lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))

                        #Variante 2,wenn keine ID, Suche �ber Name und Tag=Input, Type=Text
                        lib2_bausteine.a_send_hotkey_strg_v_browser_var2(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_send_hotkey_strg_v_browser_var3(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        #Variante 4, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_send_hotkey_strg_v_browser_var4 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                        lib2_bausteine.a_sequence_end(xaml) 
                        
                       

                    if (row[column['u_eventtype']]) == "ENTER":
                        #Baustein f�r Enter
                        lib2_bausteine.a_press_enter(xaml)


        
                        
                        
                        
                        
        else: #dann keine Browseraktivit�t, sondern innerhalb Applikation -> gesonderte Bausteine, dann muss mit uia Tags gearbeitet werden

                #Explorer, wiederum gesonderte Bausteine
                if (row[column['a_applicationname']])=="explorer": #dann ist es eine Aktivit�t im Explorer

                    if (row[column['u_type']]) == "Bearbeiten": #dann Keystroke
                        
                        if (row[column['u_eventtype']]) == "Left-Down":
                            #Starten der Sequenz
                            lib2_bausteine.a_sequence_typeinto_start(xaml, str(row[column['u_name']]))
                        
                            #Variante 1, Abfrage auf automationid, name und role
                            lib2_bausteine.a_type_into_explorer(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['u_type']]))  # xaml, application_name, title, id, name
                        
                            #Variante 2, Abfrage auf automationid und name
                            lib2_bausteine.a_type_into_explorer_var2(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['automationid']])) 

                            #Variante 3, Abfrage auf name und role
                            lib2_bausteine.a_type_into_explorer_var3(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]),  str(row[column['role']])) 

                            #Variante 4, Abfrage nur auf name
                            lib2_bausteine.a_type_into_explorer_var4(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']])) 

                            #Ende der Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                        if (row[column['u_eventtype']]) == "CTRL + C":
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml, str(row[column['u_name']]))

                            #�ber ID, name und role, uia Selektor
                            lib2_bausteine.a_send_hotkey_strg_c_in_explorer(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['automationid']]), str(row[column['u_type']]))
                            
                            #Variante 2, Abfrage auf automationid und name
                            lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var2(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']]))
                            
                            #Variante 3, Abfrage auf name und role
                            lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var3(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]),  str(row[column['u_type']]))
                            
                            #Variante 4, Abfrage nur auf name
                            lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var4(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']])) 
                           
                            #Ende der Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                        if (row[column['u_eventtype']]) == "CTRL + V":
                            
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml, str(row[column['u_name']]))

                            #�ber ID, name und role, uia Selektor
                            lib2_bausteine.a_send_hotkey_strg_v_in_explorer(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['automationid']]), str(row[column['u_type']]))
                            
                            #Variante 2, Abfrage auf automationid und name
                            lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var2(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']]))
                            
                            #Variante 3, Abfrage auf name und role
                            lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var3(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]),  str(row[column['u_type']]))
                            
                             #Variante 4, Abfrage nur auf name
                            lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var4(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']])) 
                           
                            #Ende der Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                    else: #dann immer Klick
                        
                        if (row[column['u_eventtype']])=="Left-Down":
                            
                            #Start der Sequenz
                            lib2_bausteine.a_sequence_click_start(xaml,str(row[column['u_name']]))
                            
                            #Variante 1, Abfrage auf name und role
                            lib2_bausteine.a_click_left_in_explorer (xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']])) #xaml, windowtitle, Name des Feldes, role

                            #Variante 2, Abfrage nur auf name
                            lib2_bausteine.a_click_left_in_explorer_var_2 (xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]))
                            
                            #Variante 3, Abfrage auf id und name
                            lib2_bausteine.a_click_left_in_explorer_var_3(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['automationid']]), str(row[column['u_name']]))

                            #Ende der Sequenz
                            lib2_bausteine.a_sequence_end(xaml)


                        else:
                            lib2_bausteine.a_click_right_in_explorer(xaml, str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['u_type']]))
                    
                    if (row[column['u_eventtype']]) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)



                else: #dann ist es eine Applikation

                #  gesonderte Bausteine f�r Klicks in Applikation
                    
                
                    if (row[column['u_type']])=="Element":
                        if (row[column['u_eventtype']])=="Left-Down" or "Right-Down":
                            pass #dann wird zB nur eine Excel Zeile angeklickt, bekommen wir schon �ber die nachfolgende Aktion
                                
                        if (row[column['u_eventtype']])=="CTRL + C":
                            #Start Sequenz
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml,str(row[column['u_name']]))

                            #Abfrage �ber automationid und role
                            lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                            #Variante 2, �ber name und role
                            lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                            #Variante 3, �ber aaname und ctrl Tag
                            lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                            #End Sequenz
                            lib2_bausteine.a_sequence_end(xaml)


                            
                        if (row[column['u_eventtype']])=="CTRL + V":
                             #Start Sequenz
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml,str(row[column['u_name']]))

                            #Abfrage �ber automationid und role
                            lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                            #Variante 2, �ber name und role
                            lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                            #Variante 3, �ber aaname und ctrl Tag
                            lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                            #End Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                    if (row[column['u_type']]) == "Bearbeiten":
                        if (row[column['u_eventtype']]) == "Left-Down":
                            #Start Sequenz
                            lib2_bausteine.a_sequence_typeinto_start(xaml,str(row[column['u_name']]))

                            #Variante 1, �ber automationid und role
                            lib2_bausteine.a_type_into_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['automationid']]),str(row[column['u_type']]))

                            #Variante 2, �ber name und role
                            lib2_bausteine.a_type_into_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))

                            #Variante 3, �ber aaname und ctrl Tag
                            lib2_bausteine.a_type_into_application_var3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                        if (row[column['u_eventtype']]) == "CTRL + C":
                            
                            #Start Sequenz
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml,str(row[column['u_name']]))

                            #Abfrage �ber automationid und role
                            lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                            #Variante 2, �ber name und role
                            lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                            #Variante 3, �ber aaname und ctrl Tag
                            lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                            #End Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                        if (row[column['u_eventtype']]) == "CTRL + V":
                             #Start Sequenz
                            lib2_bausteine.a_sequence_send_hotkey_start(xaml,str(row[column['u_name']]))

                            #Abfrage �ber automationid und role
                            lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                            #Variante 2, �ber name und role
                            lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                            #Variante 3, �ber aaname und ctrl Tag
                            lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                            #End Sequenz
                            lib2_bausteine.a_sequence_end(xaml)
                            
                           
                            
                            
                    else: #um alle Klickaktivit�ten abzudecken
                        
                        if (row[column['u_eventtype']]) == "Left-Down":
                            #Start Sequenz
                            lib2_bausteine.a_sequence_click_start(xaml,str(row[column['u_name']]))
                            
                            #Variante 1, �ber name und role
                            lib2_bausteine.a_click_single_in_application_var2(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']]))
                           
                        
                            #Variante 2, �ber automationid, name und role
                            lib2_bausteine.a_click_single_in_application(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]), str(row[column['u_name']]),str(row[column['u_type']]))
                           

                            #Variante 3, �ber name und Tag ctrl
                            lib2_bausteine.a_click_single_in_application_var3(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]))
                            
                            #Variante 4, �ber aaname und tag ctrl
                            lib2_bausteine.a_click_single_in_application_var4(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]))
                          
                            #Ende Sequenz
                            lib2_bausteine.a_sequence_end(xaml)

                        else:
                            lib2_bausteine.a_click_right_in_application_schaltfl�che(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))

                    

                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)


        lib_bausteine.writefoot(xaml) #schreibe Footer
    
    except psycopg2.Error as error: # Fehlerhandlind 
        print("DB-Error ", error)
   
       # finally:
    #    if con():
     #       cursor.close()
      #      con.close()  # close connection to database

#Leonie
#if __name__ == '__main__':
 #   main(sys.argv[1]) #?

if __name__ == '__main__': #Main ausf�hren
    main()
