from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(2)
parent_window_id = driver.current_window_handle
print("Parent Window id :", parent_window_id)

driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)
list_window_ids = driver.window_handles
print("List of windows : ", list_window_ids)


for window_id in list_window_ids:
    if window_id!=parent_window_id:
        driver.switch_to.window(window_id)
        print("Switched to child window with ID:",window_id)


expected_title ="New Window"
if driver.title== expected_title:
    print("Switched to the correct Window")
else:
    print("This is not the expected window") 


expected_url ="https://the-internet.herokuapp.com/windows/new"      
if driver.current_url==expected_url:
    print("switched to the current window") 
else:
    print("This is not the expected window")
time.sleep(2)
driver.quit()