import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#checkbox example
# wait = WebDriverWait(driver, 10)
# type_to_select_element = wait.until(EC.visibility_of_element_located((By.ID, "autosuggest"),))
# type_to_select_element.send_keys('ind')
# time.sleep(2)

print(driver.find_element(By.ID, "checkBoxOption1").get_attribute("value"))  #== "option1"
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#radiobuttons = driver.find_elements(By.XPATH, "///input[@name='radioButton']")
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
hide_button = driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
show_button = driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

#handling javascript alerts
name = 'Jason'
#text_box_name = driver.find_element(By.XPATH, "//input[@id='name']").send_keys("oleg")
text_box_name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
alert_button = driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
#alert_button = driver.find_element(By.ID, "alertbtn")
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()
confirm_button = driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
confirm = driver.switch_to.alert
alert.dismiss()