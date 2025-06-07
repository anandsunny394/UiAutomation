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


#Handling Checkboxes
check_boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for i in check_boxes:
    if i.get_attribute("value") == "option1":  #can also get by value=option1
        i.click()
        print(i.is_selected())  #to check if checkbox is selected
    elif i.get_attribute("name") == "checkBoxOption2": #can also select by name=attribute
        i.click()
time.sleep(5)


#Handling is_displayed
display=driver.find_element(By.ID,"displayed-text").is_displayed()
print(display)


#Handling Java "Alerts" and "Confirm" box
#Alerts
driver.find_element(By.XPATH,"//input[@value='Alert']").click()

driver.execute_script()
time.sleep(5)



