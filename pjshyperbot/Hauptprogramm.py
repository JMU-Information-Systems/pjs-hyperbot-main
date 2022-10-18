# Generate UIPath XAML from Logger DB
# coding=utf-8

from aifc import Error
from ast import Not
from asyncio.windows_events import NULL
from distutils.errors import LibError
from pickle import NONE
import sys
import sqlite3
from tkinter.tix import COLUMN
from urllib.parse import urlparse
from collections import deque
import lib_bausteine
import lib2_bausteine


# argument is the name of the database as produced by the prepare plus additional table for input/output links
def main(dbname,task, dataScraping, path):
    filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml
    mypath=path
    mydataScraping=dataScraping

    # connect to SQLite
    l_database = sqlite3.connect(dbname)
    cursor = l_database.cursor()

    xaml = open(filename,"w", encoding="utf-8")
    endknoten = deque() # stack for closing end node hierarchy
    akt_name = NONE
    offene_apps = deque() # list with open applications

    endknoten.append(lib_bausteine.activity(xaml)) # write sequence header and add the return value (Endknoten) into the stack
    endknoten.append(lib_bausteine.sequence(xaml)) # write sequence header and add the return value (Endknoten) into the stack
    endknoten.append(lib_bausteine.s_varaibles(xaml))# write variables header and add the return value (Endknoten) into the stack
    cursor.execute("SELECT * FROM variables ORDER BY v_id")  #read variable table
    
    #Initialize that columns can be queried by column name
    def matching(cursor):
        results = {}
        column = 0
        for x in cursor.description:
            results[x[0]] = column
            column = column + 1
        return results
    column = matching(cursor)

    for row in cursor:
        lib_bausteine.variable(xaml, str(row[column['vname']]), str(row[column['vtype']]), str(row[column['vinit']]))
    xaml.write(str(endknoten.pop()))
    cursor.close()
    
    #Calling the module a_comment and insert comment at the beginning
    lib_bausteine.a_comment(xaml,"2", "Für den aufgezeichneten Prozess wurde automatische eine xaml Datei erzeugt, bitte manuelle Nachbearbeitung über Debug Mode vornehmen")
    
    
    #Module manually for variable extraction from WeClapp, for this the name of the template must be given=task
    endknoten.append(lib2_bausteine.a_sequence_variablenextraktion(xaml, task))
    
    # write get text for all variables to be extracted 
    cursor = l_database.cursor()
    cursor.execute("SELECT * FROM variables ORDER BY v_id")   
    for row in cursor:
        lib2_bausteine.a_get_text (xaml, str(row[column['v_id']]), str(row[column['vname']]))
    xaml.write(str(endknoten.pop()))
    cursor.close()

    #Initialize the cursor and start the connection to the database
    cursor = l_database.cursor()
    cursor.execute("SELECT * FROM logger ORDER BY e_id")  #read logger table

    #Initialize that columns can be queried by column name, so that it is not necessary to access individual column numbers
    def matching(cursor):
        results = {}
        column = 0
        for x in cursor.description:
            results[x[0]] = column
            column = column + 1
        return results

    column = matching(cursor)
     
    ##initialization of the url_before variable needed for comparison with previous set
    url_before=None
    

    for row in cursor:   
        
        #Customizing the URL. Trimming the URLS with urllib parse and removing the special characters, setting * so that selector is valid for all pages of this URL. 
        from urllib.parse import urlparse 
        a_url = str(row[column['a_url']]).replace("&","&amp;")
        a = urlparse(str(row[column['a_url']]))
        website_name = str(a.hostname)
        
        #Here separate trimming, since urllib parse does not take effect
        if (str(row[column['a_url']])).__contains__("132.187.226.138:8080/"):
            url="*132.187.226.138:8080/*"
        
        elif str(row[column['a_applicationname']]) == "msedge":
            url = "*https://" + website_name + "/*"
        
        else:
            url=a_url

        #Error handling, if special characters like "&" are present in column "name" they are removed
        u_name= str(row[column['u_name']])

        if str(row[column['a_applicationname']]) == "notepad++":
            u_name=""
        else:
            u_name=str(row[column['u_name']]).replace("<","&lt;").replace(">","&gt;").replace("&", "&amp;amp;").replace("\'","&apos;").replace("\"","&quot;")

        # check if the application name is changed to form container
        if akt_name != str(row[column['a_applicationname']]):
            if akt_name != NONE:
                xaml.write(endknoten.pop())
            akt_name = str(row[column['a_applicationname']])
            
            #if a_applicationname is in open applications attach the application or Browser else open the application or Browser
            if str(row[column['a_applicationname']]) in offene_apps:
                if str(row[column['a_applicationname']]) == "msedge":
                        endknoten.append(lib2_bausteine.a_edge_browser_attach(xaml, url))
                else:
                    endknoten.append(lib2_bausteine.a_attach_application(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']])))
            else:
                offene_apps.append(akt_name)
                if str(row[column['a_applicationname']]) == "msedge":
                        endknoten.append(lib2_bausteine.a_edge_browser_start(xaml, a_url))
                elif str(row[column['a_applicationname']]) == "excel":
                        endknoten.append(lib2_bausteine.a_excel_application_scope(xaml, path))
                elif str(row[column['a_applicationname']]) == "winword":
                        endknoten.append(lib2_bausteine.a_word_application_scope(xaml, path))
                elif str(row[column['a_applicationname']]) == "explorer":
                        endknoten.append(lib2_bausteine.a_open_explorer(xaml, str(row[column['a_windowtitle']])))
                else:
                    endknoten.append(lib2_bausteine.a_open_application(xaml, str(row[column['a_applicationname']]), str(row[column['a_windowtitle']])))
                    lib2_bausteine.a_comment_open_application (xaml)

        # url is modified url on domain which we need for selector, 
        # a_url is the original URL, which we need for opening the browser and navigating to a page.
        #url_before is the modified URL of the previous set, which is used for comparison with the current URL and calls the navigate module if it changes
        
        #Calling the actions function
        aktionen(url, a_url,url_before, xaml, str(row[column['automationid']]), u_name, str(row[column['u_type']]), str(row[column['u_eventtype']]), str(row[column['u_value']]), str(row[column['a_applicationname']]), str(row[column['a_windowtitle']]),str(row[column['elementclass']]), str(row[column['input_variables']]))
        
        #Current value becomes predecessor value if it is not None. If activity has no url, no url should be taken over
        if url != 'None':
            url_before=url

    cursor.close()
    
    #remove all open end nodes from the stack
    while endknoten.__len__() > 0:
        if endknoten.__len__() ==2:
            for app in offene_apps:
                lib2_bausteine.a_close_window(xaml, app)
            verbesserungsvorschlaege(xaml,dbname, mydataScraping)
        xaml.write(str(endknoten.pop()))       
        


#Query on applications by looping through the row, Matching criteria between log data and blocks, calling blocks and passing the variables to generate the selectors


def aktionen(url, a_url,url_before, xaml, automationid, u_name, u_type, u_eventtype, u_value, a_applicationname, a_windowtitle,elementclass, input_variables):
    
    #Query of the event type in order not to have to distinguish between left and right clicks in the browser activities
    #Value can not be taken over directly because log data differ, therefore adjustment
    if u_eventtype=="Left-Down":
        u_eventtype="BTN_LEFT"

    if u_eventtype=="Right-Down":
        u_eventtype="BTN_RIGHT"
    
    #initialize test list on datepicker, if yes, comment is given with hint on how to handle datepickers 
    #triggers if word exists in column (can also be just a substring), case insensitive
    test_datepicker=['kalender', 'calendar', 'calend', 'datepick','timepick']
    
    # Check if word from list test_datepicker occurs in these columns
    check = (u_name + " " + elementclass + " " + automationid)

    #converts all uppercase letters to lowercase to make check insensitive
    check_upper_lower=check.lower()

    #Query on activities
    if a_applicationname == "msedge":

        #Windowtitle must be trimmed for using the selectors in the browser, because data from logger does not match exactly at the end. 
        #Therefore trim after the first word and generate a dynamic selector with*

        trim=a_windowtitle
        trim_windowtitle=trim.split(' ',2)
        trimmed_windowtitle=trim_windowtitle[0]+"*"
        
        #If url changes to the predecessor, navigate to the next page

        if url != url_before and url_before is not None:
            lib_bausteine.a_navigate_to(xaml, a_url)

        
        #Is a calendar picker used? Automations are difficult, therefore comment and note to the post-processor
        if any (x in check_upper_lower for x in test_datepicker):
            lib_bausteine.a_comment_calendar_picker(xaml)

        

        #Query on activities via column Type:
            
        #Check if the activity has a value assigned in the automationid column. If the length is greater than 0, an ID has been recorded.
        #Then only one module variant is necessary 
            
        if len(automationid)>0: 
            if u_type == "Schaltfläche" or u_type=="Link": #click acitivity
                 
                lib2_bausteine.a_click_browser_schaltfläche_id(xaml, a_applicationname, url, u_name, automationid, u_eventtype)
            
            #query on other event types in the browser and call the blocks, pass the variables                        

            elif u_type == "Kombinationsfeld":
                lib2_bausteine.a_click_kombinationsfeld(xaml,a_applicationname,url, u_name, automationid, u_eventtype)        
            
            elif u_type == "checkbox" or (u_type) == "Kontrollkästchen":
                #Using the ID of the UI element
                lib2_bausteine.a_click_browser_checkbox(xaml, a_applicationname,url,u_name, automationid, u_eventtype)
      
            elif u_type== "Optionsfeld":
                #Using the ID of the UI element
                lib2_bausteine.a_click_browser_optionsfeld(xaml,a_applicationname, url, u_name,automationid, u_eventtype)

            #like a combo box
            elif u_type=="Gruppe":
                lib2_bausteine.a_click_gruppe(xaml,a_applicationname, url, u_name, automationid, u_eventtype)  

                    
            # Query the keystroke activities in the browser

            #these types are fields where text is entered, i.e. keystroke activities
            elif u_type == "Bearbeiten" or u_type=="Suchfeld" or u_type=="Telefonnummer": 
                #Bedingung für Texteingabe
                if u_eventtype == "BTN_LEFT" or u_eventtype=="BTN_RIGHT":      

                    #Using ID and tag=Input
                    lib2_bausteine.a_type_into_browser(xaml, a_applicationname,url, u_name, automationid, input_variables)
                 
                #if there is an @character in the input, the logger returns the following expression. Same Type Into block
                elif u_eventtype=="CTRL + ALT + ALTGR + Q":
                    lib2_bausteine.a_type_into_browser(xaml, a_applicationname,url, u_name, automationid, input_variables) 
                
                #Copy shortcut combination, i.e. block Send Hotkey Ctrl+C     
                elif u_eventtype == "CTRL + C":

                    #ID, tag=Input
                    lib2_bausteine.a_send_hotkey_strg_c_browser(xaml, a_applicationname,url, u_name, automationid)

                #Insert shortcut combination, i.e. block Send Hotkey Ctrl+V
                elif u_eventtype == "CTRL + V":

                    #ID, tag=Input
                    lib2_bausteine.a_send_hotkey_strg_v_browser(xaml, a_applicationname,url, u_name, automationid)

                        
        #Else Block: then there is no ID, identification of elements not always guaranteed, therefore using variants for same activity
        #The variants are within a sequence to keep the clarity in the postprocessing
        #Therefore, each variant block starts with a start sequence, then the variants and finally the closing of the variant block.

        else:
            #Click activity condition
            if u_type == "Schaltfläche":
                #Starting the sequence
                lib2_bausteine.a_sequence_start_schaltflaeche (xaml, u_name)

                #Module variant 1, with wnd tag, attriute name and role, role push button
                lib2_bausteine.a_click_browser_schaltfläche_no_id (xaml,a_applicationname, trimmed_windowtitle, u_name, u_eventtype)
                        
                #Module variant 2, with html tag and attribute aaname
                lib2_bausteine.a_click_browser_schaltfläche_no_id_var2(xaml,a_applicationname, url,u_name, u_eventtype)
                        
                #Module variant 3, with html tag and attribute elementclass
                lib2_bausteine.a_click_browser_schaltfläche_no_id_var3(xaml, a_applicationname, url, u_name, elementclass, u_eventtype)
                
                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)

            elif u_type=="Link":
                #Start of Sequence
                lib2_bausteine.a_sequence_click_start(xaml, u_name)
                
                #Module variant 1, with wnd tag, attriute name and role, role link
                lib2_bausteine.a_click_browser_link_no_id(xaml, a_applicationname, trimmed_windowtitle, u_name, u_eventtype)
                
                ##Module variant 2, with html tag and attribute aaname und elementclass
                lib2_bausteine.a_click_browser_link_no_id_var2(xaml,a_applicationname, url, u_name, elementclass, u_eventtype)

                lib2_bausteine.a_sequence_end(xaml)

            elif u_type=="Kombinationsfeld":
                
                #Starting the sequence
                lib2_bausteine.a_sequence_click_kombinationsfeld_start(xaml)

                #Module variant 1, with wnd tag, attriute name and role. Role combo-box
                lib2_bausteine.a_click_kombinationsfeld_no_id(xaml, a_applicationname, trimmed_windowtitle, u_name, u_eventtype)

                #Baustein 2, Module 2, with html tag and attribute aaname 
                lib2_bausteine.a_click_kombinationsfeld_no_id_var2(xaml, a_applicationname, url,u_name, u_eventtype)

                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)



            elif u_type == "checkbox" or u_type=="Kontrollkästchen": #manchmal auf deutsch, manchmal englisch vom Logger
                
                #Starting the sequence
                lib2_bausteine.a_sequence_click_checkbox_start(xaml, u_name)

                #Module variant 1, with wnd tag, attriute name and role. Role check box
                lib2_bausteine.a_click_browser_checkbox_no_id (xaml, a_applicationname, trimmed_windowtitle, u_name, u_eventtype)

                #Module variant 2, Variante 2, html tag und Attribut aaname
                lib2_bausteine.a_click_left_browser_checkbox_no_id_var2(xaml, a_applicationname,url, u_name, u_eventtype)
                    
                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)


            elif u_type== "Optionsfeld":
                #Starting the sequence
                lib2_bausteine.a_sequence_click_optionsfeld_start(xaml,u_name)
                
                #Module variant 1, wnd tag and attribute name and role. role radio button
                lib2_bausteine.a_click_browser_optionsfeld_no_id(xaml,a_applicationname, trimmed_windowtitle, u_name, u_eventtype)
                
                #Modul variant 2, html Tag, Attribut aaname 
                lib2_bausteine.a_click_browser_optionsfeld_var_no_id_var2(xaml,a_applicationname, url, u_name, elementclass, u_eventtype)
                    
                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)
               
                
            #does not exist with id, therefore only here query  
            elif u_type=="Text":

                #Sequence start
                lib2_bausteine.a_sequence_click_start(xaml, u_name)

                #Module variant 1, wnd tag and attribute name and role. role editable text
                lib2_bausteine.a_click_browser_text(xaml,a_applicationname, trimmed_windowtitle, u_name, u_eventtype)

                #Modul variant 2, html Tag, Attribut aaname 
                lib2_bausteine.a_click_browser_text_var2(xaml,a_applicationname, url, u_name, u_eventtype)

                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)

            elif u_type=="Gruppe":
                #Type Group
                lib2_bausteine.a_click_gruppe_no_id(xaml, a_applicationname, trimmed_windowtitle, u_name, u_eventtype)

              
            elif u_type=="Grafik":

                #Sequence start
                lib2_bausteine.a_sequence_click_grafik_start(xaml)

                #Module variant 1, wnd tag and attribute name and role. role editable text
                lib2_bausteine.a_click_browser_grafik (xaml, a_applicationname, trimmed_windowtitle, u_name, u_eventtype)

                #Modul variant 2, html Tag, Attribut aaname 
                lib2_bausteine.a_click_browser_grafik_var2(xaml, a_applicationname, url, u_name, u_eventtype)

                #End of sequence
                lib2_bausteine.a_sequence_end(xaml)

            # i.e. it is a keystroke activity, resp. text input    
            elif u_type == "Bearbeiten":  
                
                if u_eventtype == "BTN_LEFT" or u_eventtype=="BTN_RIGHT":
                    #Sequence start
                    lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)
                    
                    #Modul variant 1, attribute name
                    lib2_bausteine.a_type_into_browser_no_id(xaml, a_applicationname,url, u_name, input_variables)
                        
                    #Modul variant 2
                    lib2_bausteine.a_type_into_browser_no_id_var2(xaml, a_applicationname,url, u_name, input_variables)

                    #End of sequence
                    lib2_bausteine.a_sequence_end (xaml)


                #wenn in der Eingabe ein @Zeichen vorkommt, gibt der Logger folgenden Ausdruck zurück. Gleicher Type Into Baustein
                elif u_eventtype=="CTRL + ALT + ALTGR + Q":
                    #Sequence start
                    lib2_bausteine.a_sequence_typeinto_start(xaml, u_name)
                    
                    #Modul variant 1
                    lib2_bausteine.a_type_into_browser_no_id(xaml, a_applicationname,url, u_name, input_variables)
                        
                    #odul variant 2
                    lib2_bausteine.a_type_into_browser_no_id_var2(xaml, a_applicationname,url, u_name, input_variables)

                    #End of sequence
                    lib2_bausteine.a_sequence_end (xaml)
   
                    
                #something is copied, i.e. block Send Hotkey Ctrl+C
                    
                elif u_eventtype == "CTRL + C":
                    #Start of sequence
                    lib2_bausteine.a_sequence_send_hotkey_Strg_C_start(xaml, u_name)
                
                    #Module variant 1
                    lib2_bausteine.a_send_hotkey_strg_c_browser_no_id(xaml, a_applicationname,url, u_name)

                    #Module variante 2
                    lib2_bausteine.a_send_hotkey_strg_c_browser_no_id_var2(xaml, a_applicationname,url, u_name, elementclass)

                    #End of sequence
                    lib2_bausteine.a_sequence_end(xaml)

                    
                #insert, Send Hotkey Ctrl+V

                elif u_eventtype == "CTRL + V":
                
                    #Start of sequence
                    lib2_bausteine.a_sequence_send_hotkey_Strg_V_start(xaml, u_name)

                    #Module variant 1
                    lib2_bausteine.a_send_hotkey_strg_v_browser_no_id(xaml, a_applicationname,url, u_name)

                    #VModul variant 2
                    lib2_bausteine.a_send_hotkey_strg_v_browser_no_id_var2(xaml, a_applicationname,url, u_name)

                    #Sequence end
                    lib2_bausteine.a_sequence_end(xaml) 
                           
                #Click Enter 
            elif u_eventtype == "ENTER":
                lib2_bausteine.a_press_enter(xaml)
               
    #Application name explorer. Use of UIA selectors, no query for types necessary since role attribute matches log data an be integrated into the selector.
    elif a_applicationname=="explorer": 


        #Test datepicker
        if any (x in check_upper_lower for x in test_datepicker):
            lib_bausteine.a_comment_calendar_picker(xaml)
  
        
        if u_type == "Bearbeiten" or u_type=="Suchfeld" or u_type=="Telefonnummer": 
            
            if u_eventtype == "BTN_LEFT" or u_eventtype=="BTN_RIGHT": #then it is a text input
                #using uia selctor 
                lib2_bausteine.a_type_into_explorer(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type, input_variables)

               
            elif u_eventtype=="CTRL + ALT + ALTGR + Q":
                lib2_bausteine.a_type_into_explorer(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type, input_variables)
                
            elif u_eventtype == "CTRL + C":
                #ID, name und role, uia Selektor
                lib2_bausteine.a_send_hotkey_strg_c_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                  
            elif u_eventtype == "CTRL + V":
                #ID, name und role, uia Selektor
                lib2_bausteine.a_send_hotkey_strg_v_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, automationid, u_type)
                 
            elif u_eventtype == "ENTER":
                lib2_bausteine.a_press_enter(xaml)    
            
                
        else: #then always click activity
                    
            if u_eventtype=="BTN_LEFT":
                #Left click, attributes Name and Role
                lib2_bausteine.a_click_left_in_explorer(xaml, a_applicationname, a_windowtitle,u_name, u_type)
                  
            else: #Right click, Name and Role
                lib2_bausteine.a_click_right_in_explorer(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                    
                 
    else: #then it is an application, separate blocks. Since here the role corresponds with the log data, this can be integrated directly into the selector
 
        #Test Datepicker,
        
        if any (x in check_upper_lower for x in test_datepicker):
            lib_bausteine.a_comment_calendar_picker(xaml)


        #does the element have an id?
        if len(automationid)>0:
            if u_type == "Bearbeiten" or u_type=="Suchfeld" or u_type=="Telefonnummer":

                if u_eventtype == "BTN_LEFT" or u_eventtype=="BTN_RIGHT":
                    #Type Into automationid, name und role
                    lib2_bausteine.a_type_into_application(xaml, a_applicationname, a_windowtitle, automationid,  u_name, u_type, input_variables)
                                
               
                elif u_eventtype=="CTRL + ALT + ALTGR + Q":
                    lib2_bausteine.a_type_into_application(xaml, a_applicationname, a_windowtitle, automationid,  u_name, u_type, input_variables)

                elif u_eventtype == "CTRL + C":
                    #automationid und role
                    lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid,u_name, u_type)
                        
                elif u_eventtype == "CTRL + V":  
                    #automationid und role
                    lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid,u_name, u_type) 
                       
                elif u_eventtype == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)  

            #type=Element occurs in excel tables
            if u_type=="Element":
                    
                if u_eventtype=="BTN_LEFT" or u_eventtype=="BTN_RIGHT":
                    #Write in Excel Cell
                   lib2_bausteine.a_write_cell(xaml, u_name, input_variables)
                                
                elif u_eventtype=="CTRL + C":
                    #automationid und role
                    lib2_bausteine.a_send_hotkey_strg_c_in_application(xaml, a_applicationname, a_windowtitle, automationid,u_name, u_type)
                        
                elif u_eventtype=="CTRL + V":
                    #automationid und role
                    lib2_bausteine.a_send_hotkey_strg_v_in_application(xaml, a_applicationname, a_windowtitle, automationid,u_name, u_type)
                                       
                elif u_eventtype == "ENTER":
                    lib2_bausteine.a_press_enter(xaml) 
                        
                                 
                
            #to cover all click activities
            else:
                        
                if u_eventtype == "BTN_LEFT":
           
                    #über automationid, name und role
                    lib2_bausteine.a_click_left_in_application (xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)

                else: 
                    lib2_bausteine.a_click_right_in_application(xaml, a_applicationname, a_windowtitle, automationid, u_name, u_type)
            
        #then there is no ID, same queries as in the if block, but using different attributes for the selectors          
        else: 
            if u_type=="Element":
                    
                if u_eventtype=="BTN_LEFT" or u_eventtype=="BTN_RIGHT":
                    pass 
                                
                elif u_eventtype=="CTRL + C":
                    lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                    
                             
                elif u_eventtype=="CTRL + V":
                    lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                        
                elif u_eventtype == "ENTER":
                    lib2_bausteine.a_press_enter(xaml)    
                       
                    
            elif u_type=="Bearbeiten" or u_type=="Suchfeld" or u_type=="Telefonnummer":
                    
                if u_eventtype=="BTN_LEFT" or u_eventtype=="BTN_RIGHT":
                    lib2_bausteine.a_type_into_application(xaml,a_applicationname, a_windowtitle,u_name,u_type, input_variables)
                                
                elif u_eventtype=="CTRL + C":
                    lib2_bausteine.a_send_hotkey_strg_c_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                                       
                elif u_eventtype=="CTRL + V":
                    lib2_bausteine.a_send_hotkey_strg_v_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
                     
                elif u_eventtype == "ENTER":
                    lib2_bausteine.a_press_enter(xaml) 
                    
            #to cover all click activities
            else: 
                if u_eventtype == "BTN_LEFT":
                    lib2_bausteine.a_click_left_in_application_no_id(xaml,a_applicationname, a_windowtitle, u_name, u_type)
                else:
                    lib2_bausteine.a_click_right_in_application_no_id(xaml, a_applicationname, a_windowtitle, u_name, u_type)
 
                    
            
