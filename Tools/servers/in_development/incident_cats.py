import requests
from bs4 import BeautifulSoup
import re

username = "Sourabh.grover"
password = "Admin@2022"

session = requests.Session()


def create_incident():
    payload={
        "operation": "apply_new",
        "attr_org_id": 2,
        "attr_caller_id": 56,
        "attr_personLocation": 1,
        "attr_origin": "monitoring",
        "attr_title": "Server Disconnected - Server Name: GPDCSMDC07 and IP: 10.1.102.89",
        "attr_description": '<p>&nbsp;</p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Hi Good day Team, </span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; We have observed that Server Name: GPDCSMDC07 and IP: 10.1.102.89 which belongs to Department: Community Safety is disconnected on SIEM console.</span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; The communication between the server and the SIEM (OSSIEM) is not working. Please check the SIEM (OSSIEM) agent on the Task bar and also confirm if SIEM (OSSIEM) services are running.</span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Please check and provide us an update for the same. </span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Thanks &amp; Regards,<br />&nbsp;&nbsp;&nbsp; Sourabh Grover<br />&nbsp;&nbsp;&nbsp; EGov SOC team<br />&nbsp;&nbsp;&nbsp; 0110546980<br />&nbsp;&nbsp;&nbsp; egov@in2ittech.co.za<br />&nbsp;&nbsp;&nbsp; </span></span></p>',
        "attr_service_id": 5,
        "attr_servicesubcategory_id": 25,
        "attr_service_details": {"legacy":"0","extradata_id":"","current_template_id":"","current_template_data":""},
        "attr_priority": 4,
        "attr_department": "safety",
        "attr_parent_incident_id":"", 
        "attr_parent_problem_id": "",
        "attr_parent_change_id": "",
        "attr_FST": "",
        "attr_FST_reported_at_site": "no",
        "attr_FST_work_finished": "no",
        "attr_FST_comment": "",
        "attr_private_log": "",
        "attr_public_log": '<p>&nbsp;</p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Hi Good day Team, </span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; We have observed that Server Name: GPDCSMDC07 and IP: 10.1.102.89 which belongs to Department: Community Safety is disconnected on SIEM console.</span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; The communication between the server and the SIEM (OSSIEM) is not working. Please check the SIEM (OSSIEM) agent on the Task bar and also confirm if SIEM (OSSIEM) services are running.</span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Please check and provide us an update for the same. </span></span></p><p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif">&nbsp;&nbsp;&nbsp; Thanks &amp; Regards,<br />&nbsp;&nbsp;&nbsp; Sourabh Grover<br />&nbsp;&nbsp;&nbsp; EGov SOC team<br />&nbsp;&nbsp;&nbsp; 0110546980<br />&nbsp;&nbsp;&nbsp; egov@in2ittech.co.za<br />&nbsp;&nbsp;&nbsp; </span></span></p>',
        "attr_functionalcis_list": "",
        "attr_functionalcis_list_tbd": [],
        "attr_functionalcis_list_tbm": {},
        "attr_functionalcis_list_tbc": [],
        "attr_contacts_list": "",
        "attr_contacts_list_tbd": [],
        "attr_contacts_list_tbm": {},
        "attr_contacts_list_tbc": [],
        "attr_child_incidents_list_tbr": [],
        "attr_child_incidents_list_tba": [],
        "attr_child_incidents_list_tbd": [],
        "attr_child_incidents_list_tbc": {},
        "attr_related_request_list_tbr": [],
        "attr_related_request_list_tba": [],
        "attr_related_request_list_tbd": [],
        "attr_related_request_list_tbc": {},
        "attr_document_list": "",
        "attr_document_list_tbd": [],
        "attr_document_list_tbm": {},
        "attr_document_list_tbc": [],
        "file": "(binary)",
        "attachment_plugin":"", 
        "class": "Incident",
        "transaction_id": "Sourabh_gr-P1Sy3w",
        "c[menu]": "NewIncident",
        "operation": "apply_new"
        }
    
    create_url= "http://10.255.253.19/CATS/CATS/web/pages/UI.php"
    response = session.post(create_url, data=payload, verify=False,
                                allow_redirects=True)
    if response.status_code == 200:
            print(f'Login successful {create_url}')
        
           
    else:
            print(f'Login failed {create_url}')

def login():
     login_url = "http://10.255.253.19/CATS/CATS/web/pages/UI.php"

     payload={
            "auth_user": username,
            "auth_pwd": password,
            "login_mode": "form",
            "loginop": "login"
        }
     
     response = session.post(login_url, data=payload, verify=False,
                                allow_redirects=True)
     if response.status_code == 200:
            print(f'Login successful {login_url}')
            create_incident()
           
     else:
            print(f'Login failed {login_url}')


login()