import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from array import array
chrome_options=Options()
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlopen
import numpy as np
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class HTMLExtraction():

    #the provided parameter task corresponds to the input of the task via the frontend.
    def getVariables(self, task):
        try:

            #Connect to chrimedriver to extract the variables from the task template.
            chrome_options.add_argument("--headless")
            PATH="C:\Program Files (x86)\chromedriver.exe"
            driver=webdriver.Chrome(PATH)
        

            driver.get("http://132.187.226.138:8080/webapp/view/common/login.page")
            loginurl="http://132.187.226.138:8080/webapp/view/settings/organizer/organizerSettings.page?mid=261"


            #login data
            username="rpa.team22@gmail.com"
            password="RPA2022#"


            #login to weclapp
            driver.find_element("name", "loginForm:username").send_keys(username)
            driver.find_element("name", "loginForm:password").send_keys(password)
            driver.find_element("name", "loginForm:remember").click()
            driver.find_element("id", "loginForm:loginButton").click()

            #time sleep to allow for delays caused by the bot.
            time.sleep(2)

            #Navigate to the organiser settings to select the correct task template. 
            driver.get(loginurl)
            time.sleep(1)

            #takes first task that is displayed, new tasks are arranged on top
            driver.find_element("name", "pageForm:editTaskTemplateOrganizationList").click()
            time.sleep(7)
        

            #find the task template that matches the delivered value for task from the frontend. 
            source=driver.find_element(By.XPATH, "//div[contains(text(), '{0}')]".format(task))

            time.sleep(7)
            action = ActionChains(driver)

            action.double_click(on_element=source)
            action.perform()
            time.sleep(4)

            #Extract the elements from the page source text via the Beautiful Soup package. 
            soup = BeautifulSoup(driver.page_source, features="html.parser")


            #find textarea of the task template with the additionally specified variables from the page source text. 
            hh=soup.find("textarea", {"id": "idTaskTemplateMPForm:taskDescriptionX_TA"})
        



            hh=hh.text
            txt = hh

            #Extraction of all table cells (<td> tags) to be able to read out the entries in the task template table.
            inputWeclapp = re.findall("<\s*td\s*[^>]*>(.*?)<\s*\/\s*td>",txt)

            a = 1

            value = []
            variableName = []


            #Store all even values of a (corresponding to the second column) in value and the odd values of a (corresponding to the first column) in variableName.
            for i in inputWeclapp:
                i = i.replace("&nbsp;","")
                if a % 2 == 0:
                    value.append(i)
                else:
                    variableName.append(i)
                a = a+1
        
            combined = np.column_stack((variableName, value))





            return (combined,variableName, value)

        except:
            print("The Chromedriver is not working correctly. Check the following points and try again: Do you have the Chrome browser installed? Have you installed Chromedriver and placed the .exe file in the following folder C:\Program Files (x86)\chromedriver.exe? Is your VPN connection set up? Have you created the right task template in WeClapp and specified the variables in table form? Did you enter the correct name of the task template in the frontend? If these hints have been taken into account, increase the time.sleep")

