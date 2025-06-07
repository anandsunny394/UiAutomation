import pytest
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Handling Java "Alerts" and "Confirm" box

#Alerts
driver.find_element(By.XPATH,"//input[@value='Alert']").click()
time.sleep(5)

#switching to alert mode
alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)

assert "Hello" in alert_text
alert.accept()



#confirm
driver.find_element(By.ID,"confirmbtn").click()
time.sleep(5)

#switching to confirm alert
confirm=driver.switch_to.alert

confirm.accept()  #accept
# confirm.dismiss() #cancel


time.sleep(5)
