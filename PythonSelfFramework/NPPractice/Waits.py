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
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(5)
elements=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for i in elements:
    i.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()


print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

total_amount=driver.find_element(By.CSS_SELECTOR,".totAmt").text
after_discount_total=driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print(total_amount)
print(after_discount_total)

#to verify
assert total_amount == after_discount_total
time.sleep(10)









