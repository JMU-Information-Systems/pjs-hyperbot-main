# Generate UIPath XAML from Logger DB
# coding=utf-8
from aifc import Error
from ast import Not
from distutils.errors import LibError
from pickle import NONE
import sys
import sqlite3
from tkinter.tix import COLUMN
import psycopg2 #Modul um eine Verbindung zum Datenbanksystem postgres herzustellen, gewünschte Datenbank zu implementieren und SQL Befehle auszuführen
#import pandas as pd
import urllib
from urllib.parse import urlparse
from collections import deque
#import xaml as xaml Datei?
import lib_bausteine
import lib2_bausteine #Bausteine werden aus seperatem Skript importiert

# argument is the name of the database as produced by the prepare plus additional table for input/output links
def main(dbname):
    filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml

    xaml = open(filename,"w", encoding="utf-8")
    endknoten = deque() # stack, um Endknotenhierarchie aufzuheben
    akt_name = NONE
    #offene_apps() =[] #collection/Liste

    endknoten.append(lib_bausteine.activity(xaml)) #schreibe Activity Header und nimm den return Wert (Endknoten) in den Stapel auf
    endknoten.append(lib_bausteine.sequence(xaml)) #schreibe Sequence Header und nimm den return Wert (Endknoten) in den Stapel auf
    
    
    lib_bausteine.a_comment(xaml,"2", "Für den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, ggf. sind Modifikationen notwendig")

    #Connect to SQLite
    l_database = sqlite3.connect(dbname)
    cursor = l_database.cursor()
    cursor.execute("SELECT * FROM logger ORDER BY e_id")  # importiere Datenbank
    #strg_c_excel= cursor.execute("SELECT COUNT (*) FROM testdatensatz2 where a_applicationname='excel' and u_eventtype='CTRL + C'")
    #number_of_strg_c_excel= strg_c_excel.fetchone()[0]
        

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

        #Prüfe, ob sich der Applikationsname ändert, um Bodys zu bilden
        if akt_name != str(row[column['a_applicationname']]):
            if akt_name != NONE:
                xaml.write(endknoten.pop())
            akt_name = str(row[column['a_applicationname']])
            
            #if a_applicationname in open applicaions attach else
            if str(row[column['a_applicationname']]) == "msedge":
                    endknoten.append(lib2_bausteine.a_edge_browser_start(xaml, url))
            elif str(row[column['a_applicationname']]) == "excel":
                    endknoten.append(lib2_bausteine.a_excel_application_scope(xaml, "workbook_path"))
            elif str(row[column['a_applicationname']]) == "word":
                    endknoten.append(lib2_bausteine.a_word_application_scope (xaml, "workbook_path"))
            else:
                endknoten.append(lib2_bausteine.a_open_application(str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), "C:\\Program Files\\"+str(row[column['a_applicationname']])+"\\"+str(row[column['a_applicationname']])+".exe"))


        aktionen(url, xaml, str(row[column['automationid']]), str(row[column['u_name']]), str(row[column['u_type']]), str(row[column['u_eventtype']]), str(row[column['u_value']]), str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]))
    

    #baue alle noch offenen Endknoten vom Stack ab
    while endknoten.__len__() > 0:
        test = endknoten.__len__()
        xaml.write(str(endknoten.pop()))       
        


#Abfrage auf Applikationen

