import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlopen
import numpy as np

class HTMLExtraction():

    def getVariables(self):
        chrome_options.add_argument("--headless")
        PATH="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(PATH)

        driver.get("http://132.187.226.138:8080/webapp/view/common/login.page")
        loginurl="http://132.187.226.138:8080/webapp/view/groupware/task/taskDetail.page?entityId=9407"

        username="rpa.team22@gmail.com"
        password="RPA2022#"

        driver.find_element("name", "loginForm:username").send_keys(username)
        driver.find_element("name", "loginForm:password").send_keys(password)
        driver.find_element("name", "loginForm:remember").click()
        driver.find_element("id", "loginForm:loginButton").click()
        time.sleep(2)
        driver.get(loginurl)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, features="html.parser")

        #hh=soup.find_all("div", {"id": "pageForm:taskDescriptionXRow"})
        hh=soup.find("textarea", {"id": "pageForm:taskDescriptionX_TA"})
        #for e in hh.findAll('br'):
            #e.extract()

        
        hh=hh.text

        #print("hh" + str(hh))
        hh=hh.replace('<br>','\n')
        hh=hh.replace('<p>','\n')

        #print(hh)

        import re
        txt = hh

        #print("Txt" + txt)

        value = re.findall("\:(.*)",txt)
        variableName = re.findall("(.*):",txt)
        

        combined = np.column_stack((variableName, value))

        print(combined[0][0])

        #Ersteller=(x[0])
        #Ankunftszeit=(x[1])
        #Zielort=(x[2])
        #Adresse des Hotels=(x[3])
        #Ausland=(x[4])
        #Enddatum=(x[5])
        #Uhrzeit=(x[6])
        

        return (combined)







