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
    offene_apps = deque() #Liste, welche Applikationsnamen der bereits offenen Anwendungen enthält

    endknoten.append(lib_bausteine.activity(xaml)) #schreibe Activity Header und nimm den return Wert (Endknoten) in den Stapel auf
    endknoten.append(lib_bausteine.sequence(xaml)) #schreibe Sequence Header und nimm den return Wert (Endknoten) in den Stapel auf
    
    
    lib_bausteine.a_comment(xaml,"2", "Für den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, ggf. sind Modifikationen notwendig")

    #Connect to SQLite
    l_database = sqlite3.connect(dbname)
    cursor = l_database.cursor()
    cursor.execute("SELECT * FROM logger ORDER BY e_id")  # importiere Datenbank

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
        #bei der URL von WeClapp, funktioniert das Trimmen mit dem Modul urllib.parse nicht, deshalbt gesonderte Anpassung
        
        if (str(row[column['a_url']])).__contains__("132.187.226.138:8080/"):
            url="*132.187.226.138:8080/*"
        else:
            #Trimmen der URLS
            from urllib.parse import urlparse 
            a_url = str(row[column['a_url']])
            a = urlparse(str(row[column['a_url']]))
            website_name = str(a.hostname)
            url = "*https://" + website_name + "/*"

        #Fehlerhandling, falls Sonderzeichen wie "&" in Spalte "name" vorhanden sind entfernen
        u_name= str(row[column['u_name']])
        if str(row[column['a_applicationname']]) == "msedge":
            u_name=str(row[column['u_name']]).replace("<","&lt;").replace("&", "&amp;amp;")
        else:
            u_name=""

        #Prüfe, ob sich der Applikationsname ändert, um Bodys zu bilden
        if akt_name != str(row[column['a_applicationname']]):
            if akt_name != NONE:
                xaml.write(endknoten.pop())
            akt_name = str(row[column['a_applicationname']])
            
            #if a_applicationname in open applicaions attach else open browser
            if str(row[column['a_applicationname']]) in offene_apps:
                if str(row[column['a_applicationname']]) == "msedge":
                        endknoten.append(lib2_bausteine.a_edge_browser_attach(xaml, a_url))
                else:
                    endknoten.append(lib2_bausteine.a_attach_application(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']])))
            else:
                offene_apps.append(akt_name)
                if str(row[column['a_applicationname']]) == "msedge":
                        endknoten.append(lib2_bausteine.a_edge_browser_start(xaml, a_url))
                elif str(row[column['a_applicationname']]) == "excel":
                        endknoten.append(lib2_bausteine.a_excel_application_scope(xaml, "workbook_path"))
                elif str(row[column['a_applicationname']]) == "word":
                        endknoten.append(lib2_bausteine.a_word_application_scope(xaml, "workbook_path"))
                else:
                    endknoten.append(lib2_bausteine.a_open_application(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]), "C:\\Program Files\\"+str(row[column['a_applicationname']])+"\\"+str(row[column['a_applicationname']])+".exe"))


        aktionen(url, a_url, xaml, str(row[column['automationid']]), u_name, str(row[column['u_type']]), str(row[column['u_eventtype']]), str(row[column['u_value']]), str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]))
    

    #baue alle noch offenen Endknoten vom Stack ab
    while endknoten.__len__() > 0:
        test = endknoten.__len__()
        xaml.write(str(endknoten.pop()))       
        


#Abfrage auf Applikationen

