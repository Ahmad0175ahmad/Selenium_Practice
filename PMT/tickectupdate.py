from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://135.181.68.196:6040/")
time.sleep(3)

email =driver.find_element(By.NAME,"email")
email.send_keys("ahmed.akram@logicps.com")
time.sleep(2)
password = driver.find_element(By.NAME,"password")
password.send_keys("Apple0175#")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)
#project click
project = driver.find_element(By.XPATH, "//span[text()='Projects']")
project.click()

#python intern
python_intern = driver.find_element(By.XPATH, "//h4[text()='Python Interns']")
python_intern.click()

red_dates = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'_EndDate') and contains(@style,'red')]"
)
from datetime import datetime, timedelta, date

today = date.today()

for ticket in red_dates:

    date_text = ticket.text.strip()   # example: Feb 10, 2026
    print("Old Date:", date_text)

    # convert string → date
    ticket_date = datetime.strptime(date_text, "%b %d, %Y").date()

    if ticket_date < today:

        new_date = today + timedelta(days=15)
        print("Updating to:", new_date)

        # click the date
        ticket.click()
        time.sleep(2)

        # Here you must select the new date from datepicker
        # Example (depends on your calendar implementation):

        new_day = str(new_date.day)

        driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') and text()='{new_day}']"
        ).click()

        time.sleep(1)

        # click update button
        driver.find_element(By.XPATH, "//button[text()='Update']").click()

        time.sleep(2)


driver.quit()