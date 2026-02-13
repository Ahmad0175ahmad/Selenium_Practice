from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/myfolders/PYTHON%20CODING/Selenium1/iframePracticeSite/nested-frame.html")
time.sleep(2)
driver.switch_to.frame("parentFrame")
driver.switch_to.frame("childFrame")

text = driver.find_element(By.ID, "childText")
print("Child Frame Task ", text.text)
time.sleep(2)
driver.switch_to.default_content()

maintext = driver.find_element(By.TAG_NAME, 'h1')
print("Main Text :", maintext.text)
driver.quit()