import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess

class EmailTemplateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Template Editor")

        # Create a scrolled text widget
        self.email_template_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.email_template_text.pack(padx=10, pady=10)

        # Create a button to trigger the email sending process
        send_button = tk.Button(root, text="Send Email", command=self.send_email)
        send_button.pack(pady=5)

        # Create a button to save the template to generate_messages.txt
        save_button = tk.Button(root, text="Save Template", command=self.save_template)
        save_button.pack(pady=5)
        
        # Create a button to clear the template
        clear_button = tk.Button(root, text="Clear Template", command=self.clear_template)
        clear_button.pack(pady=5)


    def send_email(self):
        # Retrieve the email template from the text widget
        email_template = self.email_template_text.get("1.0", tk.END)

        # Print or use the email template as needed
        
        print("Email Template:")
        print(email_template)
        print("the choosen email ids are :-")
        subprocess.run(["python", "read_emails.py"])
        
       
        
        print("Finally Sending Mail....")
        subprocess.run(["python", "mail.py"])
        

    def save_template(self):
        # Retrieve the email template from the text widget
        email_template = self.email_template_text.get("1.0", tk.END)

        # Save the template to the generate_messages.txt file
        with open('generate_messages.txt', 'w', encoding='utf-8') as file:
            file.write(email_template)
            
    def clear_template(self):
        # Clear the content of generate_messages.txt
        file_path = 'generate_messages.txt'
        if os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('')
            print("Template cleared successfully.")
        else:
            print("Template file not found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailTemplateGUI(root)
    root.mainloop()