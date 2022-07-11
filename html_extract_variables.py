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

chrome_options.add_argument("--headless")
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("http://132.187.226.138:8080/webapp/view/common/login.page")
loginurl="http://132.187.226.138:8080/webapp/view/groupware/task/taskDetail.page?entityId=5213"

username="rpa.team22@gmail.com"
password="RPA2022#"

driver.find_element("name", "loginForm:username").send_keys(username)
driver.find_element("name", "loginForm:password").send_keys(password)
driver.find_element("name", "loginForm:remember").click()
driver.find_element("id", "loginForm:loginButton").click()
time.sleep(2)
driver.get(loginurl)
time.sleep(4)

soup = BeautifulSoup(driver.page_source, "html.parser")

finden=soup.find("div", {"id": "pageForm:taskDescriptionXRow"})
inside= soup.find_all("border-bottom:1px")


print(finden)