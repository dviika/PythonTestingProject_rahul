from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.browserUtilities import BrowserUtilities


class CheckoutConfirmationPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        #self.checkout_button = (By.CSS_SELECTOR, "a.nav-link.btn-primary")
        self.country_input_field = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']")


    def checkout(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
       self.driver.find_element(*self.country_input_field).send_keys(countryName)
       wait = WebDriverWait(self.driver, 10)
       wait.until(EC.presence_of_element_located(self.country_option))
       self.driver.find_element(*self.country_option).click()
       self.driver.find_element(*self.checkbox).click()
       self.driver.find_element(*self.submit_button).click()


    def get_confirmation_message(self):
        success_message = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_message