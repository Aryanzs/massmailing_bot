import pandas as pd

# Assuming the Excel file has a column named 'Email' containing email addresses
excel_file_path = 'emails.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Extract the 'Email' column and convert it to a Python list
list_of_emails = df['Emails'].tolist()
list_of_names = df['Names'].tolist()

# Display the list of emails
print("List of Emails:")
print(list_of_emails)
print(list_of_names)















