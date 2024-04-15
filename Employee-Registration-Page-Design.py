import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Payroll Page Design")
root.config(bg="skyblue")
root.geometry("1000x600")
# Create a Canvas to hold the content
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)
canvas.config(bg = "white")

# Create a Frame inside the Canvas
main_frame = tk.Frame(canvas)
main_frame.grid(row=0, column=0, padx = 10, pady = 10, ipadx = 20, ipady = 20)
main_frame.config(bg = "white")

# Add a scrollbar to the Canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the Canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Bind the Canvas to the scrollbar
main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

headline = tk.Label(main_frame, text="SE-RI's EMPLOYEE PERSONAL INFORMATION", font=("Times New Roman", 30, "bold"))
headline.grid(row=0, column=0, padx=40, pady=40)
headline.config(bg = "white")
# Frames for sections
first_frame = tk.Frame(main_frame)
first_frame.grid(row=1, column=0, ipady = 20, ipadx = 20, padx = 20, pady = 20, sticky = "nsew")


second_frame = tk.Frame(main_frame)
second_frame.grid(row=2, column=0, ipady = 20, ipadx = 20, padx = 20, pady = 20, sticky = "nsew")

contact_info_headline = tk.Label(main_frame, text = "Contact Info", font = ("Arial",  15, "bold") )
contact_info_headline.grid(row = 3, column = 0, sticky = "w", padx = 20)
contact_info_headline.config(bg = "white")

third_frame = tk.Frame(main_frame)
third_frame.grid(row=4, column=0, ipady = 20, ipadx = 20, padx = 20, pady = 20, sticky = "nsew")

address_headline = tk.Label(main_frame, text = "Address", font = ("Arial",  15, "bold") )
address_headline.grid(row = 5, column = 0, sticky = "w", padx = 20)
address_headline.config(bg = "white")

fourth_frame = tk.Frame(main_frame)
fourth_frame.grid(row=6, column=0, ipady = 20, ipadx = 20, padx = 20, pady = 20, sticky = "nsew")

footer_buttons_frame = tk.Frame(main_frame)
footer_buttons_frame.grid(row = 7, column = 0, ipady = 20, ipadx=20, padx = 20, pady = 20, sticky = "w")
footer_buttons_frame.config(bg = "white")

save_button = tk.Button(footer_buttons_frame, text = "Save", width = 10)
save_button.grid(column = 0, row = 0, padx = 10, pady = 10 )
save_button.config(bg = "blue", fg = "white")
cancel_button = tk.Button(footer_buttons_frame, text = "Cancel", width = 10)
cancel_button.grid(column = 1, row = 0, padx = 10, pady = 10, ipadx = 5 )

image_path = "C:\\Users\\admin\\Pictures\\chaewonIcon.jpg"  # Change this to your image file path
image = Image.open(image_path)
image = image.resize((200,200))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

# Create image label
image_label = tk.Label(first_frame, image=photo)
image_label.image = photo  # Keep a reference to the image to avoid garbage collection
image_label.grid(row=1, column=0,  padx=20, pady = 20)

choosefile_button = tk.Button (first_frame, text = "Upload Profile Picture")
choosefile_button.grid(row = 2, column = 0, padx = 10, pady = 10 )

first_name_frame = tk.Frame(first_frame)
first_name_frame.grid(row=1, column=1, ipadx = 10)
first_name_label = tk.Label(first_name_frame, text="First Name: ")
first_name_label.grid(row=1, column=1, sticky="w")
first_name_entry = ttk.Entry(first_name_frame)
first_name_entry.grid(row=2, column=1)

middle_name_frame = tk.Frame(first_frame)
middle_name_frame.grid(row=1, column=2, ipadx = 10)
middle_name_label = tk.Label(middle_name_frame, text="Middle Name: ")
middle_name_label.grid(row=1, column=1, sticky="w")
middle_name_entry = ttk.Entry(middle_name_frame)
middle_name_entry.grid(row=2, column=1)

last_name_frame = tk.Frame(first_frame)
last_name_frame.grid(row=1, column=3, ipadx = 10)
last_name_label = tk.Label(last_name_frame, text="Last Name: ")
last_name_label.grid(row=1, column=1, sticky="w")
last_name_entry = ttk.Entry(last_name_frame)
last_name_entry.grid(row=2, column=1)