def verbesserungsvorschlaege(xaml, dbname, dataScraping):

    #Suggestions for improvement at the end
    l_database = sqlite3.connect(dbname)
    #two cursors are required 
    cursor = l_database.cursor()
    cursor2= l_database.cursor()

    #Count how many times something was copied or inserted from/in Excel during the process using shortcut combination CTRL+C to detect corresponding action
    strg_c_excel= cursor.execute("SELECT COUNT (*) FROM logger where a_applicationname='excel' and u_eventtype='CTRL + C'")
    strg_v_excel= cursor2.execute("SELECT COUNT (*) FROM logger where a_applicationname='excel' and u_eventtype='CTRL + V'")
    
    #Capture all results that meet the SQL statement 
    number_of_strg_c_excel= strg_c_excel.fetchone()[0]
    number_of_strg_v_excel=strg_v_excel.fetchone()[0]
    
    #Start of the suggestions for improvement: These are commented out in order not to interrupt the general flow 
    lib2_bausteine.a_sequence_comment_out(xaml)

    #Check for number of shortcut combinations in Excel to suggest intelligent activity module and insert comment with note
    if number_of_strg_c_excel>=3:

        #Sequence around proposal
        lib2_bausteine.a_sequence_read_range_start(xaml)

        #Insert comment
        lib2_bausteine.a_comment_read_range (xaml)
        
        #Insertion of the intelligent block read range, which needs to be manually post-processed
        lib2_bausteine.a_read_range(xaml)

        #End of sequence
        lib2_bausteine.a_sequence_end(xaml)

    #Check for number of shortcut combinations in Excel to suggest intelligent activity module and insert comment with note
    if number_of_strg_v_excel>=3:

        #Sequence around proposal
        lib2_bausteine.a_sequence_write_range_start(xaml)

        #Insert comment
        lib2_bausteine.a_comment_write_range(xaml)
        
        #Insertion of the intelligent block read range, which needs to be manually post-processed
        lib2_bausteine.a_write_range_excel (xaml)
 
        #End of sequence
        lib2_bausteine.a_sequence_end(xaml)

          

    # when user selects in frontend that he wants to do data scraping. Return values are Yes or No. Data scraping using the Data Scraping Wizard must be performed directly within UiPath
     
    if dataScraping=="Yes":

        #Start of sequence
        lib2_bausteine.a_sequence_data_scraping_start(xaml)

        #DaInserting a comment that gives hints on the necessary steps to be taken to do Data Scraping and connection activity to write extracted data from data scraping
        lib2_bausteine.a_comment_data_scraping (xaml)
        lib2_bausteine.a_write_range_excel (xaml)

        #End of sequence block
        lib2_bausteine.a_sequence_end(xaml)
    
    #End of the commented out block
    lib2_bausteine.a_sequence_comment_out_end(xaml) 
    cursor.close()
    cursor2.close()



if __name__ == '__main__':
    main(sys.argv[1]) 