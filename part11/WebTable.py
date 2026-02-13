from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome()

driver.get("D:\\myfolders\\PYTHON CODING\\Selenium1\\part11\\index.html")

time.sleep(3)
secondelement= driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[2]")
print(secondelement.text)


row_list=driver.find_elements(By.XPATH,"//table/tbody/tr")
print("Rows : ", len(row_list))


col_list = driver.find_elements(By.XPATH,"//table/tbody/tr[1]/th")
print("Columns : ",len(col_list))

for r in range(2, len(row_list)+1):
    for c in range(1, len(col_list)+1):

        # cell path
        cell_xpath=f"//table/tbody/tr[{r}]/td[{c}]"
        cell =driver.find_element(By.XPATH, cell_xpath)

        data =cell.text
        print(data)
    print()    




driver.quit()