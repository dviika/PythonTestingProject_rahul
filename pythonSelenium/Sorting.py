from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

#the goal in click on table column header sort and check whether veg get sorted as per alphabetical order

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
#collect all veggie names into the list -> browser sorted list a, b, c
veggies = driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
browser_veggies_list = []
for item in veggies:
    browser_veggies_list.append(item.text)
print(browser_veggies_list)
originalBrowserSortedList = browser_veggies_list
#sort this list it's going to modify existed list
browser_veggies_list.sort()
print(browser_veggies_list)
#veggieList == newSortedList
assert browser_veggies_list == originalBrowserSortedList
