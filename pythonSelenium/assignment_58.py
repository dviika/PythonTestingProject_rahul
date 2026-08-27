import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

#the goal is to click on link, go to tab 1 gran email address. go back to tab 0, enter username as grabbed email,
# enter pass, click sign in, take error message text and do assert
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Wait up to 10 seconds for the blinking link to appear and become clickable
wait = WebDriverWait(driver, 10)
blinking_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material")))
#"https://rahulshettyacademy.com/documents-request")))
blinking_link.click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])

sentence_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.im-para.red strong")))
sentence = sentence_element.text
print(sentence)
driver.switch_to.window(windows_opened[0])
username = wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("sentence")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "signInBtn").click()
error_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger")))
error_text = error_locator.get_attribute("textContent").strip()
print("Selenium grabbed:", repr(error_text))
#assert "Incorrect username/password" in error_text
assert error_text == "Incorrect username/password."


