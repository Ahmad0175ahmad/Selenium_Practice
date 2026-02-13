from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
driver.maximize_window()

# driver.implicitly_wait(10)

# search_box = driver.find_element(By.NAME, "q")
wait = WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException , TimeoutException ,Exception])
search_box =wait.until(EC.presence_of_element_located((By.NAME,"q")))
search_box.send_keys("Selenium")

search_box.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()