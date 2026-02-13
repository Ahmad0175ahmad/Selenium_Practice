from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/alerts")

#confirm alert
# confirm_btn=driver.find_element(By.ID, "confirmButton")
# confirm_btn.click()
# time.sleep(3)
# confirm=driver.switch_to.alert
# print("Alert message : ",confirm.text)
# confirm.accept()
# time.sleep(3)
# simplealert =driver.switch_to.alert
# print("Second alert : ", simplealert.text)
# simplealert.accept()


#prompt alert
prompt_btn = driver.find_element(By.ID, "promptButton")
prompt_btn.click()
time.sleep(2)
prompt = driver.switch_to.alert
prompt.send_keys("hello ahmad")
time.sleep(2)
prompt.accept()
time.sleep(3)

secondalert =driver.switch_to.alert
print("Send alert text : ",secondalert.text)
secondalert.accept()

driver.quit()

