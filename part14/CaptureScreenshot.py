from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

folder_path =r"D:\myfolders\PYTHON CODING\Selenium1\part14\Screenshots"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)



full_page_path =folder_path + "\\fullpage1.png"
#driver.save_screenshot(full_page_path)
driver.get_screenshot_as_file(full_page_path)
print("Full page screenshot saved at :", full_page_path)


element = driver.find_element(By.ID,"login-button")
element_path=folder_path + "\\login_button.png"
element.screenshot(element_path)
print("Element screenshot saved at : ",element_path )
driver.quit()