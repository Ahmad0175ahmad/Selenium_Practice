from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("D:/myfolders/PYTHON CODING/Selenium1/iframePracticeSite/index.html")
time.sleep(2)

framepath =driver.find_element(By.XPATH, '//iframe[@name="bottomFrame"]')
driver.switch_to.frame(framepath)

text = driver.find_element(By.TAG_NAME, "p")
print("Text from bottom frame : ", text.text)
