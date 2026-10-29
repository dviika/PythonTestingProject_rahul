import json
import os.path
import sys

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#test_data_path = '../data/test_e2eTestFramework.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

# CORRECTED: Dynamically builds the absolute path to your JSON file
test_data_path = os.path.join(script_dir, '..', 'data', 'test_e2eTestFramework.json')

with open (test_data_path, 'r') as f:
    test_data = json.load(f)
    test_list = test_data['data']
from pageObjects.login import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize("test_data", test_list)
def test_e2eT(browser_instance, test_data):
    driver = browser_instance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    print(login_page.getTitle())
    shop_page = login_page.login(test_data['userEmail'], test_data['userPassword'])
    shop_page.add_product_to_cart(test_data['productName'])
    print(shop_page.getTitle())
    checkout_confirmation_page = shop_page.proceed_to_checkout()
    checkout_confirmation_page.checkout()
    checkout_confirmation_page.enter_delivery_address("ind")
    checkout_confirmation_page.get_confirmation_message()


