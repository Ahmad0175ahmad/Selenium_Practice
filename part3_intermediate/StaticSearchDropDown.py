from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(2)
# find dropdown
search_box = driver.find_element(By.CLASS_NAME, "search-box")

# force scroll away (so scrolling is visible)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
# scroll back to dropdown
driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
time.sleep(1)
# original click (UNCHANGED)
search_box.click()
search_box.send_keys("S")
time.sleep(2)
option = driver.find_element(By.XPATH, "//div[@class='searchable-option' and text()='SUV']")
option.click()
time.sleep(3)

driver.quit()


