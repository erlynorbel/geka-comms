import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("User Account Information")
root.geometry("1000x400")

info_label = tk.Label(root, text="User Account Information", font=("Arial", 16, "bold"))
info_label.grid(row=0, column=0, columnspan=2, pady=5)

# Load image
image_path = "C:\\Users\\dimay\\Downloads\\chaewon icon.jpg"  # Change this to your image file path
image = Image.open(image_path)
image = image.resize((200, 200))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

# Create image label
image_label = tk.Label(root, image=photo)
image_label.image = photo  # Keep a reference to the image to avoid garbage collection
image_label.grid(row=1, column=0, rowspan=4, padx=10)

# First row: First Name, Middle Name, Last Name, Suffix, Department
first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=1, column=1, sticky="w", padx=5)
first_name_entry = ttk.Entry(root)
first_name_entry.grid(row=1, column=2, sticky="ew", padx=5)

middle_name_label = tk.Label(root, text="Middle Name:")
middle_name_label.grid(row=1, column=3, sticky="w", padx=5)
middle_name_entry = ttk.Entry(root)
middle_name_entry.grid(row=1, column=4, sticky="ew", padx=5)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=5, sticky="w", padx=5)
last_name_entry = ttk.Entry(root)
last_name_entry.grid(row=1, column=6, sticky="ew", padx=5)

suffix_label = tk.Label(root, text="Suffix:")
suffix_label.grid(row=2, column=1, sticky="w", padx=5)
suffix_entry = ttk.Entry(root)
suffix_entry.grid(row=2, column=2, sticky="ew", padx=5)

department_label = tk.Label(root, text="Department:")
department_label.grid(row=2, column=3, sticky="w", padx=5)
department_entry = ttk.Entry(root)
department_entry.grid(row=2, column=4, sticky="ew", padx=5, columnspan=3)

# Second row: Designation, Username, Password
designation_label = tk.Label(root, text="Designation:")
designation_label.grid(row=3, column=1, sticky="w", padx=5)
designation_entry = ttk.Entry(root)
designation_entry.grid(row=3, column=2, sticky="ew", padx=5)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=3, column=3, sticky="w", padx=5)
username_entry = ttk.Entry(root)
username_entry.grid(row=3, column=4, sticky="ew", padx=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=5, sticky="w", padx=5)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=3, column=6, sticky="ew", padx=5)

# Third row: Confirm Password, User Type, User Status, Employee Number
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=4, column=1, sticky="w", padx=5)
confirm_password_entry = ttk.Entry(root, show="*")
confirm_password_entry.grid(row=4, column=2, sticky="ew", padx=5)

user_type_label = tk.Label(root, text="User Type:")
user_type_label.grid(row=4, column=3, sticky="w", padx=5)
user_type_entry = ttk.Entry(root)
user_type_entry.grid(row=4, column=4, sticky="ew", padx=5)

user_status_label = tk.Label(root, text="User Status:")
user_status_label.grid(row=4, column=5, sticky="w", padx=5)
user_status_entry = ttk.Entry(root)
user_status_entry.grid(row=4, column=6, sticky="ew", padx=5)

employee_number_label = tk.Label(root, text="Employee Number:")
employee_number_label.grid(row=5, column=1, sticky="w", padx=5)
employee_number_entry = ttk.Entry(root)
employee_number_entry.grid(row=5, column=2, sticky="ew", padx=5, columnspan=6)

# Fourth row: Update, Delete, Cancel buttons
update_button = ttk.Button(root, text="Update", style="Custom.TButton",)
update_button.grid(row=6, column=1, padx=5, pady=10, sticky="ew")

delete_button = ttk.Button(root, text="Delete")
delete_button.grid(row=6, column=2, padx=5, pady=10, sticky="ew")

cancel_button = ttk.Button(root, text="Cancel")
cancel_button.grid(row=6, column=3, padx=5, pady=10, sticky="ew")

root.mainloop()