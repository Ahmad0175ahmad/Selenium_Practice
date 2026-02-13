from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

time.sleep(3)

dropdown = Select(driver.find_element(By.ID, "carBrands")) 

if dropdown.is_multiple:
    print("This dropdown is multiselect")
else:
    print("This dropdown is single-select")    

dropdown.select_by_visible_text("Mercedes")
print("Selected Option : ", dropdown.first_selected_option.text)

time.sleep(2)

dropdown.select_by_value("audi")
print("Selected Option : " , dropdown.first_selected_option.text)
time.sleep(2)

dropdown.select_by_index(1)
print("Selected option : ", dropdown.first_selected_option.text)
driver.quit()