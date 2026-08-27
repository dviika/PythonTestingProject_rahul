import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

#the goal in to enter ber (3 product will appear and add them all to the card) add discount code,
# calculate total amount for all 3 items without discount, verify that discount was aplied
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
parent_tab_text = driver.find_element(By.TAG_NAME, "h3").text
print(parent_tab_text)
assert "Opening a new window" == parent_tab_text
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
