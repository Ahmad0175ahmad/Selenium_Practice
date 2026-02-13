from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()
print("Browser opended")
driver.maximize_window()
print("Browser Maximized")
driver.get("http://www.deadlinkcity.com/")

time.sleep(2)
#links =driver.find_elements(By.TAG_NAME,"a")
links = driver.find_elements(By.XPATH,"//a")
print(f"Total links found : {len(links)}")
time.sleep(2)
#Testing each Link 
for link in links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url, timeout=5)
        if response.status_code>=400:
            print("Broken link")
        else:
            print("Valid Link")   
    except Exception as e:
        print(f"Error happened : {e}")     
driver.quit()