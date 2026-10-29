from selenium.webdriver.common.by import By
from pageObjects.shopPage import ShopPage
from utilities.browserUtilities import BrowserUtilities


class LoginPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.NAME, "password")
        self.sign_in_field = (By.ID, "signInBtn")




    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username) #unpac tuple into 2 separate arg Id and useename
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.sign_in_field).click()
        shop_page = ShopPage(self.driver)
        return shop_page


