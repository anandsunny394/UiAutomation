import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
expected_list=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

products=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
list_b=[]
for i in products:
    list_b.append(i.text)
print(list_b)

assert expected_list == list_b


products_1=driver.find_elements(By.XPATH,"//div[@class='products']/div/div/button")
for item in products_1:
    item.click()

driver.find_element(By.XPATH,"//a/img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

tables=driver.find_elements(By.XPATH,"//td[5]/p")
for i in tables:
    print(i.text)

