import win32com.client as win32
import openpyxl
import time

# from selcats import autocats

# open Excel file
wb = openpyxl.load_workbook('closing_mails.xlsx')
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

# # Search for emails in folder


response="Hi Team, \n \nPlease note that the server is active and we are proceeding on closing the ticket. \n \nThanks & Regards \nSourabh Grover \nEGov SOC team \n0110546980 \negov@in2ittech.co.za"

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
        
        
        reply = email.ReplyAll()
        reply.Body = response
        reply.Display()
        # reply.send()
            
    except:
        
       print(search +"is not working ")
