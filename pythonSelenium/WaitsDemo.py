import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

#the goal in to enter ber (3 product will appear and add them all to the card) add discount code,
# calculate total amount for all 3 items without discount, verify that discount was aplied
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(6)
# 5 sec is maximum of wait, if it happens earlier it will be done earlier
#search_field = driver.find_element(By.XPATH, "//input[@type='search']").send_keys(name)
search_field = driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
#wait = WebDriverWait(driver, 10)
product_result = driver.find_elements(By.XPATH, "//div[@class ='products']/div")
print(len(product_result))
count = len(product_result)
assert count == 3 #should be 3 items
for item in product_result:
    item.find_element(By.XPATH, "div/button").click()

card = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#time.sleep(2)
proceed_to_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

promo_code =driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
apply_button =driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Explicit wait - It is used to wait explicitly based on the given time for a particular element
#presence_of_element_located
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
#code = driver.find_element(By.CLASS_NAME, ".promoInfo").text
#print(code)

