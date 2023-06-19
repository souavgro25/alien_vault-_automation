import win32com.client as win32

def send_email(subject, body, recipients, cc, account_name):
    outlook = win32.Dispatch("Outlook.Application")

    mail = outlook.CreateItem(0)
    mail.Subject = subject
    mail.Body = body
    mail.To = ";".join(recipients)
    mail.CC = ";".join(cc)

    # Find the desired account by name
    account = None
    for acc in outlook.Session.Accounts:
        if acc.DisplayName == account_name:
            account = acc
            break

    if account is None:
        print(f"Account '{account_name}' not found.")
        return

    mail._oleobj_.Invoke(*(64209, 0, 8, 0, account))  # Set the account for sending

    mail.Display()  # Display the email before sending (optional)
      # Send the email

    print("Email sent successfully.")

# Example usage
# subject = "test"
# body = "test"

# recipients = ["Sourabh.Grover@in2ittech.com"]
# cc = []
# account_name = "egov@in2ittech.co.za"

# send_email(subject, body, recipients, cc, account_name)
