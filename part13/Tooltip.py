from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver= webdriver.Chrome()

driver.maximize_window()
driver.get("https://practice.expandtesting.com/tooltips")
time.sleep(3)

button1=driver.find_element(By.ID,"btn1")
action =ActionChains(driver)
action.move_to_element(button1).perform()

time.sleep(2)

tooltip_text = button1.get_attribute("title")
print(tooltip_text)
driver.quit()