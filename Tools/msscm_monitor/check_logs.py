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
# from readxl import excel
# from check_user import searchoutlook

# Specify the username and password for the AlienVault account
username = "eGov_SOC"
password = "Admin@2023"
driver_path = "C:/Users/Sourabh.Grover/Downloads/"

today = datetime.now().date()
yesterday = today - timedelta(days=1)  # subtract one day from today's date
print("Today's date:", today)
# print("Yesterday's date:", yesterday)
# Format the current date to "DD-MM-YYYY" format
formatted_Today_date = today.strftime("%d-%m-%Y").split("-")
formatted_date = yesterday.strftime("%d-%m-%Y").split("-")

# d=int(formatted_date[0])-1
d = formatted_date[0]
y = formatted_date[2]
m = formatted_date[1]

# todays day date
Td = formatted_Today_date[0]
Ty = formatted_Today_date[2]
Tm = formatted_Today_date[1]
ip = "35"


session = requests.Session()


def check_Msccm():

    url_date = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?clear_criteria=time&clear_criteria_element=&submit=Query DB&=&time_range=range&time_cnt=2&time[0][0]= &time[0][1]=>=&time[0][8]= &time[0][9]=AND&time[1][1]=<=&time[0][2]={m}&time[0][3]={d}&time[0][4]={y}&time[0][5]=00&time[0][6]=00&time[0][7]=00&time[1][2]={Tm}&time[1][3]={Td}&time[1][4]={Ty}&time[1][5]=23&time[1][6]=59&time[1][7]=59"

    session.get(url_date)
    msscm_url = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?search=1&hidden_menu=1&bsf=Query+DB&search_str=&submit=Event+Name&selected_time_range=on&userdata%5B0%5D=userdata1&userdata%5B1%5D=like&plugin=1844&sort_order=&plugingroup=&ctx=&sensor=&userdata%5B2%5D=&addhomeips=-1&networkgroup=&ossim_risk_a=+&rep%5B1%5D=&rep%5B0%5D=&otx%5B0%5D=&tags=Last%2520Day&groupby_1=&groupby_ip=ipempty&groupby_hostname=hostnameempty&groupby_username=usernameempty&groupby_port=portempty&groupby_proto=portprotoempty"
    res = session.get(msscm_url, verify=False)

    latest_log_time(res.text)


def latest_log_time(html_code):

    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find the <td> tag containing the time
    time_td = soup.find('td', align='center').text.strip()
     
    print(time_td)


def login(ip):

    login_url = f"https://10.255.253.{ip}/ossim/session/login.php"
    requests.packages.urllib3.disable_warnings()

    response = requests.get(login_url, verify=False)

    Phpses = response.cookies["PHPSESSID"]

    cookie = f"PHPSESSID={Phpses}"

    login_data = {
        "user": username,
        "passu": password,
        "embed": "",
        "bookmark_string": "",
        "pass": "QWRtaW5AMjAyMw==",
    }

    response = session.post(
        login_url,
        data=login_data,
        verify=False,
        allow_redirects=True,
        headers={"Cookie": cookie},
    )

    if response.status_code == 200:

        # print(f"Login successful {login_url}")
        check_Msccm()

    else:
        print(f"Login failed {login_url}")


login(ip)
