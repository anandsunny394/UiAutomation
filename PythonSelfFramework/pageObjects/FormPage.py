from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self,driver):
        self.driver=driver


    name=(By.XPATH,"//input[@name='name']")

    def formElement(self):

        return self.driver.find_element(*FormPage.name)
