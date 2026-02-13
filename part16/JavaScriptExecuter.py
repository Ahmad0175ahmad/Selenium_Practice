from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver =webdriver.Chrome()
driver.maximize_window()
# driver.get("https://practice.expandtesting.com/infinite-scroll")

# for i in range(10):
#     driver.execute_script("window.scrollBy(0,600);") #scroll 600px down
#     time.sleep(1)
# driver.quit()

# driver.execute_script("window.scrollBy(0,600);") #scroll 600px down
# time.sleep(1)
# driver.execute_script("window.scrollBy(0,600);") #scroll 600px down
# time.sleep(1)


# driver.execute_script("window.scrollBy(0,-600);") #scroll 600px up
# time.sleep(1)


# driver.get("https://practice.expandtesting.com/large")
# element = driver.find_element(By.ID, "sibling-50.3")
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# time.sleep(1)
# driver.quit()


driver.get("https://practice.expandtesting.com/dynamic-loading/1")
start_btn =driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")

driver.execute_script("arguments[0].click();", start_btn)
time.sleep(3)


driver.quit()