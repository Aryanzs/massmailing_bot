import subprocess
import tkinter as tk
from tkinter import scrolledtext

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main GUI")

        # Create buttons for options
        store_button = tk.Button(self.master, text="Store Gmail ID and Names in Excel", command=self.open_store_popup)
        store_button.pack(padx=20, pady=20)

        write_button = tk.Button(self.master, text="Write Email Message", command=self.open_write_popup)
        write_button.pack(padx=20, pady=20)

    def open_store_popup(self):
        # Run mailinggui.py using subprocess
        subprocess.run(["python", "Email_ids_store_gui.py"])
        # Add widgets for store Gmail ID in Excel pop-up

    def open_write_popup(self):
        subprocess.run(["python", "write_mail_gui.py"])

if __name__ == "__main__":
    root = tk.Tk()
    main_gui_instance = MainGUI(root)
    root.mainloop()








