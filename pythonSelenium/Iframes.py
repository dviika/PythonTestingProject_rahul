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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
iframe_body = driver.find_element(By.ID, "tinymce")
iframe_body.send_keys(Keys.CONTROL + "a") #select all
iframe_body.send_keys(Keys.DELETE) #Delete
iframe_body.send_keys("I just have just entered a text into iframe")
driver.switch_to.default_content()
header = driver.find_element(By.CSS_SELECTOR, "h3").text
assert header == "An iFrame containing the TinyMCE WYSIWYG Editor"