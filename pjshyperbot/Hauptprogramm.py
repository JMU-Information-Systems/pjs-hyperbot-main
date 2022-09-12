# Generate UIPath XAML from Logger DB
from aifc import Error
from pickle import NONE
import sys
import sqlite3
from tkinter.tix import COLUMN
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gewünschte Datenbank zu implementieren und SQL Befehle auszuführen
import pandas as pd
import urllib
from collections import deque
#import xaml as xaml
from urllib.parse import urlparse
import lib_bausteine
import lib2_bausteine #Bausteine werden aus seperatem Skript importiert, bessere Übersichtlichkeit

# argument is the name of the database as produced by the prepare plus additional table for input/output links
def main(dbname):
    filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml

    xaml = open(filename,"w", encoding="utf-8")
    endknoten = deque() # stack, um Endknotenhierarchie aufzuheben
    
    #Declaration Section
    v_zaehler=0
    v_a_applicationname="x" #Initialer Wert, nicht verändern, wird unten abgefragt

    ret = lib_bausteine.activity_head #schreibe Activity Header und nimm den return Wert (Endknoten) in den Stapel auf
    if ret != NONE:
        endknoten.append(ret)
    ret = lib_bausteine.sequence_head #schreibe Sequence Header und nimm den return Wert (Endknoten) in den Stapel auf
    if ret != NONE:
        endknoten.append(ret)
    
    
    lib_bausteine.a_comment(xaml,"2", "Für den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, ggf. sind Modifikationen notwendig")

        #Connect to SQLLite
        #db_pfad = ("C:\\Program Files\\DB Browser for SQLite\\test2.db")

        #l_database = sqlite3.connect(db_pfad)
        #cursor = l_database.cursor()
        #cursor.execute("Select * from testdaten3")  # importiere Datenbank
        #strg_c_excel= cursor.execute("SELECT COUNT (*) FROM testdatensatz2 where a_applicationname='excel' and u_eventtype='CTRL + C'")
        #
        #number_of_strg_c_excel= strg_c_excel.fetchone()[0]
        


        #if number_of_strg_c_excel>=3:
            #Start der Sequenz:
            #lib2_bausteine.a_sequence_read_range_start (xaml):
            #lib2_bausteine.a_read_range(outputtable_name, range, sheet_name, workbook_path)) Variablen müssen vom Frontend kommen
            #lib2_bausteine.a_comment_read_range (xaml)
            #Ende der Sequenz
            #lib2_bausteine.a_sequence_end(xaml)


        #wenn Nutzer im Frontend auswählt, dass er Data Scraping machen möchte
        #Start der Sequenz
        #lib2_bausteine.a_sequence_data_scraping_start
        #lib2_bausteine.a_comment_data_scraping (xaml):
        #lib2_bausteine.a_write_range_excel (xaml, datatable, sheetname, workbookpath): #aus Frontend die Variablen
        #Ende der Sequenz
        #lib2_bausteine.a_sequence_end(xaml)


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
            
        a = urlparse(str(row[column['a_url']]))
        website_name = str(a.hostname)
        url = "*https://" + website_name + "*"

        
        #Abfrage auf Applikationen

        #Browser: Wenn der a_applicationname "Edge"  ist, handelt es sich um Browseraktivitäten, deshalb hier andere Bausteine verwenden

    if (row[column['a_applicationname']]) == "msedge":
                
            if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                lib_bausteine.a_comment_calendar_picker(xaml)

            #Abfrage auf Aktivitäten über Spalte Type:
            if (row[column['u_type']]) == "Schaltfläche" or "Kombinationsfeld": #dann ist es eine Klickakitivität

                if str.__contains__(str(row[column['u_name']]), (("Minimieren") or ("Maximieren"))): #Ausschluß, dies wird nicht automatisiert
                    pass

                #Art des Klicks:Linksklick?
                if (row[column['u_eventtype']]) == "Left-Down":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_click_start(xaml, str(row[column['u_name']]))
                        
                    #Baustein Variante 1, über automationid, tag=Input, type=text
                    lib2_bausteine.a_click_left_browser_schaltfläche(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                    # Baustein Variante 2, nur automationid 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_2(xaml, str(row[column['a_applicationname']]), url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                    #Baustein Variante 3, mit  mit Tag+Type=Button in Kombination mit Abfrage nach Name (aaname) des Feldes 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_3(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                    # Baustein Variante 4, Tag=Button, Type=Submit in Kombination mit Abfrage nach Name des Feldes (aaname)
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_4(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                    #Baustein Variante 5, aaname und Tag=A 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_5(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                    #Baustein Variante 6, nur aaname
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_6(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                    #Variante 7, Baustein mit Name & Tag=SPAN
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_7(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                    #Variante 8, über aaname und tag=Input
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_8(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                    #Variante 9, über aaname und tag= Select
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_9(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                    #Variante 10, über name
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_10(xaml,str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                        
                    #Ende der Sequenz, alles zwischendrin wird ausprobiert
                    lib2_bausteine.a_sequence_end(xaml)


                #Rechtsklick?
                if (row[column['u_eventtype']]) == "Right-down":
                    lib2_bausteine.a_click_right_browser_schaltfläche(xaml,str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                    
                #Schließen des aktuellen Fensters
                # if (row[column['u_name']])=="Schließen" or "schließen" or "tab schließen": #name
                    #k   lib2_bausteine.a_close_window(xaml)
                
                
            #Abfrage auf andere Eventtypen im Browser
                        
            if (row[column['u_type']]) == "checkbox":
                #Starten der Sequenz
                lib2_bausteine.a_sequence_click_checkbox_start(xaml,str(row[column['u_name']]))

                #Variante 1, über ID
                lib2_bausteine.a_click_left_browser_checkbox(xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']]), str(row[column['automationid']]))

                #Variante 2, über name
                lib2_bausteine.a_click_left_browser_checkbox_var2(xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']]))

                #Variante 3, über aaname
                lib2_bausteine.a_click_left_browser_checkbox_var3(xaml, str(row[column['a_applicationname']]),url,str(row[column['u_name']]))
                    
                lib2_bausteine.a_sequence_end(xaml)
                    


                                                                          
            if (row[column['u_type']])== "Option":
                lib2_bausteine.a_click_single_browser_optionsfeld(xaml,str(row[column['a_applicationname']]), url, str(row[column['u_name']]), str(row[column['automationid']]))
                lib_bausteine.a_comment_optionsfeld(xaml)
               
            #Wird ein Kalenderpicker verwendet? Dann Kommentar mit Hinweis
            if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                lib_bausteine.a_comment_calendar_picker(xaml)
                    
            #Notwendige Texteingaben werden aus dem UI genommen, nicht direkt aus der Aufzeichnung, daher Text ausschließen
            if (row[column['u_type']])=="Text":
                pass
          
            #Wen Type ein Link ist, dann wird zu diesem Link navigiert
            if (row[column['u_type']]) == "Link":
                lib_bausteine.a_navigate_to(xaml, str(row[column['u_value']]))  # row 19= value, hier steht Link zu dem navigiert wird

            # Abfrage der Keystroke Aktivitäten im Browser

            if (row[column['u_type']]) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivität, bzw. Texteingabe
                    
                if (row[column['u_eventtype']]) == "Left-Down":
                        
                    #Start der Sequenz
                    lib2_bausteine.a_sequence_typeinto_start(xaml, str(row[column['u_name']]))
                        
                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_type_into_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))
                        
                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_type_into_browser_var2 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))
                        
                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_type_into_browser_var3 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_type_into_browser_var4 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Ende der Sequenz, alles zwischendrin wird ausprobiert
                    lib2_bausteine.a_sequence_end (xaml)


                #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                if (row[column['u_eventtype']]) == "CTRL + C":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, str(row[column['u_name']]))

                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))

                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var2(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var3(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var4 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    lib2_bausteine.a_sequence_end(xaml)

                #es wird etas eingefügt, Send Hotkey Strg+V
                if (row[column['u_eventtype']]) == "CTRL + V":
                        
                    lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml,str(row[column['u_name']]))

                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]), str(row[column['automationid']]))

                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var2(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var3(xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var4 (xaml, str(row[column['a_applicationname']]),url, str(row[column['u_name']]))

                    lib2_bausteine.a_sequence_end(xaml) 
                        
                       

                if (row[column['u_eventtype']]) == "ENTER":
                    #Baustein für Enter
                    lib2_bausteine.a_press_enter(xaml)


        
                        
                        
                        
                        
    else: #dann keine Browseraktivität, sondern innerhalb Applikation -> gesonderte Bausteine, dann muss mit uia Tags gearbeitet werden

            #Explorer, wiederum gesonderte Bausteine
            if (row[column['a_applicationname']])=="explorer": #dann ist es eine Aktivität im Explorer
                    
                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)

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
                            
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, str(row[column['u_name']]))

                        #über ID, name und role, uia Selektor
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
                            
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml,str(row[column['u_name']]))

                        #über ID, name und role, uia Selektor
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['automationid']]), str(row[column['u_type']]))
                            
                        #Variante 2, Abfrage auf automationid und name
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var2(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']]))
                            
                        #Variante 3, Abfrage auf name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var3(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']]),  str(row[column['u_type']]))
                            
                            #Variante 4, Abfrage nur auf name
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var4(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), str(row[column['u_name']])) 
                           
                        #Ende der Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    
                if (row[column['u_eventtype']]) == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)
                            
                            
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
                    



            else: #dann ist es eine Applikation

            #  gesonderte Bausteine für Klicks in Applikation
                    
                #if (row[column[a_applicationname]])=="excel":
                #    lib2_bausteine.a_excel_application_scope(xaml, hier muss Pfad rein)
                #nach den Excel Bausteinen, speichert Excel
                #    lib2_bausteine.a_excel_auto_save (xaml)

                #if (row[column[a_applicationname]])=="msword":
                #    lib2_bausteine.a_word_application_scope(xaml, hier muss Pfad rein)

                #für andere Applikationen zum öffnen
                #lib2_bausteine.a_open_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), root):)

                if str.__contains__(str(row[column['u_name']]), (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)

                if (row[column['u_type']])=="Element":
                    if (row[column['u_eventtype']])=="Left-Down" or "Right-Down":
                        pass #dann wird zB nur eine Excel Zeile angeklickt, bekommen wir schon über die nachfolgende Aktion
                                
                    if (row[column['u_eventtype']])=="CTRL + C":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml,str(row[column['u_name']]))

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)


                            
                    if (row[column['u_eventtype']])=="CTRL + V":
                            #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml,str(row[column['u_name']]))

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                if (row[column['u_type']]) == "Bearbeiten":
                    if (row[column['u_eventtype']]) == "Left-Down":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml,str(row[column['u_name']]))

                        #Variante 1, über automationid und role
                        lib2_bausteine.a_type_into_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['automationid']]),str(row[column['u_type']]))

                        #Variante 2, über name und role
                        lib2_bausteine.a_type_into_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))

                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_type_into_application_var3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                    if (row[column['u_eventtype']]) == "CTRL + C":
                            
                        #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, str(row[column['u_name']]))

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    if (row[column['u_eventtype']]) == "CTRL + V":
                            #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml,str(row[column['u_name']]))

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]),str(row[column['u_type']]))
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]), str(row[column['u_type']]))
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['u_name']]))

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                            
                           
                            
                            
                else: #um alle Klickaktivitäten abzudecken
                        
                    if (row[column['u_eventtype']]) == "Left-Down":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml,str(row[column['u_name']]))
                            
                        #Variante 1, über name und role
                        lib2_bausteine.a_click_single_in_application_var(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]), str(row[column['u_type']]))
                           
                        
                        #Variante 2, über automationid, name und role
                        lib2_bausteine.a_click_single_in_application_var2(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]), str(row[column['u_name']]),str(row[column['u_type']]))
                           

                        #Variante 3, über name und Tag ctrl
                        lib2_bausteine.a_click_single_in_application_var3(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]))
                            
                        #Variante 4, über aaname und tag ctrl
                        lib2_bausteine.a_click_single_in_application_var4(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]), str(row[column['u_name']]))
                          
                        #Ende Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    else:
                        lib2_bausteine.a_click_right_in_application_schaltfläche(xaml,str(row[column['a_applicationname']]),str(row[column['a_windowtitle']]),str(row[column['automationid']]))
                

    while endknoten.count > 0: #baue alle noch offenen Endknoten vom Stack ab
        xaml.write(endknoten.pop())

   
       # finally:
    #    if con():
     #       cursor.close()
      #      con.close()  # close connection to database

if __name__ == '__main__':
    main(sys.argv[1]) #um Datein als eigenständiges Programm zu nutzten und Elemente impoertierbar zu machen