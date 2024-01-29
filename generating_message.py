
import pandas as pd

def generate_email_from_file(file_path, recipient_names_file, company_name, website_url, discount_percentage, your_name, your_title):
    # Read the email content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        email_template = file.read()

    # Read recipient names from the Excel file
    recipient_names_df = pd.read_excel(recipient_names_file)
    recipient_names_list = recipient_names_df['Names'].tolist()

    # Iterate through recipient names and format the email template
    email_contents = []
    for recipient_name in recipient_names_list:
        formatted_email = email_template.format(
            recipient_name=recipient_name,
            company_name=company_name,
            website_url=website_url,
            discount_percentage=discount_percentage,
            your_name=your_name,
            your_title=your_title
        )
        email_contents.append(formatted_email)

    return email_contents

# Example usage:
file_path = 'generate_messages.txt'
recipient_names_file = 'emails.xlsx'  # Excel file with 'Names' column
company_name = "ABC Learning Solutions"
website_url = "https://www.abclearningsolutions.com"
discount_percentage = 10
your_name = "Durga"
your_title = "CEO"

email_contents = generate_email_from_file(file_path, recipient_names_file, company_name, website_url, discount_percentage, your_name, your_title)

# Print or use the 'email_contents' list as needed
for email_content in email_contents:
    print(email_content)



