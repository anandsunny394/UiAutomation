import time

import pytest
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(10)

