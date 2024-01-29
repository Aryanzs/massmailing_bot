import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

class EmailEntryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Entry GUI")
        
        # Create a Label and Entry for Email IDs and Names
        email_label = ttk.Label(master, text="Enter Email IDs and Names (comma-separated):")
        email_label.pack(pady=10)
        self.email_entry = ttk.Entry(master)
        self.email_entry.pack(pady=10)

        # Create a button to add Email IDs and Names to Excel
        add_button = ttk.Button(master, text="Add Email IDs and Names", command=self.add_emails_and_names)
        add_button.pack(pady=10)
        
        # Create a button to clear data in Excel
        clear_button = ttk.Button(master, text="Clear Data", command=self.clear_data)
        clear_button.pack(pady=10)

    def add_emails_and_names(self):
        # Retrieve Email IDs and Names from Entry widget
        entries_text = self.email_entry.get()

        # Check if entries are not empty
        if entries_text:
            # Split comma-separated entries and create a DataFrame
            entries_list = [entry.strip() for entry in entries_text.split(',')]
            entries_dict = {'Emails': [], 'Names': []}
            
            for entry in entries_list:
                email, name = entry.split('|')  # Assuming the format is email|name
                entries_dict['Emails'].append(email)
                entries_dict['Names'].append(name)

            df = pd.DataFrame(entries_dict)
            
            # Append Email IDs and Names to Excel file
            excel_file_path = 'emails.xlsx'
            try:
                # Try to read the existing Excel file
                existing_df = pd.read_excel(excel_file_path)
                df = pd.concat([existing_df, df], ignore_index=True)
            except FileNotFoundError:
                pass

            df.to_excel(excel_file_path, index=False)
            messagebox.showinfo("Success", "Email IDs and Names added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter Email IDs and Names.")

    def clear_data(self):
        # Clear data in Excel file
        excel_file_path = 'emails.xlsx'
        try:
            existing_df = pd.read_excel(excel_file_path)
            existing_df.drop(existing_df.index, inplace=True)
            existing_df.to_excel(excel_file_path, index=False)
            messagebox.showinfo("Success", "Data cleared successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No data to clear.")

if __name__ == "__main__":
    root = tk.Tk()
    email_entry_gui_instance = EmailEntryGUI(root)
    root.mainloop()
