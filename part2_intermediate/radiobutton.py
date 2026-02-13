from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

time.sleep(3)
bmw_radio =driver.find_element(By.ID , "radio2")
bmw_radio.click()

time.sleep(2)
tesla_radio = driver.find_element(By.ID , 'radio4')
tesla_radio.click()
time.sleep(2)
driver.quit()