from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")

time.sleep(2)
#username=driver.find_element(By.NAME,"user-name")
username = driver.find_element(By.XPATH ,"//input[@id='user-name']")
username.send_keys("standard_user")
time.sleep(1)
#userpassword = driver.find_element(By.ID,"password")
userpassword = driver.find_element(By.XPATH , "//input[@name='password']")
userpassword.send_keys("secret_sauce")
time.sleep(1)

button = driver.find_element(By.XPATH, "//input[@id='login-button']")
button.click()
time.sleep(4)

# item = driver.find_element( By.XPATH, "//div[text()='Sauce Labs Onesie']/parent::a")
# item.click()
item = driver.find_element(By.LINK_TEXT , 'Sauce Labs Onesie')
item.click()
# item3 =driver.find_element(By.XPATH, "//a[@id = 'item_2_title_link']")
# item3.click()
# item2 = driver.find_element(By.XPATH , "//button[@id='add-to-cart-sauce-labs-backpack']")

# item2.click()
time.sleep(2)

input("Press the enter :")

driver.quit()


