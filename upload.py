import openpyxl
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def update_excel_data(downloaded_file_path, searchTerm, colName, new_value):
    book = openpyxl.load_workbook(downloaded_file_path)
    sheet = book.active
    dict = {}
    for i in range(1, sheet.max_row +1): #to get rows
        if sheet.cell(row=1, column=i).value == colName:  #before colName it was iterating through column until name= price
            dict['col'] = i
            break
    for i in range(1, sheet.max_row + 1): #i it's rows
        for j in range(1, sheet.max_column + 1): #j it's columns for iterating through columns
            if sheet.cell(row=i, column=j).value == searchTerm: #before searchTerm it was iterating through rows until Apple
                dict['row'] = i
                break
    print("Found positions:", dict)
    sheet.cell(row=dict['row'], column=dict['col']).value = new_value #before new_value here was 500
    book.save(downloaded_file_path)

downloaded_file_path ="C:\\Users\\HP\\Downloads\\download.xlsx"
fruit_name = 'Apple'
newValue = '999'
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
download_button = wait.until(EC.visibility_of_element_located((By.ID, "downloadButton")))
download_button.click()

#edit excel with updated value through func update_excel_data()
update_excel_data(downloaded_file_path, fruit_name,"price", newValue)
#upload file back to url
file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type = 'file']")))
file_input.send_keys(downloaded_file_path)
message_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
msg = wait.until(EC.visibility_of_element_located(message_locator))
print("Upload confirmed:", msg.text)

#print(driver.find_element(By.XPATH, "//div[@class = 'Toastify__toast-body']/div[2]").text)
#print(driver.find_element(*message_locator).text)
price_column_locator = driver.find_element(By.XPATH,"//div[text() ='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH, f"//div[text() ='{fruit_name}']/parent::div/parent::div/div[@id ='cell-{price_column_locator}-undefined']").text
assert actual_price == newValue
driver.quit()