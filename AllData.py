from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import sys
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

# Get the current date
current_date = datetime.date.today()

# Format the current date to "DD-MM-YYYY" format
formatted_date = current_date.strftime("%d-%m-%Y").split('-')

d=int(formatted_date[0])-1
y=formatted_date[2]
m=formatted_date[1]

n=4
ip=[35,37,39,41,38,40]
all =['An user attempted to change his password','A directory service object was deleted','A directory service object was created','A directory service object was modified','User account disabled or deleted','User account unlocked','User account enabled or created']
Task_eventname= ['A directory service object was modified','A directory service object was deleted','A directory service object was created','A directory service object was modified','User account disabled or deleted','User account unlocked','User account enabled or created']
Daily_rpt_event=['Security Enabled Local Group Changed','Multiple Windows Logon Failures','Logon Failure - Unknown user or bad password']
DB_rpt_events=['MS SQL Server Logon Failure','MS SQL Server Logon Success']

# View define
Task_view=['User account changed']
Daily_rpt_view=['Multiple Windows Logon Failure','Security Enabled Local Group Changed']
DB_rpt_view=['Database Logon Success/Failure']

# download directory
download_path="C:/Users/Sourabh.Grover/Downloads/"
task_dst_path = f"C:/Users/Sourabh.Grover/Desktop/daily task data/Task_data_{d}_{m}_{y}"
Daily_rpt_dst_path = f"C:/Users/Sourabh.Grover/Desktop/Daily report/Daily_rpt_{d}_{m}_{y}"
DB_rpt_dst_path = f"C:/Users/Sourabh.Grover/Desktop/DB report/DB_rpt_{d}_{m}_{y}"



def download(eventname,d,m,n,ip,cr_view):
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
    viewurl=f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view={cr_view}"
    # if ip==41:
    #     viewurl=f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=User%20Account%20Changed"
    # elif ip==39:
    #     viewurl = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=user account change"
    # elif ip==38:
    #     viewurl = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view=User Account changed"
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
    filename = f"Events_egov_soc_2023-{m}-{d}.csv"
    # wait for the" download to complete
    while not os.path.exists(f"C:/Users/Sourabh.Grover/Downloads/{filename}"):
        print(f"not exist {filename}")
        time.sleep(1)
    return filename



def download_data(events,dst_p,view,ip):
    os.makedirs(dst_p, exist_ok=True)
    for ip in ip :
        for i in events:
            if i =="Security Enabled Local Group Changed":
                crt_view=view[1]
            else:
                crt_view=view[0]
            filename = download(i,d,m,n,ip,crt_view)
            try:
                new_filename = f"{i}_{ip}_{d}_{m}.csv"
                os.rename(os.path.join(download_path, filename), os.path.join(download_path, new_filename))

                src_path=os.path.join(download_path,new_filename)
                shutil.move(src_path, dst_p)
            except :
                continue    
            
try:
    select_data=sys.argv[1].lower()
except :
    select_data = ""
if select_data == "daily":
    download_data(Daily_rpt_event,Daily_rpt_dst_path,Daily_rpt_view,ip)

if select_data =="db":
    download_data(DB_rpt_events,DB_rpt_dst_path,DB_rpt_view,ip)
if  select_data =="task":
    download_data(Task_eventname,task_dst_path,Task_view,ip)

if select_data =='all':
    download_data(Daily_rpt_event,Daily_rpt_dst_path,Daily_rpt_view,ip)
    download_data(DB_rpt_events,DB_rpt_dst_path,DB_rpt_view,ip)
    download_data(Task_eventname,task_dst_path,Task_view,ip)

if select_data == "" or "help":
    print ("please give argument \n * db for db report \n * daily for daily report \n * task for Task Data \n * all for All (db, daily ,task ) data ")