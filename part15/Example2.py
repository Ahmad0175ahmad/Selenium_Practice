from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com/")
time.sleep(2)
print("First page : "+ driver.title)


driver.switch_to.new_window("tab")
driver.get("https://www.youtube.com/")
time.sleep(1)
print("Second page : "+ driver.title)
driver.switch_to.new_window("window")
driver.get("https://www.facebook.com/")
time.sleep(1)
print("Third page : "+ driver.title)
handles =driver.window_handles
print("\n All Windows/tab handles", handles)


# driver.switch_to.window(handles[0])
# time.sleep(2)
# print("Web page at 0 index : "+ driver.title)
time.sleep(1)

target_title ="YouTube"
for h in handles:
    driver.switch_to.window(h)
    if driver.title==target_title:
        print("Switched to page title", driver.title)
        break
        time.sleep(2)


driver.quit()