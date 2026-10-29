from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import CheckoutConfirmationPage
from utilities.browserUtilities import BrowserUtilities


class ShopPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_to_card = (By.XPATH, "//div[@class='card h-100']")
        #self.checkout_button = (
            #By.XPATH,"//a[contains(@class, 'btn-primary') and contains(., 'Checkout')]",)
        self.checkout_button = (By.CSS_SELECTOR, "a.nav-link.btn-primary")

    def add_product_to_cart(self, product_name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.shop_link)).click()
        phones = self.driver.find_elements(*self.product_to_card)
        for i in phones:
            phoneName = i.find_element(By.XPATH, "./div/h4/a").text
            if phoneName == product_name:
                i.find_element(By.XPATH, ".//button").click()  # div/button
                break

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.checkout_button))
        button.click()
        checkout_confirmation = CheckoutConfirmationPage(self.driver)
        return checkout_confirmation
