from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os
import time
import openpyxl

wb = openpyxl.load_workbook('followups.xlsx')
sheet = wb.active

driver_path = 'C:/Users/Sourabh.Grover/Downloads/'
driver_name = 'chromedriver_win32.exe'
driver_fullpath = os.path.join(driver_path, driver_name)

username = "Sourabh.grover"
password = "Admin@2022"

def autocats(event, driver):
    try:
        print(event)
        num = int(event) - 1
        i = str(num).zfill(len(event))
        search_url = f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=modify&class=Incident&id={i}"
        driver.get(search_url)
        response_title = driver.title
        print(response_title)
        val= str(i)
        if val in response_title:
            i = event
            search_url = f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=modify&class=Incident&id={i}"
            driver.get(search_url)

        response = "Hi Team, \n \nGentle Reminder!! \n\nWe kindly request you to validate and give updates on the below-mentioned Incident. \n \nThanks & Regards \nSourabh Grover \nEGov SOC team \n0110546980 \negov@in2ittech.co.za"

        apply_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form_2']/button[2]")))
        iframe = WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="cke_3_contents"]/iframe')))
        text = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "cke_editable")))
        text.send_keys(response)
        driver.switch_to.default_content()
        apply_button.click()
        time.sleep(5)
    except TimeoutException:
        print(f"Problem in {event}")

with Chrome(service=Service(executable_path=driver_fullpath)) as driver:
    login_url = "http://10.255.253.19/CATS/CATS/web/pages/UI.php"
    driver.get(login_url)
    username_input = driver.find_element(By.ID, "user")
    password_input = driver.find_element(By.ID, "pwd")
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    for i in sheet['A']:
        i = str(i.value)
        autocats(i, driver)
