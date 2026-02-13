from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("D:/myfolders/PYTHON CODING/Selenium1/iframePracticeSite/index.html")
time.sleep(3)
driver.switch_to.frame("leftFrame")

driver.find_element(By.NAME ,'name').send_keys("Ahmad")
time.sleep(2)
driver.find_element(By.NAME, 'email').send_keys("ahmad@gmail.com")
driver.switch_to.default_content()
time.sleep(2)

driver.quit()