#Browser: Wenn der a_applicationname "Edge"  ist, handelt es sich um Browseraktivitäten in MS Edge
def aktionen(url, a_url, xaml, automationid, u_name, u_type, u_eventtype, u_value, a_applicationname, a_windowtitle, input_variables):
    
    if a_applicationname == "msedge":
            
            #Wird ein Kalenderpicker verwendet? Dann Kommentar mit Hinweis
            if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend") or ("datepicker"))):
                lib_bausteine.a_comment_calendar_picker(xaml)
            

            #Schließen des aktuellen Fensters
                # if (row[column['u_name']])=="Schließen" or "schließen" or "tab schließen": #name
                    #k   lib2_bausteine.a_close_window(xaml)


            #Abfrage auf Aktivitäten über Spalte Type:

            #Ist ein Wert in der Spalte automationid vorhanden?
            #größer 0, d.h. es wurde eine ID mit aufgezeichnet
            
            if len(automationid)>0: 
            
                if u_type == "Schaltfläche" or "Link": #dann ist es eine Klickakitivität

                    if str.__contains__(u_name, (("Minimieren") or ("Maximieren") or ("Abbrechen"))): #Ausschluss, dies wird nicht automatisiert
                        pass

                    #Art des Klicks:Linksklick?
                    if u_eventtype == "Left-Down":
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, u_name)
                        
                        #Baustein Variante 1, über automationid, tag=Input, type=text
                        lib2_bausteine.a_click_left_browser_schaltfläche_id(xaml, a_applicationname,url, u_name, automationid)
                        
                        # Baustein Variante 2, nur automationid 
                        lib2_bausteine.a_click_left_browser_schaltfläche_id_var_2(xaml, a_applicationname, url, u_name, automationid)

                        #Baustein Variante 3, mit aaname und parentid
                        lib2_bausteine.a_click_left_browser_schaltfläche_id_var_3(xaml, a_applicationname, url, u_name, automationid)
                        
                        #Ende der Sequenz, alles zwischendrin wird ausprobiert
                        lib2_bausteine.a_sequence_end(xaml)

                    #Rechtsklick
                    else:
                        lib2_bausteine.a_click_right_browser_schaltfläche(xaml,a_applicationname,url, u_name, automationid)
            
            
                #Abfrage auf andere Eventtypen im Browser                        

                elif (u_type)=="Kombinationsfeld":
                    lib2_bausteine.a_click_kombinationsfeld(xaml,a_applicationname,url, u_name, automationid)        
            
                elif (u_type) == "checkbox" or "Kontrollkästchen": #manchmal auf deutsch, manchmal englisch vom Logger
                    #Variante über ID
                    lib2_bausteine.a_click_left_browser_checkbox(xaml, a_applicationname,url,u_name, automationid)
      
                elif (u_type)== "Optionsfeld":
                    #Variante 1, nur über ID
                    lib2_bausteine.a_click_left_browser_optionsfeld(xaml,a_applicationname, url, u_name,automationid)

                #wie Kombinationsfeld, nur wenn ID vorhanden ist berücksichtigen. Identifikation über parentid
                elif (u_type)=="Gruppe":
                    lib2_bausteine.a_click_gruppe(xaml,a_applicationname, u_name, automationid)
                    
                # Abfrage der Keystroke Aktivitäten im Browser

                elif (u_type) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivität
                    
                    #Bedingung für Texteingabe
                    if (u_eventtype) == "Left-Down":       

                        #Suche über ID, tag=Input, type=Text
                        lib2_bausteine.a_type_into_browser(xaml, a_applicationname,url, u_name, automationid, input_variables)
                    
                    #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                    
                    elif (u_eventtype) == "CTRL + C":

                        #ID, tag=Input, type=Text
                        lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, a_applicationname,url, u_name, automationid)

                    elif (u_eventtype) == "CTRL + V":

                        #ID, tag=Input, type=Text
                        lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, a_applicationname,url, u_name, automationid)
                     
                    #Baustein für Enter 
                    elif (u_eventtype) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)
                        
            #dann gibt es keine ID
            else:
                 #Bedingung für Klickaktivität
                 if u_type == "Schaltfläche" or "Link":

                     #Linksklick
                     if u_eventtype == "Left-Down":
                        
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, u_name)

                        #Baustein Variante 1, nur über aaname
                        lib2_bausteine.a_click_left_browser_schaltfläche_no_id(xaml,a_applicationname, url,u_name)
                        
                        #Baustein Variante 2, mit Tag+Type=Button in Kombination mit Abfrage nach Name (aaname) des Feldes 
                        lib2_bausteine.a_click_left_browser_schaltfläche_no_id_var2(xaml,a_applicationname, url,u_name)
                        
                        #Baustein Variante 3, Tag=Button, Type=Submit in Kombination mit Abfrage nach Name des Feldes (aaname)
                        lib2_bausteine.a_click_left_browser_schaltfläche_no_id_var3(xaml,a_applicationname,url,u_name)
                        
                        #Baustein Variante 4, aaname und Klasse
                       # lib2_bausteine.a_click_left_browser_schaltfläche_no_id_var4(xaml,a_applicationname,url,u_name,u_class)
                        
                        #Baustein Variante 5, mit aaname und Tag=Span 
                        lib2_bausteine.a_click_left_browser_schaltfläche_no_id_var5 (xaml,a_applicationname,url, u_name)

                        #Variante 6, Baustein mit Name & Tag=Select
                        lib2_bausteine.a_click_left_browser_schaltfläche_no_id_var6(xaml,a_applicationname,url,u_name)
                      
                        lib2_bausteine.a_sequence_end(xaml)

                     elif (u_eventtype) == "Right-down":
                        lib2_bausteine.a_click_right_browser_schaltfläche(xaml,a_applicationname,url, u_name, automationid)


                 elif (u_type)=="Kombinationsfeld":
                    lib2_bausteine.a_click_kombinationsfeld(xaml,a_applicationname,url, u_name, automationid)

                 elif (u_type) == "checkbox" or "Kontrollkästchen": #manchmal auf deutsch, manchmal englisch vom Logger
                    
                    #Start der Sequenz
                    lib2_bausteine.a_sequence_click_checkbox_start(xaml, u_name)

                    #Variante mit name, tag=Input, type=checkbox
                    lib2_bausteine.a_click_left_browser_checkbox_no_id (xaml, a_applicationname, url, u_name)

                    #Variante 2, über aaname, Tag=Input, type=checkbox
                    lib2_bausteine.a_click_left_browser_checkbox_no_id_var2(xaml, a_applicationname,url, u_name)
                    
                    #Ende der Sequenz
                    lib2_bausteine.a_sequence_end(xaml)

                 elif (u_type)== "Optionsfeld":
                    #Starten der Sequenz
                    lib2_bausteine.a_sequence_click_optionsfeld_start(xaml,u_name)
                
                    #Variante 1, über aaname und aria-role=option
                    lib2_bausteine.a_click_left_browser_optionsfeld_no_id(xaml,a_applicationname, url, u_name)
                
                    #Variante 2, nur über aaname
                    lib2_bausteine.a_click_left_browser_optionsfeld_var_no_id_var2(xaml,a_applicationname, url, u_name)
                    
                    #Ende der Sequenz
                    lib2_bausteine.a_sequence_end(xaml)
                    #lib_bausteine.a_comment_optionsfeld(xaml)
                
                 #keine ID
                 elif (u_type)=="Text":

                    #Start der Sequenz
                    lib2_bausteine.a_sequence_click_start(xaml, u_name)
                    #Variante 1, über aaname und tag=LABEL
                    lib2_bausteine.a_click_browser_text(xaml,a_applicationname, url, u_name)

                    #Variante 2, nur über aaname
                    lib2_bausteine.a_click_browser_text_var2(xaml,a_applicationname, url, u_name)

                    #Ende der Sequenz
                    lib2_bausteine.a_sequence_end(xaml)

                
                 elif (u_type) == "Bearbeiten":  # d.h. es ist eine Keystroke Aktivität, bzw. Texteingabe
                    
                    if (u_eventtype) == "Left-Down":

                        #Start der Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)
                     
                        #Suche über Name und Tag=Input, Type=Text
                        lib2_bausteine.a_type_into_browser_no_id(xaml, a_applicationname,url, u_name, input_variables)
                        
                        #Variante 3, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_type_into_browser_no_id_var2(xaml, a_applicationname,url, u_name, input_variables)

                        #Variante 4, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_type_into_browser_no_id_var3 (xaml, a_applicationname,url, u_name, input_variables)

                        #Ende der Sequenz, alles zwischendrin wird ausprobiert
                        lib2_bausteine.a_sequence_end (xaml)
                       
                    
                    #es wird etwas kopiert, d.h. Baustein Send Hotkey Strg+C
                    
                    elif (u_eventtype) == "CTRL + C":
                        
                        #Starten der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)

                        #Variante 1,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                        lib2_bausteine.a_send_hotkey_strg_c_browser_no_id(xaml, a_applicationname,url, u_name)

                        #Variante 2, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_send_hotkey_strg_c_browser_no_id_var2(xaml, a_applicationname,url, u_name)

                        #Variante 3, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_send_hotkey_strg_c_browser_no_id_var3(xaml, a_applicationname,url, u_name)

                        lib2_bausteine.a_sequence_end(xaml)

                    
                   #es wird etwas eingefügt, Send Hotkey Strg+V

                    elif (u_eventtype) == "CTRL + V":
                        
                        #Start der Sequenz     
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                        #Variante 1,wenn keine ID, Suche über Name und Tag=Input, Type=Text
                        lib2_bausteine.a_send_hotkey_strg_v_browser_no_id(xaml, a_applicationname,url, u_name)

                        #Variante 2, keine ID, kein Name, nur Tag=Input, type =text
                        lib2_bausteine.a_send_hotkey_strg_v_browser_no_id_var2(xaml, a_applicationname,url, u_name)

                        #Variante 3, keine ID, kein Name, nur Tag=Input
                        lib2_bausteine.a_send_hotkey_strg_v_browser_no_id_var3(xaml, a_applicationname,url, u_name)

                        lib2_bausteine.a_sequence_end(xaml) 
                           
                    #Baustein für Enter 
                    elif (u_eventtype) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)
               
 
    if (a_applicationname)=="explorer": 
            
            if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend") or ("datepicker"))):
                lib_bausteine.a_comment_calendar_picker(xaml)

            if (u_type) == "Bearbeiten": 
                
                if (u_eventtype) == "Left-Down": #dann ist es eine Texteingabe
                   
                   #Variante 1, Abfrage auf automationid, name und role   
                    lib2_bausteine.a_type_into_explorer(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type, input_variables)
                
                elif (u_eventtype) == "CTRL + C":
                    #über ID, name und role, uia Selektor
                    lib2_bausteine.a_send_hotkey_strg_c_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                  
                elif (u_eventtype) == "CTRL + V":
                    #über ID, name und role, uia Selektor
                    lib2_bausteine.a_send_hotkey_strg_v_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                 
                elif (u_eventtype) == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)    
            
                
            else: #dann immer Klickaktivität, keine weitere Unterscheidung nach Typ notwendig, da dieser immer mitgeliefert wird und mit Logger übereinstimmt
                    
                if (u_eventtype)=="Left-Down":
                    #Linksklick, Name und Role
                    lib2_bausteine.a_click_left_in_explorer(xaml, a_applicationname, a_windowtitle, u_type)
                  
                else: #Rechtsklick, Name und Role
                    lib2_bausteine.a_click_right_in_explorer(xaml, a_applicationname, a_windowtitle, u_type)
                    

                 
    else: #dann ist es eine Applikation, gesonderte Bausteine
                    
            if str.__contains__(u_name, (("Kalender") or ("Calendar") or ("Calend") or ("datepicker"))):
                lib_bausteine.a_comment_calendar_picker(xaml)

            if a_applicationname=="excel":
                lib2_bausteine.a_excel_auto_save(xaml)

            #wird ID mit aufgezeichnet?
            if len(automationid)>0:

                if (u_type)=="Element":
                    
                    if (u_eventtype)=="Left-Down" or "Right-Down":
                        pass #dann wird zB nur eine Excel Zeile angeklickt, bekommen wir schon über die nachfolgende Aktion
                                
                    elif (u_eventtype)=="CTRL + C":
                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                    elif (u_eventtype)=="CTRL + V":
                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                    
                        
                    elif (u_eventtype) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml) 
                        
                elif (u_type) == "Bearbeiten":
                    
                    if (u_eventtype) == "Left-Down":
                        #Type Into mit automationid und role
                        lib2_bausteine.a_type_into_application(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type, input_variables)

                    elif (u_eventtype) == "CTRL + C":
                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type)
                        
                    elif (u_eventtype) == "CTRL + V":  
                        #Abfrage über automationid und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_type) 
                       
                    elif (u_eventtype) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)                   
                
                #um alle Klickaktivitäten abzudecken
                else:
                        
                    if (u_eventtype) == "Left-Down":
           
                        #über automationid, name und role
                        lib2_bausteine.a_click_single_in_application_var2(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)
                    
                    else: 
                        lib2_bausteine.a_click_right_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)
            
            #dann gibt es keine ID            
            else: 
                if (u_type)=="Element":
                    
                    if (u_eventtype)=="Left-Down" or "Right-Down":
                        pass #dann wird zB nur eine Excel Zeile angeklickt, bekommen wir schon über die nachfolgende Aktion
                                
                    elif (u_eventtype)=="CTRL + C":
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)
                        
                        #Variante 1, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 2, über aaname und wnd Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                    
                             
                    elif (u_eventtype)=="CTRL + V":
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)
                        
                        #Variante 1, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 2, über aaname und wnd Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                        
                        
                    elif (u_eventtype) == "ENTER":
                        lib2_bausteine.a_press_enter(xaml)    
                       
                    
                elif (u_type)=="Bearbeiten":
                    
                    if (u_eventtype)=="Left-Down" or "Right-Down":

                        #Start Sequenz
                        lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)

                        #Variante 2, über name und role
                        lib2_bausteine.a_type_into_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type, input_variables)

                        #Variante 3, über aaname und ctrl Tag
                        lib2_bausteine.a_type_into_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name, input_variables)
                        
                        #Ende der Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                                
                    elif (u_eventtype)=="CTRL + C":
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)
                        
                        #Variante 1, über name und role
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 2, über aaname und wnd Tag
                        lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                    
                             
                    elif (u_eventtype)=="CTRL + V":
                        #Start der Sequenz
                        lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)
                        
                        #Variante 1, über name und role
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                          
                        #Variante 2, über aaname und wnd Tag
                        lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name)

                        #End Sequenz
                        lib2_bausteine.a_sequence_end(xaml)
                        
                        
                        
                    
                #um Klickaktivitäten abzudecken
                else: 

                    if (u_eventtype) == "Left-Down":
                        
                        #Start Sequenz
                        lib2_bausteine.a_sequence_click_start(xaml, u_name)
                            
                        #Variante 1, über name und role
                        lib2_bausteine.a_click_single_in_application_no_id (xaml, a_applicationname, a_windowtitle, u_name, u_type)
                                
                        #Variante 2, über name und Tag ctrl
                        lib2_bausteine.a_click_single_in_application_no_id_var2(xaml, a_applicationname, a_windowtitle, u_name)
                            
                        #Variante 4, über aaname und tag ctrl
                        lib2_bausteine.a_click_single_in_application_no_id_var3 (xaml, a_applicationname, a_windowtitle, u_name)
                          
                        #Ende Sequenz
                        lib2_bausteine.a_sequence_end(xaml)

                        
                    else:
                        lib2_bausteine.a_click_right_in_application_var2(xaml, a_applicationname, a_windowtitle, u_name, u_type)
              
                

''' 
def verbesserungsvorschläge():
    #Verbesserungsvorschläge am Ende:
    
    #Zählen wie oft etwas im Prozessverlauf aus Excel kopiert wird
    #strg_c_excel= cursor.execute("SELECT COUNT (*) FROM logger where a_applicationname='excel' and u_eventtype='CTRL + C'")
    #number_of_strg_c_excel= strg_c_excel.fetchone()[0]
       
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

   
   

        '''

if __name__ == '__main__':
    main(sys.argv[1]) #um Datein als eigenständiges Programm zu nutzen und Elemente importierbar zu machen