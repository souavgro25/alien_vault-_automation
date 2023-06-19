import requests

session = requests.Session()

url4 = "http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=details&class=Incident&id=4453"
headers4 = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Referer": "http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=details&class=Incident&id=4453&",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "cats-79814594a827a54e1d0b55fcf4f59432=rsdo2jv30pslv1l6hhcav669ra",
}

data4 = "auth_user=sourabh.grover&auth_pwd=Admin%402022&login_mode=form&loginop=login"

response = session.post(url4, headers=headers4, data=data4)

print(response.text)

incident="4278"

incide_url=f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_assign&class=Incident&id={incident}"

session.get(incide_url)

url = f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_assign&class=Incident&id={incident}"
headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryfA2WIiAj91BzdSf8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Referer": f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_assign&class=Incident&id={incident}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "cats-79814594a827a54e1d0b55fcf4f59432=kbmmh6bu8ge6skfke89q0a8uo2",
}

data = f'''------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="attr_team_id"

39
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="attr_agent_id"

56
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="id"

{incident}
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="class"

Incident
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="operation"

apply_stimulus
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="stimulus"

ev_assign
------WebKitFormBoundaryfA2WIiAj91BzdSf8
Content-Disposition: form-data; name="transaction_id"

Sourabh_gr-jXEzUU
------WebKitFormBoundaryfA2WIiAj91BzdSf8--'''

response = session.post(url, headers=headers, data=data)

print(response.text)

resolve_url=f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_resolve&class=Incident&id={incident}"

session.get(resolve_url)

url2 = f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_resolve&class=Incident&id={incident}"
headers2 = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7DLgiMznH6a1t5wp",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Referer": f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_resolve&class=Incident&id={incident}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "cats-79814594a827a54e1d0b55fcf4f59432=kbmmh6bu8ge6skfke89q0a8uo2",
}

data2 = f'''------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="attr_service_id"

5
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="attr_servicesubcategory_id"

25
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="attr_resolution_code"

assistance
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="attr_solution"

server is active
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="attr_Document_Create_resolved"

no
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="id"

{incident}
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="class"

Incident
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="operation"

apply_stimulus
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="stimulus"

ev_resolve
------WebKitFormBoundary7DLgiMznH6a1t5wp
Content-Disposition: form-data; name="transaction_id"

Sourabh_gr-CcRH43
------WebKitFormBoundary7DLgiMznH6a1t5wp--'''

response2 = session.post(url2, headers=headers2, data=data2)

print(response2.text)

close_url=f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_close&class=Incident&id={incident}"

session.get(close_url)

url3 = f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_close&class=Incident&id={incident}"
headers3 = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryABM6bJvGpRCHohHo",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Referer": f"http://10.255.253.19/CATS/CATS/web/pages/UI.php?operation=stimulus&stimulus=ev_close&class=Incident&id={incident}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "cats-79814594a827a54e1d0b55fcf4f59432=kbmmh6bu8ge6skfke89q0a8uo2",
}

data3 = f'''------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="attr_user_satisfaction"

1
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="attr_user_comment"

server is active hence we are closing the ticket
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="id"

{incident}
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="class"

Incident
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="operation"

apply_stimulus
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="stimulus"

ev_close
------WebKitFormBoundaryABM6bJvGpRCHohHo
Content-Disposition: form-data; name="transaction_id"

Sourabh_gr-px1GWe
------WebKitFormBoundaryABM6bJvGpRCHohHo--'''

response3 = session.post(url3, headers=headers3, data=data3)

print(response3.text)
