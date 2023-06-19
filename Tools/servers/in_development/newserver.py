import openpyxl

def create_host_ip_dictionary(file_path, sheet_name):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    # Select the sheet by name
    sheet = workbook[sheet_name]

    # Create an empty dictionary
    host_ip_dict = {}

    # Iterate over all rows until all columns are empty
    for row in sheet.iter_rows(values_only=True):
        if all(cell is None for cell in row):
            break

        # Get the values in the row as a list
        values = list(row)

        # Extract the hostname and IP address from the values list
        host = values[0]
        ip = values[1] if len(values) > 1 else None

        # Add the hostname and IP address to the dictionary
        if host is not None:
            host_ip_dict[host] = ip

    return host_ip_dict

# Example usage
file_path = "ticketsopen.xlsx"
sheet_name = "Sheet1"

host_ip_dictionary = create_host_ip_dictionary(file_path, sheet_name)
print("Host-IP Dictionary:")
for host, ip in host_ip_dictionary.items():
    print(f"Hostname: {host}, IP: {ip}")