import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
wait = WebDriverWait(driver, 10)
type_to_select_element = wait.until(EC.visibility_of_element_located((By.ID, "autosuggest"),))
type_to_select_element.send_keys('ind')
time.sleep(2)

search_results = driver.find_elements(By.CSS_SELECTOR, "li[class ='ui-menu-item'] a")
print(len(search_results))

for item in search_results:
    if item.text == "India"
        item.click()
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
