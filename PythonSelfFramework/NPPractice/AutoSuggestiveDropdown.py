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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("Ind")
# driver.find_element(By.XPATH,"//a[normalize-space(text()) = 'India']").click() #selecting element by text

#selecting dynamic dropdown through iteration
dropdown_elements=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for i in dropdown_elements:
    if i.text == "India":
        i.click()

#get text will only work if text for any element is present on refreshing
#To get the dynamically text entered(example "India")we can use get_attribute("value")
selected_country=driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(selected_country)
assert selected_country == "India"







driver.find_element(By.ID,"ctl00_mainContent_ddl_originStation1_CTXT").send_keys("A")
origin_city=driver.find_elements(By.XPATH,"//li[@class='livecl']")
for i in origin_city:
    if i.text == "Goa (GOI)":
        i.click()
        break


# driver.find_element(By.XPATH,"ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys("B")


