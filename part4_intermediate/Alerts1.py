from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/V4/index.php")
time.sleep(2)
login_btn = driver.find_element(By.NAME , "btnLogin")
login_btn.click()

time.sleep(2)
alert1 = driver.switch_to.alert
print("Alert text : ", alert1.text)

alert1.accept()

driver.quit()

