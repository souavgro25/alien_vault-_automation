from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver_path = 'C:/Users/Sourabh.Grover/Downloads/chromedriver_win32.exe'

username = "Sourabh.grover"
password = "Admin@2022"
# title = "hello"
# desc = "desc bro"
# department = "Human Settlements"
pending_reason="Awaiting for server status confirmation from client"

def create_incident(driver, title, desc, department):
    print("Creating incident...")
    create_url = "http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=new&class=Incident&c%5Bmenu%5D=NewIncident"
    driver.get(create_url)

    caller = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_caller_id"]')))
    caller.click()

    select_caller = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_caller_id"]/option[36]')))
    select_caller.click()

    origin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_origin"]')))
    origin.click()

    select_origin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_origin"]/option[3]')))
    select_origin.click()

    title_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_title"]')))
    title_input.send_keys(title)

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="cke_1_contents"]/iframe')))
    desc_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cke_editable")))
    desc_input.send_keys(desc)
    driver.switch_to.default_content()

    service = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_service_id"]')))
    service.click()

    select_service = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_service_id"]/option[6]')))
    select_service.click()

    # sub_service = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_servicesubcategory_id"]')))
    # sub_service.click()

    # sub_select_service = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2_servicesubcategory_id"]/option[3]')))
    # sub_select_service.click()

   

    department_select_xpath = '//*[@id="2_department"]/option[contains(text(), "{}")]'.format(department)
    department_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, department_select_xpath)))
    department_select.click()

    create=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form_2"]/button[2]')))
    create.click()

    asign_url="http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_assign&class=Incident&id=4451&c[menu]=NewIncident"
    driver.get(asign_url)
    check1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="att_0"]')))
    check1.click()
    check2=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="att_0"]/option[4]')))
    check2.click()

    pending_url="http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_pending&class=Incident&id=4451&c[menu]=NewIncident"
    driver.get(pending_url)
    check3=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="att_0"]')))
    check3.send_keys(pending_reason)
    check4=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="apply_stimulus"]/button[2]/span')))
    check4.click()

    inciden_no = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-widget-results-outer"]/div[3]/div/div[2]/h1/span'))).getText()
    print(inciden_no)
    time.sleep(10)



def login_cats(title,desc,department):
    with Chrome(service=Service(executable_path=driver_path)) as driver:
        login_url = "http://10.255.253.19/CATS/CATS/web/pages/UI.php"
        driver.get(login_url)

        username_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user")))
        password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pwd")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        create_incident(driver, title, desc, department)
