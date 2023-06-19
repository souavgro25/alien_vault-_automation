import win32com.client as win32
import openpyxl
import time

# from selcats import autocats

# open Excel file
wb = openpyxl.load_workbook('followups.xlsx')
sheet = wb.active
# Outlook details
outlook = win32.Dispatch('Outlook.Application')
namespace = outlook.GetNamespace('MAPI')

# Find email account by name
for acc in outlook.Session.Accounts:
    if acc.DisplayName == 'egov@in2ittech.co.za':
        account = acc
        inbox_folder = namespace.Folders(account.DeliveryStore.DisplayName).Folders('Inbox')
        break

# Search for emails in folder
cats=[]
rest=[]
check1="We kindly request you to validate and give updates on the below-mentioned Incident"
response="Hi Team, \n \nGentle Reminder!! \n\nWe kindly request you to validate and give updates on the below-mentioned Incident. \n \nThanks & Regards \nSourabh Grover \nEGov SOC team \n0110546980 \negov@in2ittech.co.za"
check2 = "This server is still showing disconnected in our SIEM console, Please check and provide us an update"
for search in sheet['A']:
    if search.value is None:
        break
    try :
        search =search.value
        search=str(search)
        
        search_filter = "@SQL=\"urn:schemas:httpmail:subject\" like '%" + search + "%'"
        emails = inbox_folder.Items.Restrict(search_filter)
        emails.Sort('[ReceivedTime]', True)
        email = emails.GetFirst()
        
        if check1.lower() in email.Body.lower() or check2  in email.Body:
            reply = email.ReplyAll()
            reply.Body = response
            # reply.Display()
            reply.send()
            
            print(search)
            
            cats.append(search)
        else :
            rest.append(search)
        time.sleep(30)
    except:
        
       print(search +"is not working ")
print(cats)
# autocats(cats)
print(rest)