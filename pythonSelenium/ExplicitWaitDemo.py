import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

#the goal in to enter ber (3 product will appear and add them all to the card) add discount code,
# calculate total amount for all 3 items without discount, verify that discount was aplied
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.implicitly_wait(5)
#wait = WebDriverWait(driver, 10)
# 5 sec is maximum of wait, if it happens earlier it will be done earlier
#search_field = driver.find_element(By.XPATH, "//input[@type='search']").send_keys('ber')
search_field = driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
product_result = driver.find_elements(By.XPATH, "//div[@class ='products']/div")
products_text= driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
print(products_text)
expected_list = ['Cucumber','Raspberry','Strawberry']
search_result_ber_actual_list = []
for item in products_text:
    search_result_ber_actual_list.append(item.text.split(' - ')[0])
print(search_result_ber_actual_list)
assert search_result_ber_actual_list == expected_list
print(len(product_result))
count = len(product_result)
assert count == 3

for item in product_result:
    logging.info(item.text)
    item.find_element(By.XPATH, "div/button").click()
card = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)
proceed_to_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#Sum validation total price
#total_price = driver.find_elements(By.XPATH, "//tr/td[5]/p")  tr td:nth-child(5) p
total_price = driver.find_elements(By.CSS_SELECTOR, " tr td:nth-child(5) p")
sum = 0
for price in total_price:
    sum = sum + int(price.text)
print(sum)

time.sleep(2)
total_price = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(total_price)
assert sum == total_price
promo = driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")

apply_button = driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Explicit wait - It is used to wait explicitly based on the given time for a particular element
#presence_of_element_located
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
discount_percent = (driver.find_element(By.XPATH, "//span[@class='discountPerc']").text)
print(discount_percent)
discount_percent = float(discount_percent.replace('%', '')) / 100
total_after_discount = (driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
total_after_discount = float(total_after_discount.replace('%', '')) / 100
dicount_amount = total_price * discount_percent/100
print(dicount_amount)
price_after_discount = total_price - dicount_amount
assert price_after_discount == total_price - dicount_amount
#code = driver.find_element(By.CLASS_NAME, ".promoInfo").text
#print(code)
#We need to check Total Price and Total After discount
driver.quit()