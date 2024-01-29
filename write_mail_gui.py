import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess
from tkinter import ttk, messagebox
from datetime import datetime



class EmailTemplateGUI:
    def __init__(self,master, root):
        self.master = master
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


                # Create a button to display stored templates
        display_templates_button = ttk.Button( text="Display Templates", command=self.display_templates)
        display_templates_button.pack(pady=10)
        
        # Create a button to clear the template
        clear_button = tk.Button(root, text="Clear Template", command=self.clear_template)
        clear_button.pack(pady=5)

        # Counter for canvas creation
        self.canvas_counter = 1
        self.templates_dict = {}


# to send email from the new one
    def send_email(self):
        # Retrieve the email template from the text widget
        email_template = self.email_template_text.get("1.0", tk.END)
        # Print or use the email template as needed
        self.save_intxt()
        print("Email Template:")
        print(email_template)
        print("the choosen email ids are :-")
        subprocess.run(["python", "read_emails.py"])   
        
        print("Finally Sending Mail....")
        subprocess.run(["python", "mail.py"])
      
    def save_intxt(self):
        # Retrieve the email template from the text widget
        email_template = self.email_template_text.get("1.0", tk.END)
        # Save the template to the generate_messages.txt file
        with open('generate_messages.txt', 'w', encoding='utf-8') as file:
            file.write(email_template)


# to send email by using temlate and modifying it
    def send_email2(self, email_content):
        self.save_txt()
        print("Email Template:")
        print(email_content)
        print("the choosen email ids are :-")
        subprocess.run(["python", "read_emails.py"])   
        print("Finally Sending Mail....")
        subprocess.run(["python", "mail.py"])
        messagebox.showwarning("Remainder", "Email sent successfully.")


    def save_txt(self):
        # Retrieve the email template from the text widget
        email_template = self.template_text.get("1.0", tk.END)
        # Save the template to the generate_messages.txt file
        with open('generate_messages.txt', 'w', encoding='utf-8') as file:
            file.write(email_template)



# /// to save the templates
    def save_template(self):
        # Retrieve the email template from the Text widget
        email_template = self.email_template_text.get("1.0", tk.END)
        # Generate a unique identifier (you can use a timestamp, UUID, etc.)
        unique_identifier = self.generate_unique_identifier()
        # Save the template to the file with the unique identifier (appending to the file)
        file_name = 'templates.txt'
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"\n--- Template {unique_identifier} ---\n")
            file.write(email_template)
        messagebox.showinfo("Success", f"Template appended to {file_name}")


# //creating a new canvas and dsplaying all the templates

    def display_templates(self):
        # Read templates from the file and display them in a new window
        file_name = 'templates.txt'
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                templates_content = file.readlines()

            # Create a new window to display templates
            display_window = tk.Toplevel(self.master)
            display_window.title("Stored Templates")

            # Initialize canvas and scrollbar
            canvas = tk.Canvas(display_window, width=400, height=600, borderwidth=2, relief="solid")
            canvas.pack(pady=10, side="left", fill="both", expand=True)

            scrollbar = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame to contain all the canvas widgets
            canvas_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

            # Iterate over templates and create canvas for each
            current_canvas = None
            for template in templates_content:
                if template.startswith('---'):
                    # Extract unique identifier from the template line
                    unique_identifier = template.split()[2]
                    # Create a new canvas
                    current_canvas = tk.Canvas(canvas_frame, width=380, height=100, borderwidth=2, relief="solid")
                    current_canvas.pack(pady=5, padx=5, fill="x")

                    # Add a button to the canvas
                    button = ttk.Button(current_canvas, text="Use this template", command=lambda canvas=current_canvas: self.button_callback(canvas))
                    button.pack(side="bottom")

                elif current_canvas is not None:
                    # Append template content to the current canvas
                    tk.Label(current_canvas, text=template, anchor="w", justify="left", wraplength=380).pack(pady=5, padx=5)

            # Configure the canvas scroll region
            canvas_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        except FileNotFoundError:
            messagebox.showwarning("Warning", "No templates found.")




    def button_callback(self, current_canvas):
        # Extract template content from the canvas
        template_content = ""
        for widget in current_canvas.winfo_children():
            if isinstance(widget, tk.Label):
                template_content += widget.cget("text") + "\n"

        # Create a new window for sending email with the template
        send_email_window = tk.Toplevel(self.master)
        send_email_window.title("Send Email")

        # Display the template content in a Text widget
        self.template_text = tk.Text(send_email_window, wrap="word", width=50, height=10)
        self.template_text.insert(tk.END, template_content)
        self.template_text.pack(padx=10, pady=10)

        # Add a button to send the email using the template
        send_email_button = ttk.Button(send_email_window, text="Send Email", command=lambda content=template_content: self.send_email2(content))
        send_email_button.pack(pady=10)
        


    def generate_unique_identifier(self):
        formatted_time = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return formatted_time



    def clear_template(self):
        # Clear the content of generate_messages.txt
        generate_messages_path = 'generate_messages.txt'
        self.clear_file(generate_messages_path)
        print("generate_messages.txt cleared successfully.")

        # Clear the content of templates.txt
        templates_path = 'templates.txt'
        self.clear_file(templates_path)
        print("templates.txt cleared successfully.")

    def clear_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('')
        else:
            print(f"{file_path} not found.")




if __name__ == "__main__":
    root = tk.Tk()
    app = EmailTemplateGUI(root,root)
    root.mainloop()
