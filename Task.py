from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import os
import shutil

Options = Options()
Options.add_experimental_option("detach", True)

# Specify the username and password for the AlienVault account
username = "eGov_SOC"
password = "Admin@2023"
driver_path = 'C:/Users/Sourabh.Grover/Downloads/'
driver_name = 'chromedriver_win32.exe'
driver_fullpath = os.path.join(driver_path, driver_name)

d=22
y=2023
m='04'
n=4
ip=[35,37,39,41,38,40]
all =['An user attempted to change his password','A directory service object was deleted','A directory service object was created','A directory service object was modified','User account disabled or deleted','User account unlocked','User account enabled or created']
eventname= ['A directory service object was modified']
download_path="C:/Users/Sourabh.Grover/Downloads/"

dst_path = f"C:/Users/Sourabh.Grover/Desktop/daily task data/{d}_{m}_{y}"
os.makedirs(dst_path, exist_ok=True)

def download(eventname,d,m,n,ip):
    # Specify the URL of the AlienVault login page
    url = f"https://10.255.253.{ip}/ossim/session/login.php"
    # Initialize the Chrome driver and navigate to the AlienVault login page
    driver = Chrome(executable_path=driver_fullpath)
    driver.get(url)
    time.sleep(0)
    allow1 = driver.find_element(By.ID, 'details-button')
    allow1.click()
    allow = driver.find_element(By.ID, 'proceed-link')
    allow.click()
    time.sleep(1)
    # Find the username and password input fields and enter the login credentials
    username_input = driver.find_element(By.ID, "user")
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, "passu")
    password_input.send_keys(password)
    # Submit the login form
    password_input.send_keys(Keys.RETURN)
    time.sleep(1)
    # Navigate to the events page        
    searchurl = f"https://10.255.253.{ip}/ossim/forensics/base_stat_alerts.php?sort_order=occur_d&submit=Query+DB&sig_type=0&sig[0]=LIKE&sig[1]={eventname}&sig[2]=&&time_range=range&time_cnt=2&time%5B0%5D%5B0%5D=+&time%5B0%5D%5B1%5D=%3E%3D&time%5B0%5D%5B8%5D=+&time%5B0%5D%5B9%5D=AND&time%5B1%5D%5B1%5D=%3C%3D&time%5B0%5D%5B2%5D={m}&time%5B0%5D%5B3%5D={d}&time%5B0%5D%5B4%5D=2023&time%5B0%5D%5B5%5D=00&time%5B0%5D%5B6%5D=00&time%5B0%5D%5B7%5D=00&time%5B1%5D%5B2%5D={m}&time%5B1%5D%5B3%5D={d}&time%5B1%5D%5B4%5D=2023&time%5B1%5D%5B5%5D=23&time%5B1%5D%5B6%5D=59&time%5B1%5D%5B7%5D=59"
    driver.get(searchurl)
    try:
        driver.find_element(By.CLASS_NAME,"qlink").click()
    except:
        n=n-1
        print("breaking")
        return
    viewurl=f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=User account changed"
    if ip==41:
        viewurl=f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=User%20Account%20Changed"
    elif ip==39:
        viewurl = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=user account change"
    elif ip==38:
        viewurl = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=User Account changed"
    driver.get(viewurl)
    time.sleep(1)
    downloadlink=f"https://10.255.253.{ip}/ossim/forensics/report_launcher.php?url=/ossim/forensics/base_stat_alerts.php?sort_order=occur_d&submit=Query+DB&sig_type=0&sig[0]=LIKE&sig[1]={eventname}&sig[2]=&&time_range=range&time_cnt=2&time%5B0%5D%5B0%5D=+&time%5B0%5D%5B1%5D=%3E%3D&time%5B0%5D%5B8%5D=+&time%5B0%5D%5B9%5D=AND&time%5B1%5D%5B1%5D=%3C%3D&time%5B0%5D%5B2%5D={m}&time%5B0%5D%5B3%5D={d}&time%5B0%5D%5B4%5D=2023&time%5B0%5D%5B5%5D=00&time%5B0%5D%5B6%5D=00&time%5B0%5D%5B7%5D=00&time%5B1%5D%5B2%5D={m}&time%5B1%5D%5B3%5D={d}&time%5B1%5D%5B4%5D=2023&time%5B1%5D%5B5%5D=23&time%5B1%5D%5B6%5D=59&time%5B1%5D%5B7%5D=59&type=33"
    driver.get(downloadlink)
    driver.find_element(By.ID,'numrows').click()
    down=driver.find_element(By.XPATH,'//option[text()="5000"]')
    down.click()
    download_link=driver.find_element(By.NAME,"generate")
    download_link.click()
    d=d+1
    filename = f"Events_egov_soc_2023-{m}-{d} ({n}).csv"
    # wait for the" download to complete
    while not os.path.exists(f"C:/Users/Sourabh.Grover/Downloads/{filename}"):
        print(f"not exist {filename}")
        time.sleep(1)
    return filename




for ip in ip :
    for i in eventname:
        filename = download(i,d,m,n,ip)
        try:
            new_filename = f"{i}_{ip}_{d}_{m}.csv"
            os.rename(os.path.join(download_path, filename), os.path.join(download_path, new_filename))

            src_path=os.path.join(download_path,new_filename)
            shutil.move(src_path, dst_path)
        except :
            continue      
    