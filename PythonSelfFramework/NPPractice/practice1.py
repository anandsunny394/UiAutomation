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
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.current_url)
print(driver.title)


driver.find_element(By.NAME,"name").send_keys("This is Testing")
email_box=driver.find_element(By.XPATH,"//input[@name='email']").is_displayed()
print(email_box)


#Static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female") #first will select female
dropdown.select_by_index(0)  #then will select male
time.sleep(10)






element=driver.find_element(By.XPATH,"(//h4[normalize-space()='Two-way Data Binding example:'])[1]").text
print(element)

assert ("Data" in element)





















driver.close()