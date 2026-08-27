import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_object = Service("D:/Study_PY/chrome_driver2026/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service = service_object)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)


