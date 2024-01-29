import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from generating_message import generate_email_from_file  # Import the generate_email function
from read_emails import list_of_emails, list_of_names
import pandas as pd

# Your SMTP server configuration
smtp_server = "smtp.gmail.com" 
smtp_port = 587  # Change this to the appropriate port
sender_email = ''
sender_password = ""



def generate_email_from_file(file_path, recipient_names, company_name, website_url, discount_percentage, your_name, your_title):
    with open(file_path, 'r', encoding='utf-8') as file:
        email_template = file.read()

    email_contents = []
    for recipient_name in recipient_names:
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

def send_email(receiver_email, recipient_name, email_content):
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(email_content, 'plain'))

        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Elevate Your Learning Experience with Our New LMS Software!"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"Email sent to {recipient_name} ({receiver_email}) successfully!")

    except Exception as e:
        print(f"Error sending email to {recipient_name} ({receiver_email}): {str(e)}")

# Example usage:
if __name__ == "__main__":
    excel_file_path = 'emails.xlsx'
    df = pd.read_excel(excel_file_path)
    
    list_of_emails = df['Emails'].tolist()
    list_of_names = df['Names'].tolist()

    company_name = "ABC Learning Solutions"
    website_url = "https://www.abclearningsolutions.com"
    discount_percentage = 10
    your_name = "Durga"
    your_title = "CEO"

    for recipient_email, recipient_name in zip(list_of_emails, list_of_names):
        email_contents = generate_email_from_file(file_path="generate_messages.txt", recipient_names=[recipient_name],
                                                  company_name=company_name, website_url=website_url,
                                                  discount_percentage=discount_percentage,
                                                  your_name=your_name, your_title=your_title)

        send_email(recipient_email, recipient_name, email_contents[0])


