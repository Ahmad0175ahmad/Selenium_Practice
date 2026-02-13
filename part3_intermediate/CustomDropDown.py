from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(2)
# find dropdown
dropdown = driver.find_element(By.ID, "custom-select")

# force scroll away (so scrolling is visible)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
# scroll back to dropdown
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)
# original click (UNCHANGED)
dropdown.click()
time.sleep(2)

# original option selection (UNCHANGED)
red_option = driver.find_element(
    By.XPATH, "//div[@class='custom-options']/div[text()='Red']"
)
red_option.click()

time.sleep(2)
driver.quit()
