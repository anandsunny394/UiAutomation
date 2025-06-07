from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    deliveryLocation=(By.ID,"country")

    def location_function(self):
        return self.driver.find_element(*CheckOutPage.deliveryLocation)





