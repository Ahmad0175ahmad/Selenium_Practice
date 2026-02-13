from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("D:/myfolders/PYTHON CODING/Selenium1/iframePracticeSite/index.html")
time.sleep(2)
driver.switch_to.frame(1)
button=driver.find_element(By.TAG_NAME,'button')
button.click()

time.sleep(2)

alert = driver.switch_to.alert
print("Alert text : ",alert.text)
alert.accept()
time.sleep(2)
dropdown =Select(driver.find_element(By.ID, "options"))
dropdown.select_by_visible_text("Option Two")
time.sleep(2)
driver.switch_to.default_content()
driver.quit()