#Browser: Wenn der a_applicationname "Edge"  ist, handelt es sich um Browseraktivitäten in MS Edge
def aktionen(url, xaml, automationid, u_name, u_type, u_eventtype, u_value, a_applicationname, a_windowtitle):
    if a_applicationname == "msedge":
                
            if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend"))):
                lib_bausteine.a_comment_calendar_picker(xaml)

            #Abfrage auf Aktivitäten über Spalte Type:
            if u_type == "Schaltfläche": #dann ist es eine Klickakitivität

                if str.__contains__(u_name, (("Minimieren") or ("Maximieren"))): #Ausschluß, dies wird nicht automatisiert
                    pass

                #Art des Klicks:Linksklick?
                if u_eventtype == "Left-Down":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_click_start(xaml, u_name)
                        
                    #Baustein Variante 1, über automationid, tag=Input, type=text
                    lib2_bausteine.a_click_left_browser_schaltfläche(xaml, a_applicationname,url, u_name, automationid)
                        
                    # Baustein Variante 2, nur automationid 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_2(xaml, a_applicationname, url, u_name, automationid)
                        
                    #Baustein Variante 3, mit  mit Tag+Type=Button in Kombination mit Abfrage nach Name (aaname) des Feldes 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_3(xaml,a_applicationname, url,u_name)
                        
                    # Baustein Variante 4, Tag=Button, Type=Submit in Kombination mit Abfrage nach Name des Feldes (aaname)
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_4(xaml,a_applicationname,url,u_name)
                        
                    #Baustein Variante 5, aaname und Tag=A 
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_5(xaml,a_applicationname,url,u_name)
                        
                    #Baustein Variante 6, nur aaname
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_6(xaml,a_applicationname,url,u_name)

                    #Variante 7, Baustein mit Name & Tag=SPAN
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_7(xaml,a_applicationname,url, u_name)

                    #Variante 8, über aaname und tag=Input
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_8(xaml,a_applicationname,url,u_name)
                        
                    #Variante 9, über aaname und tag= Select
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_9(xaml,a_applicationname,url,u_name)

                    #Variante 10, über name
                    lib2_bausteine.a_click_left_browser_schaltfläche_var_10(xaml,a_applicationname,url,u_name)
                        
                    #Ende der Sequenz, alles zwischendrin wird ausprobiert
                    lib2_bausteine.a_sequence_end(xaml)


                #Rechtsklick?
                if (u_eventtype) == "Right-down":
                    lib2_bausteine.a_click_right_browser_schaltfläche(xaml,a_applicationname,url, u_name, automationid)
                    
                #Schließen des aktuellen Fensters
                # if (row[column['u_name']])=="Schließen" or "schließen" or "tab schließen": #name
                    #k   lib2_bausteine.a_close_window(xaml)
                
                
            #Abfrage auf andere Eventtypen im Browser                        
            if (u_type)=="Kombinationsfeld":
                lib2_bausteine.a_click_kombinationsfeld(xaml,a_applicationname,url, u_name, automationid)
            

            if (u_type) == "checkbox":
                #Starten der Sequenz
                #lib2_bausteine.a_sequence_click_checkbox_start(xaml,u_name)

                #Variante 1, über ID
                lib2_bausteine.a_click_left_browser_checkbox(xaml, a_applicationname,url,u_name, automationid)

                #Variante 2, über name
                lib2_bausteine.a_click_left_browser_checkbox_var2(xaml, a_applicationname,url,u_name)

                #Variante 3, über aaname
                lib2_bausteine.a_click_left_browser_checkbox_var3(xaml, a_applicationname,url, u_name)
                    
                #lib2_bausteine.a_sequence_end(xaml)
                    
                                                                        
            if (u_type)== "Option":
                lib2_bausteine.a_click_single_browser_optionsfeld(xaml,a_applicationname, url, u_name, automationid)
                lib_bausteine.a_comment_optionsfeld(xaml)
               
            #Wird ein Kalenderpicker verwendet? Dann Kommentar mit Hinweis
            if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend"))):
                lib_bausteine.a_comment_calendar_picker(xaml)
                    
            #Notwendige Texteingaben werden aus dem UI genommen, nicht direkt aus der Aufzeichnung, daher Text ausschließen
            if (u_type)=="Text":
                pass
          
            #Wen Type ein Link ist, dann wird zu diesem Link navigiert
            if (u_type) == "Link":
                lib_bausteine.a_navigate_to(xaml, u_value)  # row 19= value, hier steht Link zu dem navigiert wird

            # Abfrage der Keystroke Aktivitäten im Browser

            if (u_type) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivität, bzw. Texteingabe
                    
                if (u_eventtype) == "Left-Down":
                        
                    #Start der Sequenz
                    lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)
                        
                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_type_into_browser(xaml, a_applicationname,url, u_name, automationid, "Text")
                        
                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_type_into_browser_var2 (xaml, a_applicationname,url, u_name, "Text")
                        
                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_type_into_browser_var3 (xaml, a_applicationname,url, u_name, "Text")

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_type_into_browser_var4 (xaml, a_applicationname,url, u_name, "Text")

                    #Ende der Sequenz, alles zwischendrin wird ausprobiert
                    lib2_bausteine.a_sequence_end (xaml)


                #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                if (u_eventtype) == "CTRL + C":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)

                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, a_applicationname,url, u_name, automationid)

                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var2(xaml, a_applicationname,url, u_name)

                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var3(xaml, a_applicationname,url, u_name)

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_send_hotkey_strg_c_browser_var4 (xaml, a_applicationname,url, u_name)

                    lib2_bausteine.a_sequence_end(xaml)

                #es wird etwas eingefügt, Send Hotkey Strg+V
                if (u_eventtype) == "CTRL + V":
                        
                    lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                    #Variante 1, Suche über ID, tag=Input, type=Text
                    lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, a_applicationname,url, u_name, automationid)

                    #Variante 2,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var2(xaml, a_applicationname,url, u_name)

                    #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var3(xaml, a_applicationname,url, u_name)

                    #Variante 4, keine ID, kein Name, nur Tag=Input
                    lib2_bausteine.a_send_hotkey_strg_v_browser_var4 (xaml, a_applicationname,url, u_name)

                    lib2_bausteine.a_sequence_end(xaml) 

                #Baustein für Enter                               
                if (u_eventtype) == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)
 
                                              
    else: #dann keine Browseraktivität, sondern eine Applikation mit gesonderten Bausteinen (dann muss mit uia Tags gearbeitet werden)

            #Explorer, eigene Bausteine
            if (a_applicationname)=="explorer": 
                    
                if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)

                if (u_type) == "Bearbeiten": #dann Keystroke
                        
                    if (u_eventtype) == "Left-Down":
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)
                        
                        #Variante 1, Abfrage auf automationid, name und role
                        lib2_bausteine.a_type_into_explorer(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)
                        
                        #Variante 2, Abfrage auf automationid und name
                        lib2_bausteine.a_type_into_explorer_var2(xaml, a_applicationname, a_windowtitle, u_name, automationid) 

                        #Variante 3, Abfrage auf name und role
                        lib2_bausteine.a_type_into_explorer_var3(xaml, a_applicationname, a_windowtitle, u_name, u_type)  #str(row[column['role']]) 

                        #Variante 4, Abfrage nur auf name
                        lib2_bausteine.a_type_into_explorer_var4(xaml, a_applicationname, a_windowtitle, u_name) 

                        #Ende der Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    if (u_eventtype) == "CTRL + C":
                            
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)

                        #über ID, name und role, uia Selektor
                        lib2_bausteine.a_send_hotkey_strg_c_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                            
                        #Variante 2, Abfrage auf automationid und name
                        lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                            
                        #Variante 3, Abfrage auf name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var3(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                            
                        #Variante 4, Abfrage nur auf name
                        lib2_bausteine.a_send_hotkey_strg_c_in_explorer_var4(xaml, a_applicationname, a_windowtitle, u_name) 
                           
                        #Ende der Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    if (u_eventtype) == "CTRL + V":
                            
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                        #über ID, name und role, uia Selektor
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                            
                        #Variante 2, Abfrage auf automationid und name
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                            
                        #Variante 3, Abfrage auf name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var3(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                            
                            #Variante 4, Abfrage nur auf name
                        lib2_bausteine.a_send_hotkey_strg_v_in_explorer_var4(xaml, a_applicationname, a_windowtitle, u_name) 
                           
                        #Ende der Sequenz
                        #lib2_bausteine.a_sequence_end(xaml)

                    
                if (u_eventtype) == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)
                            
                            
                else: #dann immer Klick
                        
                    if (u_eventtype)=="Left-Down":
                            
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, u_name)
                            
                        #Variante 1, Abfrage auf name und role
                        lib2_bausteine.a_click_left_in_explorer (xaml, a_applicationname, a_windowtitle, u_name, u_type) #xaml, windowtitle, Name des Feldes, role

                        #Variante 2, Abfrage nur auf name
                        lib2_bausteine.a_click_left_in_explorer_var_2 (xaml, a_applicationname, a_windowtitle, u_name)
                            
                        #Variante 3, Abfrage auf id und name
                        lib2_bausteine.a_click_left_in_explorer_var_3(xaml, a_applicationname, a_windowtitle, automationid, u_name)

                        #Ende der Sequenz
                        #lib2_bausteine.a_sequence_end(xaml)


                    else:
                        lib2_bausteine.a_click_right_in_explorer(xaml, automationid, u_name, u_type)
                    

            else: #dann ist es eine Applikation

                #gesonderte Bausteine für Klicks in Applikation
                    
                #if (row[column[a_applicationname]])=="excel":
                #    lib2_bausteine.a_excel_application_scope(xaml, hier muss Pfad rein)
                #nach den Excel Bausteinen, speichert Excel
                #    lib2_bausteine.a_excel_auto_save (xaml)

                #if (row[column[a_applicationname]])=="msword":
                #    lib2_bausteine.a_word_application_scope(xaml, hier muss Pfad rein)

                #für andere Applikationen zum Öffnen
                #lib2_bausteine.a_open_application(xaml, a_applicationname, a_windowtitle, root):)

                if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend"))):
                    lib_bausteine.a_comment_calendar_picker(xaml)

                if (u_type)=="Element":
                    if (u_eventtype)=="Left-Down" or "Right-Down":
                        pass #dann wird zB nur eine Excel Zeile angeklickt, bekommen wir schon über die nachfolgende Aktion
                                
                    if (u_eventtype)=="CTRL + C":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)


                            
                    if (u_eventtype)=="CTRL + V":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                if (u_type) == "Bearbeiten":
                    if (u_eventtype) == "Left-Down":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)

                        #Variante 1, über automationid und role
                        lib2_bausteine.a_type_into_application(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)

                        #Variante 2, über name und role
                        lib2_bausteine.a_type_into_application_var_2(xaml, a_applicationname, a_windowtitle, u_name, u_type)

                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_type_into_application_var3(xaml, a_applicationname, a_windowtitle, u_name)

                    if (u_eventtype) == "CTRL + C":
                            
                        #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_var_3(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    if (u_eventtype) == "CTRL + V":
                            #Start Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                        #Variante 2, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_var_3(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                                       
                            
                else: #um alle Klickaktivitäten abzudecken
                        
                    if (u_eventtype) == "Left-Down":
                        #Start Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, u_name)
                            
                        #Variante 1, über name und role
                        lib2_bausteine.a_click_single_in_application(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                           
                        
                        #Variante 2, über automationid, name und role
                        lib2_bausteine.a_click_single_in_application_var2(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)
                           

                        #Variante 3, über name und Tag ctrl
                        lib2_bausteine.a_click_single_in_application_var3(xaml, a_applicationname, a_windowtitle, u_name)
                            
                        #Variante 4, über aaname und tag ctrl
                        lib2_bausteine.a_click_single_in_application_var4(xaml, a_applicationname, a_windowtitle, u_name)
                          
                        #Ende Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                    else:
                        lib2_bausteine.a_click_right_in_application(a_applicationname, a_windowtitle, automationid)
                
  

       #Verbesserungsvorschläge am Ende:
       #lib2_bausteine.a_sequence_auskommentiert(xaml)


    #if number_of_strg_c_excel>=3:
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

        #lib2_bausteine.a_sequence_end(xaml)
        #lib2_bausteine.a_sequence_auskommentiert_end(xaml) #am Ende wenn alle Vorschläge gemacht wurden

   
       # finally:
    #    if con():
     #       cursor.close()
      #      con.close()  # close connection to database

if __name__ == '__main__':
    main(sys.argv[1]) #um Datein als eigenständiges Programm zu nutzen und Elemente importierbar zu machen