suffix_frame = tk.Frame(first_frame)
suffix_frame.grid(row=1, column=4, ipadx = 10)
suffix_label = tk.Label(suffix_frame, text="Suffix: ")
suffix_label.grid(row=1, column=1, sticky="w")
suffix_entry = ttk.Entry(suffix_frame)
suffix_entry.grid(row=2, column=1)

dob_frame = tk.Frame(first_frame)
dob_frame.grid(row=2, column=1, ipadx = 10)
dob_label = tk.Label(dob_frame, text="Date of Birth: ")
dob_label.grid(row=1, column=1, sticky="w")
dob_entry = DateEntry(dob_frame)
dob_entry.grid(row=2, column=1)

gender_frame = tk.Frame(first_frame)
gender_frame.grid(row=2, column=2, ipadx = 10)
gender_label= tk.Label(gender_frame, text="Gender: ")
gender_label.grid(row=1, column=1, sticky="w")
gender_entry= ttk.Combobox(gender_frame)
gender_entry.grid(row=2, column=1)

nationality_frame= tk.Frame(first_frame)
nationality_frame.grid(row=2, column=3, ipadx = 10)
nationality_label= tk.Label(nationality_frame, text="Nationality: ")
nationality_label.grid(row=1, column=1, sticky="w")
nationality_entry= ttk.Combobox(nationality_frame)
nationality_entry.grid(row=2, column=1)

civilstatus_frame = tk.Frame(first_frame)
civilstatus_frame.grid(row = 2, column = 4, ipadx = 10 )
civilstatus_label= tk.Label(nationality_frame, text="Civil Status: ")
civilstatus_label.grid(row=1, column=1, sticky="w")
civilstatus_entry= ttk.Combobox(nationality_frame)
civilstatus_entry.grid(row=2, column=1)

department_frame = tk.Frame(second_frame)
department_frame.grid(row=0, column=0, padx = 10, pady = 10)
department_label = tk.Label(department_frame, text="Department: ")
department_label.grid(row=0, column=0, pady=10, sticky = "w")
department_entry = tk.Entry(department_frame)
department_entry.grid(row=1, column=0, pady=10)

designation_frame = tk.Frame(second_frame)
designation_frame.grid(row=0, column=1, padx = 10, pady = 10)
designation_label= tk.Label(designation_frame, text="Designation: ")
designation_label.grid(row=0, column=0, pady=10, sticky = "w")
designation_entry = tk.Entry(designation_frame)
designation_entry.grid(row=1, column=0, pady=10)

qualifiedstatus_frame = tk.Frame(second_frame)
qualifiedstatus_frame.grid(row=0, column=2, padx = 10, pady = 10)
qualifiedstatus_label= tk.Label(qualifiedstatus_frame, text="Qualified Dep. Status: ")
qualifiedstatus_label.grid(row=0, column=0, pady=10, sticky = "w")
qualifiedstatus_comb = ttk.Combobox(qualifiedstatus_frame)
qualifiedstatus_comb.grid(row=1, column=0, pady=10)

employeestatus_frame= tk.Frame(second_frame)
employeestatus_frame.grid(row=1, column=0, padx = 10, pady = 10)
employeestatus_label= tk.Label(employeestatus_frame, text="Employee Status: ")
employeestatus_label.grid(row=0, column=0, pady=10, sticky = "w")
employeestatus_entry= tk.Entry(employeestatus_frame)
employeestatus_entry.grid(row=1, column=0, pady=10)

paydayte_frame = tk.Frame(second_frame)
paydayte_frame.grid(row=1, column=1, ipadx = 10)
paydayte_label= tk.Label(paydayte_frame, text="Paydate: ")
paydayte_label.grid(row=1, column=1, sticky="w")
paydayte_date= DateEntry(paydayte_frame)
paydayte_date.grid(row=2, column=1)

employeenumber_frame= tk.Frame(second_frame)
employeenumber_frame.grid(row=1, column=2, padx = 10, pady = 10)
employeenumber_label= tk.Label(employeenumber_frame, text="Employee Number: ")
employeenumber_label.grid(row=0, column=0, pady=10, sticky = "w")
employeenumber_entry= tk.Entry(employeenumber_frame)
employeenumber_entry.grid(row=1, column=0, pady=10)

