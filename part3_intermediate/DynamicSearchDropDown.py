from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://google.com")

time.sleep(2)
searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
time.sleep(2)

suggestions = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")
for suggestion in suggestions:
    print(suggestion.text)
driver.quit()