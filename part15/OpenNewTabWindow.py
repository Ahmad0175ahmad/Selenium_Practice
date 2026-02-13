from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com/")
time.sleep(2)
print("First page : "+ driver.title)

#driver.switch_to.new_window("tab")
driver.switch_to.new_window("window")


driver.get("https://www.facebook.com/")
time.sleep(2)
print("Second page : "+ driver.title)

driver.close()
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[0])
print("First page : "+ driver.title)


driver.quit()