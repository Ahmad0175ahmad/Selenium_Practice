from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
print("Browser opended")
driver.maximize_window()
print("Browser Maximized")
driver.get("https://practice.expandtesting.com/")

time.sleep(2)
#link=driver.find_element(By.LINK_TEXT, "Test Login Page")
link=driver.find_element(By.PARTIAL_LINK_TEXT,"Test Login")
driver.execute_script("arguments[0].scrollIntoView(true);",link)

time.sleep(2)
link.click()
print("Login Page Open")
time.sleep(2)
driver.quit()