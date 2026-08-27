import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
wait = WebDriverWait(driver, 10)
link_to_shop_locator = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='shop']"))).click()
#(By.XPATH, "//a[contains(@href, 'shop')]"))
phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for i in phones:
    phoneName = i.find_element(By.XPATH, "./div/h4/a").text
    if phoneName == 'Blackberry':
        i.find_element(By.XPATH, ".//button").click() #div/button
        break

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class*='validate filter-input form-control']")))
input_field.send_keys("Ind")
input_field.click()
link_to_the_country = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
link_to_the_country.click()
#checkbox = wait.until(EC.element_to_be_clickable((By.ID, 'checkbox2')))
checkbox_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'checkbox checkbox-primary']")))
checkbox_label.click()
driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']").click()
purchase_complete_msg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in purchase_complete_msg
driver.quit()

