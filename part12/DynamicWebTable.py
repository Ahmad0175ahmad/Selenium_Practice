from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/dynamic-table")

time.sleep(3)
row_list=driver.find_elements(By.XPATH,"//table[@class='table table-striped']/tbody/tr")
print("Rows : ", len(row_list))


for r in range(1,len(row_list)+1):
    cell=driver.find_element(By.XPATH,f"//table[@class='table table-striped']/tbody/tr[{r}]/td[1]")
    if cell.text=="Chrome":
        cpu =driver.find_element(By.XPATH,f"//table[@class='table table-striped']/tbody/tr[{r}]/td[contains(text(),'%')]")
        print("Cpu : ",cpu.text)
        yellow_label =driver.find_element(By.ID,"chrome-cpu")
        if cpu.text in yellow_label.text:
            print("Value Equal ",yellow_label.text,cpu.text)
        else:
            print("Not match")    
        break   
    
driver.quit()