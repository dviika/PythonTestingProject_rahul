from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#the goal in click on table column header sort and check whether veg get sorted as per alphabetical order

# 1. Initialize the Chrome options object
chrome_options = Options()
# 2. Add your desired configurations
chrome_options.add_argument("--headless")  # Example: Run without opening a GUI window
chrome_options.add_argument("--start-maximized")
# 3. PASS THE OPTIONS OBJECT HERE
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()



