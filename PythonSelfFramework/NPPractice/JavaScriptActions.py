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




#scrolling window
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#window.scrollBy(0,700) can we used to scroll to down of the page

#Taking screenshot
driver.get_screenshot_as_file("Screenshot1.png")

time.sleep(5)