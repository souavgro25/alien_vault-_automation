from datetime import datetime, timedelta
import sys
import time
import os
import shutil
import pandas as pd
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import re
import csv
from readxl import excel
# Specify the username and password for the AlienVault account
username = "eGov_SOC"
password = "Admin@2023"
driver_path = 'C:/Users/Sourabh.Grover/Downloads/'

# Get the current date
today = datetime.now().date()
yesterday = today - timedelta(days=1)  # subtract one day from today's date
print("Yesterday's date:", yesterday)
# Format the current date to "DD-MM-YYYY" format
formatted_date = yesterday.strftime("%d-%m-%Y").split('-')

# d=int(formatted_date[0])-1
d = formatted_date[0]
y = formatted_date[2]
m = formatted_date[1]

n = 4
ip = [35, 37, 39, 41, 40, 38]
all = ['An user attempted to change his password',
       'A directory service object was deleted',
       'A directory service object was created',
       'A directory service object was modified',
       'User account disabled or deleted',
       'User account unlocked',
       'User account enabled or created']
Task_eventname = ['User account changed',
                  'A directory service object was moved',
                  'A directory service object was deleted',
                  'A directory service object was created',
                  'A directory service object was modified',
                  'User account disabled or deleted',
                  'User account unlocked',
                  'User account enabled or created']
Task_39_eventname = [' A user account was changed by a computer account',
                     'User account changed',
                     'A directory service object was moved',
                     'A directory service object was deleted',
                     'A directory service object was created',
                     'A directory service object was modified',
                     'User account disabled or deleted',
                     'User account unlocked',
                     'User account enabled or created',
                     'A user account was changed by another user account',
                     'An user failed to change his password']
Daily_rpt_event = ['User account disabled or deleted',
                   'Multiple Windows Logon Failures',
                   'Security Enabled Local Group Changed',
                   'Multiple Windows Logon Failures',
                   'Logon Failure - Unknown user or bad password',
                   'User account enabled or created']
DB_rpt_events = ['MS SQL Server Logon Failure', 'MS SQL Server Logon Success']
Daily_rpt_event2 = ['Multiple Windows Logon Failures',
                    'Logon Failure - Unknown user or bad password']
userchange = ['User account changed']
# View define
Task_view = ['User account changed']
Daily_rpt_view = ['Multiple Windows Logon Failure',
                  'Security Enabled Local Group Changed',
                  'User account created/deleted']
Daily_rpt_view2 = ['Multiple Windows Logon Failure']
DB_rpt_view = ['Database Logon Success/Failure']

# download directory
download_path = "C:/Users/Sourabh.Grover/Downloads/"
task_dst_path = f"C:/Users/Sourabh.Grover/Desktop/daily task data/Task_data_{d}_{m}_{y}"
Daily_rpt_dst_path = f"C:/Users/Sourabh.Grover/Desktop/Daily report/Daily_rpt_{d}_{m}_{y}"
DB_rpt_dst_path = f"C:/Users/Sourabh.Grover/Desktop/DB report/DB_rpt_{d}_{m}_{y}"


session = requests.Session()


