from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

time.sleep(3)

multiselect =Select(driver.find_element(By.ID , "multiSelect"))
if multiselect.is_multiple:
    print("dropdown is multi select")
else:
    print("dropdown is not multi select")    
multiselect.select_by_visible_text("Volvo")
multiselect.select_by_visible_text("Saab")

time.sleep(3)
multiselect.deselect_by_visible_text("Volvo")

# select all options
# selected_options = multiselect.all_selected_options
# for option in selected_options:
#     print("Selected : ", option.text)

alloptions = multiselect.options
for option in alloptions:
    print(option.text)

driver.quit()

