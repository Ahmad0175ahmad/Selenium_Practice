from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time, os 
#from dotenv import load_dotenv

#load_dotenv()
# USER_EMAIL = os.getenv("USER_EMAIL")
# USER_PASSWORD = os.getenv("USER_PASSWORD")
# SELECTED_USER_EMAIL = os.getenv("SELECTED_USER_EMAIL")
URL="http://135.181.68.196:6040"

USER_EMAIL = ''
USER_PASSWORD = ''
SELECTED_USER_EMAIL = ""


chrome_options = webdriver.ChromeOptions() 

prefs = {"profile.password_manager_leak_detection": False}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get(URL)

try:
    wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(USER_EMAIL)
    wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(USER_PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))).click()
    print("Login successful.")

except Exception as e:
    print("Login failed:", e)
    driver.quit()
    exit()

time.sleep(2)
# import pyautogui
# pyautogui.click(1213, 5144)
# time.sleep(2)


try:
    driver.find_element(By.XPATH,"//li[@title='Projects']//span[@class='_icon_1718h_96']").click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//h4[text()='Python Interns']"))).click()
    filter_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Filter']")))
    filter_button.click()
    time.sleep(2)

    user_checkbox_xpath = f"//label[contains(., '{SELECTED_USER_EMAIL}')]/input[@type='checkbox']"

    wait.until(EC.presence_of_element_located((By.XPATH, user_checkbox_xpath))).click()
    print("User selected.")

    filter_button.click()
    print("Filter applied.")

except Exception as e:
    print("Filtering failed:", e)
    driver.quit()
    exit()

time.sleep(2)

print("Searching for overdue tickets...")
index = 0
while True:
    try:
        tickets = driver.find_elements(By.CSS_SELECTOR, "div[class*='taskcontainer']")
        if index >= len(tickets):
            break
    except Exception:
        print("No tickets found or error retrieving tickets.")
        break

    ticket = tickets[index]
    try:
        due_date_element = ticket.find_element(By.CSS_SELECTOR, "div[class*='EndDate']")
        if "red" in due_date_element.get_attribute("style"):
            print(f"Updating overdue ticket #{index + 1}...")
            ticket.click()

            modal_due_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'_headerElements')]//p[contains(@style,'red')]")))
            modal_due_date.click()

            target_date = datetime.today() + timedelta(days=30)

            current_month_text = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__current-month").text
            if target_date.strftime("%B") not in current_month_text:
                 wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__navigation--next"))).click()

            day_xpath = f"//div[contains(@class,'react-datepicker__day') and not(contains(@class,'--outside-month')) and text()='{target_date.day}']"
            wait.until(EC.element_to_be_clickable((By.XPATH, day_xpath))).click()
            print(f"Date successfully updated to {target_date.strftime('%Y-%m-%d')}.")

            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(2)

    except Exception:
            print(f"Ticket #{index + 1} encountered an error.")

    index += 1

print("\nProcess complete. All overdue tickets have been updated.")
time.sleep(3)
driver.quit()