contactno_frame = tk.Frame(third_frame)
contactno_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
contactno_label= tk.Label(contactno_frame, text="Contact No. ")
contactno_label.grid(row=0, column=0, pady=10, sticky = "w")
employeenumber_entry= tk.Entry(contactno_frame)
employeenumber_entry.grid(row=1, column=0, pady=10)

email_frame = tk.Frame(third_frame)
email_frame.grid(row = 0, column = 1, padx = 10, pady = 10)
email_label= tk.Label(email_frame, text="Email: ")
email_label.grid(row=0, column=0, pady=10, sticky = "w")
email_entry= tk.Entry(email_frame)
email_entry.grid(row=1, column=0, pady=10)

othersocmed_frame = tk.Frame(third_frame)
othersocmed_frame.grid(row = 1, column = 0, padx = 10, pady = 10)
othersocmed_label= tk.Label(othersocmed_frame, text="Other (Social Media)")
othersocmed_label.grid(row=0, column=0, pady=10, sticky = "w")
othersocmed_comb= ttk.Combobox(othersocmed_frame)
othersocmed_comb.grid(row=1, column=0, pady=10)

socmed_id_frame= tk.Frame(third_frame)
socmed_id_frame.grid(row = 1, column = 1, padx = 10, pady = 10)
socmed_id_label= tk.Label(socmed_id_frame, text="Social Media Account ID/No. ")
socmed_id_label.grid(row=0, column=0, pady=10, sticky = "w")
socmed_id_entry= tk.Entry(socmed_id_frame)
socmed_id_entry.grid(row=1, column=0, pady=10)


addr1_frame = tk.Frame(fourth_frame)
addr1_frame.grid(column=0, row=0, padx=10, pady=10)
addr2_frame = tk.Frame(fourth_frame)
addr2_frame.grid(column=0, row=1, padx=10, pady=10)
city_frame = tk.Frame(fourth_frame)
city_frame.grid(column=0, row=2, padx=10, pady=10)
sp_frame = tk.Frame(fourth_frame)
sp_frame.grid(column=1, row=2, padx=10, pady=10)
country_frame = tk.Frame(fourth_frame)
country_frame.grid(column=0, row=3, padx=10, pady=10, sticky="w")  # Align to the west
zipcode_frame = tk.Frame(fourth_frame)
zipcode_frame.grid(column=1, row=3, padx=10, pady=10)
picture_path_frame = tk.Frame(fourth_frame)
picture_path_frame.grid(column=0, row=4, pady=10)

addr1_label = tk.Label(addr1_frame, text="Address Line 1:")
addr1_label.grid(column=0, row=0, padx=10, sticky="w")
addr1_entry = tk.Entry(addr1_frame)
addr1_entry.grid(column=0, row=1, ipadx=50, pady=10)

addr2_label = tk.Label(addr2_frame, text="Address Line 2:")
addr2_label.grid(column=0, row=0, padx=10, sticky="w")
addr2_entry = tk.Entry(addr2_frame)
addr2_entry.grid(column=0, row=1, ipadx=50, pady=10)

city_label = tk.Label(city_frame, text="City/Municipality:")
city_label.grid(column=0, row=0, padx=10, sticky="w")
city_entry = tk.Entry(city_frame)
city_entry.grid(column=0, row=1, ipadx=50, pady=10)

sp_label = tk.Label(sp_frame, text="State/Province:")
sp_label.grid(column=0, row=0, padx=10, sticky="w")
sp_entry = tk.Entry(sp_frame)
sp_entry.grid(column=0, row=1, ipadx=50, pady=10)

country_label = tk.Label(country_frame, text="Country:")
country_label.grid(column=0, row=0, padx=10, sticky="w")
country_entry = ttk.Combobox(country_frame)
country_entry.insert(0, "Philippines")
country_entry.grid(column=0, row=1, padx=10, pady=10)

zipcode_label = tk.Label(zipcode_frame, text="Zip Code:")
zipcode_label.grid(column=0, row=0, padx=10, sticky="w")
zipcode_entry = tk.Entry(zipcode_frame)
zipcode_entry.grid(column=0, row=1, ipadx=50, pady=10)

picture_path_label = tk.Label(picture_path_frame, text="Picture Path:")
picture_path_label.grid(column=0, row=0, padx=10, sticky="w")
picture_path_entry = tk.Entry(picture_path_frame)
picture_path_entry.grid(column=0, row=1, ipadx=50, pady=10)

root.mainloop()
