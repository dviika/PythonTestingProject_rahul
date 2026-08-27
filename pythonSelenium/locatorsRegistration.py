import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@@@123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@@@123")
#driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()

driver.quit()
