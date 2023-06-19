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
print("Yesterday's date:", yesterday)
# Format the current date to "DD-MM-YYYY" format
formatted_date = yesterday.strftime("%d-%m-%Y").split("-")
formatted_date_today = today.strftime("%d-%m-%Y").split("-")
# d=int(formatted_date[0])-1
d = formatted_date[0]
y = formatted_date[2]
m = formatted_date[1]

td = formatted_date_today[0]
ty = formatted_date_today[2]
tm = formatted_date_today[1]

try:
    ip = [sys.argv[2]]
    if ip == [] :
        ip = [37, 38, 39, 40, 41]
except:
     ip = [37, 38, 39, 40, 41]
event_name = [
    "Special privileges assigned to new logon",
    "Windows Network Logon",
    "Kerberos user pre-authentication failed",
    "Windows audit failure event",
    "Windows DC Logon Failure",
    "Failed attempt to perform a privileged operation",
    "Logon Failure - Unknown user or bad password"
]
all = [
    "Logon Failure - Unknown user or bad password"
]
userchange = ["User account changed"]
analysis_dst_path = f"C:/Users/Sourabh.Grover/Desktop/Analysis/Analysis_{d}_{m}_{y}"

session = requests.Session()


def finduser(html_code):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_code, "html.parser")

    # Find all <td> tags with align="left"
    left_td_tags = soup.find_all("td", {"align": "left"})

    # Find all <td> tags with anchor tags containing links
    link_td_tags = soup.find_all("td", {"align": "center"})

    # Create a dictionary to store the data
    list1 = []
    list2 = []
    list3 = []
    full = []

    for td in left_td_tags:
        data_dict = {}
        username = td.text.strip()
        # print(username)
        list1.append(username)

    for td in link_td_tags:
        anchor = td.find("a")
        if anchor is not None:
            count = anchor.text.strip()
            data_dict["count"] = count
            link = anchor["href"]
            data_dict["link"] = link
            list2.append(count)
            list3.append(link)

    for item1, item2, item3 in zip(list1, list2, list3):
        data_dict = {"username": item1, "count": item2, "link": item3}
        full.append(data_dict)

    return full


