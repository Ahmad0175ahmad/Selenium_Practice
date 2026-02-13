from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
message = driver.find_element(By.TAG_NAME ,"p").text
print(message)
driver.quit()