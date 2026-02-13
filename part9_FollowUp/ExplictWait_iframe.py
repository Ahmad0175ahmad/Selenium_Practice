from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/myfolders/PYTHON%20CODING/Selenium1/iframePracticeSite/nested-frame.html")
time.sleep(2)


iframes=driver.find_elements(By.NAME ,"parentFrame")


if iframes:
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME ,"parentFrame"))
        )
    except:
        print("Parent frame not found")    
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, "childFrame"))
        )
    except:
        print("Child frame not found")    

    childtext = driver.find_element(By.ID , "childText")
    print("Child Text : ", childtext.text)


    driver.switch_to.parent_frame()

    iframes_ParentFrame = driver.find_elements(By.TAG_NAME , "iframe")
    print("Total iframe in parent frame : ", len(iframes_ParentFrame))


    parenttext =driver.find_element(By.TAG_NAME, "p")
    print("Parent text : ", parenttext.text)

    driver.switch_to.default_content()


    iframes = driver.find_elements(By.TAG_NAME , "iframe")
    print("Total iframe in main : ", len(iframes))

else:
    print("parentFrame not found ")

driver.quit()        