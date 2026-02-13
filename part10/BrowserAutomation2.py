from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(6)

parent_window_id =driver.current_window_handle
print("Parent window id : ",parent_window_id)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(5)
parent_window_id=driver.current_window_handle
# switch to child window id
list_window_ids =driver.window_handles
for window_id in list_window_ids:
    if window_id!=parent_window_id:
        driver.switch_to.window(window_id)
        print("Switched to Child Window with ID :", window_id)
time.sleep(4)
expected_title ="Human Resources Management Software | HRMS | OrangeHRM"
if driver.title==expected_title:
    print("Switched to the correct window")
else:
    print("This is not the corect window")

expected_url ="https://www.orangehrm.com/"
if driver.current_url==expected_url:
    print("Switched to the correct window")
else:
    print("This is not a correct window")    

driver.close()
# driver.find_element(By.XPATH,"(//button[@class='nav-link contact-btn-nav'])[2]").click()
time.sleep(4)
driver.quit()




