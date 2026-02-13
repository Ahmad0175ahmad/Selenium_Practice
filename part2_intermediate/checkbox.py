from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

time.sleep(3)
print("Title : ",driver.title)
print("URL : ", driver.current_url)

# ford_checkbox=driver.find_element(By.ID, "option1")
# if not ford_checkbox.is_selected():
#     ford_checkbox.click()
# bmw_checkbox=driver.find_element(By.ID, "option2")
# if not bmw_checkbox.is_selected():
#     bmw_checkbox.click()
# time.sleep(3)
# print(ford_checkbox.is_selected())
# print(bmw_checkbox.is_selected())


checkboxes = driver.find_elements(By.XPATH , "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
driver.quit()

