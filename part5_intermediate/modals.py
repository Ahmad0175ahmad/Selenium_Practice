from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice-automation.com/modals/")
print("url opened")

# WAIT for page JS to load
time.sleep(3)

# Click Simple Modal
driver.find_element(By.ID, "simpleModal").click()

# WAIT for modal animation to finish
time.sleep(2)

# Get modal title
modal_title = driver.find_element(By.ID, "pum_popup_title_1318").text
print("Simple Modal title :", modal_title)

# Get modal content (IMPORTANT FIX)
modal_text = driver.find_element(
    By.XPATH, "(//div[@class='pum-content popmake-content'])[1]").text

print("Simple Modal text :", modal_text)
time.sleep(2)
btn=driver.find_element(By.XPATH , "(//button[@class='pum-close popmake-close'])[1]")
btn.click()
time.sleep(3)
driver.quit()