def download(eventname, d, m, ip, cr_view, dst_p):

    # Specify the URL of the AlienVault login page
    events_url = f"https://10.255.253.{ip}/ossim/forensics/"
    # Initialize the Chrome driver and navigate to the AlienVault login page

    # Navigate to the events page
    searchurl = f"https://10.255.253.{ip}/ossim/forensics/base_stat_alerts.php?sort_order=occur_d&submit=Query+DB&sig_type=0&sig[0]=LIKE&sig[1]={eventname}&sig[2]=&&time_range=range&time_cnt=2&time%5B0%5D%5B0%5D=+&time%5B0%5D%5B1%5D=%3E%3D&time%5B0%5D%5B8%5D=+&time%5B0%5D%5B9%5D=AND&time%5B1%5D%5B1%5D=%3C%3D&time%5B0%5D%5B2%5D={m}&time%5B0%5D%5B3%5D={d}&time%5B0%5D%5B4%5D=2023&time%5B0%5D%5B5%5D=00&time%5B0%5D%5B6%5D=00&time%5B0%5D%5B7%5D=00&time%5B1%5D%5B2%5D={m}&time%5B1%5D%5B3%5D={d}&time%5B1%5D%5B4%5D=2023&time%5B1%5D%5B5%5D=23&time%5B1%5D%5B6%5D=59&time%5B1%5D%5B7%5D=59"
    response = session.get(searchurl, verify=False)
    if response.status_code == 200:

        # print(response.text)
        html_content = response.text
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all links in the HTML content
        links = soup.find_all('a')

        # Search for links that start with the desired URL
        pattern = r'base_qry_main\.php\?new=1&submit=Query.*'
        matching_links = [link for link in links if re.search(
            pattern, link.get('href', ''))]

        extend_url = ""
        if matching_links == []:
            print(f"{eventname} is not found on .{ip}")
            return

        else:
            view_url = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view={cr_view}"

            for link in matching_links:

                extend_url = link.get('href')

            res = session.get(f"{events_url}{extend_url}", verify=False)
            res = session.get(view_url, verify=False)
            res = session.get(
                f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?submit=Query+DB&export=1&show_rows=5000", verify=False)
            res = session.get(
                f"https://10.255.253.{ip}/ossim/forensics/csv.php?rtype=33", verify=False)

            if res.status_code == 200:
                # Decode the res content as UTF-8 and split it into lines
                lines = res.content.decode('utf-8').splitlines()
                # Create a CSV reader object from the lines
                reader = csv.reader(lines)
                # Iterate over the rows of the CSV file
                try:

                    with open(f'{dst_p}/{eventname}_{ip}.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        # Write each row from the reader object to the writer object
                        for row in reader:
                            writer.writerow(row)
                    print(
                        f'File {eventname}_{ip} downloaded and saved successfully')
                except:
                    print(
                        f"some error may be same name{eventname}_{ip} file is exist ")
    else:
        print('Access to protected page failed')

    return


def download_data(events, dst_p, view, ip):

    os.makedirs(dst_p, exist_ok=True)
    print(dst_p)
    for ip in ip:
        login_url = f"https://10.255.253.{ip}/ossim/session/login.php"
        requests.packages.urllib3.disable_warnings()

        response = requests.get(login_url, verify=False)

        Phpses = response.cookies['PHPSESSID']

        cookie = f"PHPSESSID={Phpses}"

        login_data = {
            'user': username,
            'passu': password,
            'embed': '',
            'bookmark_string': '',
            "pass":	"QWRtaW5AMjAyMw=="

        }

        response = session.post(login_url, data=login_data, verify=False,
                                allow_redirects=True, headers={'Cookie': cookie})

        # Check if the login was successful
        # Check if the login was successful
        if response.status_code == 200:
            print(f'Login successful {login_url}')
            if ip == 39 and view == Task_view:
                events_id = Task_39_eventname
            else:
                events_id = events
            for i in events_id:
                print(i)
                if i == "Security Enabled Local Group Changed":
                    cr_view = view[1]
                elif (i == "User account enabled or created" or i == "User account disabled or deleted") and (view == Daily_rpt_view):
                    cr_view = view[2]
                else:
                    cr_view = view[0]
                print(f"event name is {i} and view is {cr_view}")
                download(i, d, m, ip, cr_view, dst_p)

        else:
            print(f'Login failed {login_url}')


try:
    select_data = sys.argv[1].lower()
except:
    select_data = ""
if select_data == "daily":
    download_data(Daily_rpt_event, Daily_rpt_dst_path, Daily_rpt_view, ip)
    excel(Daily_rpt_dst_path)
if select_data == "db":
    download_data(DB_rpt_events, DB_rpt_dst_path, DB_rpt_view, ip)
    excel(DB_rpt_dst_path)
if select_data == "task":
    download_data(Task_eventname, task_dst_path, Task_view, ip)
    excel(task_dst_path)
if select_data == 'all':
    download_data(Daily_rpt_event, Daily_rpt_dst_path, Daily_rpt_view, ip)
    download_data(DB_rpt_events, DB_rpt_dst_path, DB_rpt_view, ip)
    download_data(Task_eventname, task_dst_path, Task_view, ip)
    excel(Daily_rpt_dst_path)
    excel(DB_rpt_dst_path)
    excel(task_dst_path)

if select_data == "" or "help":
    print("please give argument \n * db for db report \n * daily for daily report \n * task for Task Data \n * all for All (db, daily ,task ) data ")


# Display the contents of the dictionary