def download(eventname, d, m, ip, cr_view, dst_p,tm,td):

    events_url = f"https://10.255.253.{ip}/ossim/forensics/"

    searchurl = f"https://10.255.253.{ip}/ossim/forensics/base_stat_alerts.php?sort_order=occur_d&submit=Query+DB&sig_type=0&sig[0]=LIKE&sig[1]={eventname}&sig[2]=&&time_range=range&time_cnt=2&time%5B0%5D%5B0%5D=+&time%5B0%5D%5B1%5D=%3E%3D&time%5B0%5D%5B8%5D=+&time%5B0%5D%5B9%5D=AND&time%5B1%5D%5B1%5D=%3C%3D&time%5B0%5D%5B2%5D={m}&time%5B0%5D%5B3%5D={d}&time%5B0%5D%5B4%5D=2023&time%5B0%5D%5B5%5D=00&time%5B0%5D%5B6%5D=00&time%5B0%5D%5B7%5D=00&time%5B1%5D%5B2%5D={tm}&time%5B1%5D%5B3%5D={td}&time%5B1%5D%5B4%5D=2023&time%5B1%5D%5B5%5D=23&time%5B1%5D%5B6%5D=59&time%5B1%5D%5B7%5D=59"

    response = session.get(searchurl, verify=False)
    username_url = f"https://10.255.253.{ip}/ossim/forensics/base_stat_extra.php?sort_order=occur_d&addr_type=username"
    response = session.get(username_url)
    if response.status_code == 200:

        html_content = response.text

        matching_links = finduser(html_content)
        filtered_count = [
            item for item in matching_links if int(item["count"].replace(".", "")) > 100
        ]
        filtered_data = [
            item for item in filtered_count if not item["username"].endswith("$")
        ]
        filtered_data = [item for item in filtered_data if item !=
                         '-  Account Domain:  -  Logon ID:  0x0  Logon Type:   3  New Logo']
        searchuser = []
        for i in filtered_data:
            print(i["username"])
            searchuser.append(i["username"])

        # users = searchoutlook(eventname, searchuser)
        # print(users)
        # filtered_users = {}
        filter_userdata = []

        # for value in filtered_data:
        #     username = value["username"]
        #     if username in users:
        #         filtered_users = value
        #         filter_userdata.append(filtered_users)
        filter_userdata = filtered_data

        print(filter_userdata)

        # Find all links in the HTML content
        # matching_links=[]

        extend_url = ""
        if filter_userdata == []:
            print(f"{eventname} is not found on .{ip}")
            return

        else:
            view_url = f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?num_result_rows=-1&submit=Query+DB&current_view=-1&custom_view={cr_view}"
            res = session.get(view_url, verify=False)
            n = 0
            for link in filter_userdata:
                n = n + 1
                extend_url = link["link"]

                res = session.get(f"{events_url}{extend_url}", verify=False)
                html = res.text
                # getss(html,link['username'])
                res = session.get(view_url, verify=False)
                res = session.get(
                    f"https://10.255.253.{ip}/ossim/forensics/base_qry_main.php?submit=Query+DB&export=1&show_rows=5000",
                    verify=False,
                )
                res = session.get(
                    f"https://10.255.253.{ip}/ossim/forensics/csv.php?rtype=33",
                    verify=False,
                )

                if res.status_code == 200:
                    # Decode the res content as UTF-8 and split it into lines
                    lines = res.content.decode("utf-8").splitlines()
                    # Create a CSV reader object from the lines
                    reader = csv.reader(lines)
                    # Iterate over the rows of the CSV file
                    try:

                        with open(
                            f'{dst_p}/{eventname}_{ip}_{link["username"]}.csv',
                            "w",
                            newline="",
                        ) as f:
                            writer = csv.writer(f)
                            # Write each row from the reader object to the writer object
                            for row in reader:
                                writer.writerow(row)
                        print(
                            f"File {eventname}_{ip} downloaded and saved successfully"
                        )
                    except:
                        print(
                            f"some error may be same name{eventname}_{ip} file is exist "
                        )
    else:
        print("Access to protected page failed")

    return


def download_data(events, dst_p, view, ip):

    os.makedirs(dst_p, exist_ok=True)
    print(dst_p)
    for ip in ip:

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
            crview = view[0]
            print(f"Login successful {login_url}")
            events_id = events
            for i in events_id:
                print(i)
                print(f"event name is {i} and view is {crview}")
                download(i, d, m, ip, crview, dst_p,tm,td)

        else:
            print(f"Login failed {login_url}")


if len(sys.argv) <= 1:
    print("Usage: python scrape.py 1 \n use 1 for 'Special privileges assigned to new logon' \n use 2 for 'Windows Network Logon' \n use 3 for 'Kerberos user pre-authentication failed' \n use 4 for 'Windows audit failure event' \n use 5 for 'Windows DC Logon Failure' \n use 6 for 'Failed attempt to perform a privileged operation' \n use 7 for 'Logon Failure - Unknown user or bad password' ")
    sys.exit(1)

eventname = str(sys.argv[1])


if eventname == "1":
    download_data([event_name[0]], analysis_dst_path, userchange, ip)
if eventname == "2":
    download_data([event_name[1]], analysis_dst_path, userchange, ip)
if eventname == "3":
    download_data([event_name[2]], analysis_dst_path, userchange, ip)
if eventname == "4":
    download_data([event_name[3]], analysis_dst_path, userchange, ip)
if eventname == "5":
    download_data([event_name[4]], analysis_dst_path, userchange, ip)
if eventname == "6":
    download_data([event_name[5]], analysis_dst_path, userchange, ip)
if eventname == "7":
    download_data([event_name[6]], analysis_dst_path, userchange, ip)
