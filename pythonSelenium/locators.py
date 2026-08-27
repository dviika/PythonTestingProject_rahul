import time

import driver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Rahul")
# CSS selector -> tagname[attribute = ' value'] ->>> input[name ="name"] or #id or .classname
#driver.find_element(By.CSS_SELECTOR, "input[name ='name']").send_keys("Roman")
driver.find_element(By.NAME, "email").send_keys("RahulShetty@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID, "exampleCheck1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)  #Male will be selected
dropdown.select_by_value("teacher") #only if there is a value atrubute spefified



driver.find_element(By.ID, "inlineRadio2").click()

driver.find_element(By.NAME, "bday").send_keys("02/15/2023")
# Xpath -> //tagname[@attribute = ' value'] ->>> //input[@type='submit]
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
#assert message == "Success! The Form has been submitted successfully!."
assert "Success!" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.close()
