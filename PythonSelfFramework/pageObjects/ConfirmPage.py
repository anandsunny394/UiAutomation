from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    cart=(By.XPATH,"//div[@class='card h-100']")
    navigateCheckout=(By.XPATH, "//div/ul/li/a[@class='nav-link btn btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")



    def cartItems(self):
        return self.driver.find_elements(*ConfirmPage.cart)

    def navigate_Checkout(self):
        return self.driver.find_element(*ConfirmPage.navigateCheckout)

    def checkOutButton(self):
        return self.driver.find_element(*ConfirmPage.checkOut)




