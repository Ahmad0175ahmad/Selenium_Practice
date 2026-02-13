from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

input_fields =driver.find_elements(By.TAG_NAME ,"input")
# print(len(input_fields))

# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# index = 0
# for field in input_fields:
#     print(f"index:{index} : {field.get_attribute('id')} ")
#     index=index+1

input_fields[0].send_keys("standard_user")
input_fields[1].send_keys("secret_sauce")
time.sleep(2)
input_fields[2].click()


products =driver.find_elements(By.XPATH , "//div[@class='inventory_item_name ']")

for product in products:
    print(product.text)

time.sleep(3)
input("Press Enter")
driver.quit()

