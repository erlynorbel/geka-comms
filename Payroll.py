import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Payroll Page Design")

# Create a Canvas to hold the content
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Create a Frame inside the Canvas
main_frame = tk.Frame(canvas)
main_frame.grid(row=1, column=0)

# Add a scrollbar to the Canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the Canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Bind the Canvas to the scrollbar
main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# headline
headline = tk.Label(main_frame, text="SE-RI's CHOICE PAYROLL", font=("Times New Roman", 30, "bold"))
headline.grid(row=0, column=1, padx=40, pady=40)

# leftframe
first_frame = tk.Frame(main_frame)
first_frame.grid(row=1, column=0)

# rightframe
second_frame = tk.Frame(main_frame)
second_frame.grid(row=1, column=1)

info_label = tk.Label(first_frame, text="EMPLOYEE BASIC INFO:", font=("Arial", 12, "bold"))
info_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")  # Align label to the left

image_path = "C:\\Users\\dimay\\Downloads\\chaewon icon.jpg"  # Change this to your image file path
image = Image.open(image_path)
image = image.resize((200, 200))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

# Create image label
image_label = tk.Label(first_frame, image=photo)
image_label.image = photo  # Keep a reference to the image to avoid garbage collection
image_label.grid(row=1, column=0,  padx=10, pady = 10)

# First row: Employee Number
employee_number = tk.Label(first_frame, text="Employee Number")
employee_number.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")  

employee_number_entry = ttk.Entry(first_frame)
employee_number_entry.grid(row=2, column=1, padx=0, sticky="e")  

# Second row: Search Employee
search_employee_label = tk.Label(first_frame, text="Search Employee")
search_employee_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")  

search_employee_button = ttk.Button(first_frame, text="Search")
search_employee_button.grid(row=3, column=1, padx=0, sticky="e") 

#Third row: Department 
department_label = tk.Label(first_frame, text="Department")
department_label.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w") 

department_entry = ttk.Entry(first_frame)
department_entry.grid(row=4, column=1, padx=0, sticky="e")  

#Fourth row: BASIC INCOME: 
basic_income_headline = tk.Label(first_frame, text = "BASIC INCOME: ", font=("Arial", 12, "bold"))
basic_income_headline.grid(row = 5, column = 0, padx = 10, pady = 30, sticky = "w")

#Fifth row: Rate/hour 
ratehour_label = tk.Label(first_frame, text="Rate / Hour:")
ratehour_label.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="w") 

ratehour_entry = ttk.Entry(first_frame)
ratehour_entry.grid(row=6, column=1, padx=0, sticky="e")  

#Sixth row: No. of hours / Cut Off
cutoffbasic_label = tk.Label(first_frame, text="No. of Hours / Cut Off:")
cutoffbasic_label.grid(row=7, column=0, padx=(10, 5), pady=5, sticky="w") 

cutoffbasic_entry = ttk.Entry(first_frame)
cutoffbasic_entry.grid(row=7, column=1, padx=0, sticky="e")  

#Seventh row: Income Cutoff
incomebasic_label = tk.Label(first_frame, text="Income / Cut Off:")
incomebasic_label.grid(row=8, column=0, padx=(10, 5), pady=5, sticky="w") 

incomebasic_entry = ttk.Entry(first_frame)
incomebasic_entry.grid(row=8, column=1, padx=0, sticky="e")  

#Eight row: HONORARIUM INCOME 
basic_income_headline = tk.Label(first_frame, text = "HONORARIUM INCOME: ", font=("Arial", 12, "bold"))
basic_income_headline.grid(row = 9, column = 0, padx = 10, pady = 30, sticky = "w")

#Ninth row: Rate/hour Honorarium
ratehourhono_label = tk.Label(first_frame, text="Rate / Hour")
ratehourhono_label.grid(row=10, column=0, padx=(10, 5), pady=5, sticky="w") 

ratehourhono_entry = ttk.Entry(first_frame)
ratehourhono_entry.grid(row=10, column=1, padx=0, sticky="e")

#Tenth row: Noofhours
cutoffhono_label = tk.Label(first_frame, text="No. of hours / Cut off:")
cutoffhono_label.grid(row=11, column=0, padx=(10, 5), pady=5, sticky="w") 

cutoffhono_entry = ttk.Entry(first_frame)
cutoffhono_entry.grid(row=11, column=1, padx=0, sticky="e")

#Eleventh row: Income cut off 
incomehono_label = tk.Label(first_frame, text="Income / Cut Off: ")
incomehono_label.grid(row=12, column=0, padx=(10, 5), pady=5, sticky="w") 

incomehono_entry = ttk.Entry(first_frame)
incomehono_entry.grid(row=12, column=1, padx=0, sticky="e")

#Twelve Row: HONORARIUM INCOME 
basic_income_headline = tk.Label(first_frame, text = "OTHER INCOME: ", font=("Arial", 12, "bold"))
basic_income_headline.grid(row = 13, column = 0, padx = 10, pady = 30, sticky = "w")

#Thirteenthrow: Income cut off 
rateother_label = tk.Label(first_frame, text="Rate / Hour")
rateother_label.grid(row=14, column=0, padx=(10, 5), pady=5, sticky="w") 

rateother_entry = ttk.Entry(first_frame)
rateother_entry.grid(row=14, column=1, padx=0, sticky="e")

#Fourteen row: Income cut off 
noofhoursother_label = tk.Label(first_frame, text="No of Hours / Cut Off: ")
noofhoursother_label.grid(row=15, column=0, padx=(10, 5), pady=5, sticky="w") 

noofhoursother_entry = ttk.Entry(first_frame)
noofhoursother_entry.grid(row=15, column=1, padx=0, sticky="e")

#Fifteenth row: Income cut off 
incomesother_label = tk.Label(first_frame, text="Income / Cut Off: ")
incomesother_label.grid(row=16, column=0, padx=(10, 5), pady=5, sticky="w") 

incomesother_entry = ttk.Entry(first_frame)
incomesother_entry.grid(row=16, column=1, padx=0, sticky="e")

# SUMMARY INCOME
basic_income_headline = tk.Label(first_frame, text = "SUMMARY INCOME: ", font=("Arial", 12, "bold"))
basic_income_headline.grid(row = 17, column = 0, padx = 10, pady = 30, sticky = "w")


grossincome_label = tk.Label(first_frame, text="GROSS INCOME: ")
grossincome_label.grid(row=18, column=0, padx=(10, 5), pady=5, sticky="w") 

grossincome_entry = ttk.Entry(first_frame)
grossincome_entry.grid(row=18, column=1, padx=0, sticky="e")


netincome_label = tk.Label(first_frame, text="NET INCOME: ")
netincome_label.grid(row=19, column=0, padx=(10, 5), pady=5, sticky="w") 

netincome_entry = ttk.Entry(first_frame)
netincome_entry.grid(row=19, column=1, padx=0, sticky="e")




first_name_label = netincome_label = tk.Label(second_frame, text="First Name: ")
netincome_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

firstname_entry = ttk.Entry(second_frame)
firstname_entry.grid(row=0, column=1, padx=0, sticky="e")


middle_name_label = tk.Label(second_frame, text="Middle Name: ")
middle_name_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")

middle_name_entry = ttk.Entry(second_frame)
middle_name_entry.grid(row=1, column=1, padx=0, sticky="e")

surname_label = tk.Label(second_frame, text="Surname: ")
surname_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

surname_entry = ttk.Entry(second_frame)
surname_entry.grid(row=2, column=1, padx=0, sticky="e")

middle_name_label = tk.Label(second_frame, text="Middle Name: ")
middle_name_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")

middle_name_entry = ttk.Entry(second_frame)
middle_name_entry.grid(row=1, column=1, padx=0, sticky="e")

surname_label = tk.Label(second_frame, text="Surname: ")
surname_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")

surname_entry = ttk.Entry(second_frame)
surname_entry.grid(row=2, column=1, padx=0, sticky="e")

civil_label = tk.Label(second_frame, text="Surname: ")
surname_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

civil_entry = ttk.Entry(second_frame)
civil_entry.grid(row=3, column=1, padx=0, sticky="e")

quali_label = tk.Label(second_frame, text="Qualified Dependents Status: ")
quali_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

quali_entry = ttk.Entry(second_frame)
quali_entry.grid(row=3, column=1, padx=0, sticky="e")

paydata_label = tk.Label(second_frame, text="Paydate: ")
paydata_label.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w")

paydata_entry= ttk.Entry(second_frame)
paydata_entry.grid(row=4, column=1, padx=0, sticky="e")

employeestatus_label = tk.Label(second_frame, text="Employee Status: ")
employeestatus_label.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="w")

employeestatus_entry= ttk.Entry(second_frame)
employeestatus_entry.grid(row=5, column=1, padx=0, sticky="e")

designation_label = tk.Label(second_frame, text="Designation: ")
designation_label.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="w")

designation_entry= ttk.Entry(second_frame)
designation_entry.grid(row=6, column=1, padx=0, sticky="e")

regular_deductions = tk.Label(second_frame, text="REGULAR DEDUCTIONS", font=("Arial", 12, "bold"))
regular_deductions.grid(row=7, column=0, pady=30, sticky="w")

sss_label = tk.Label(second_frame, text="SSS Contribution: ")
sss_label.grid(row=8, column=0, padx=(10, 5), pady=5, sticky="w")

sss_entry= ttk.Entry(second_frame)
sss_entry.grid(row=8, column=1, padx=0, sticky="e")

philhealth_label = tk.Label(second_frame, text="PhilHealth Contribution: ")
philhealth_label.grid(row=9, column=0, padx=(10, 5), pady=5, sticky="w")

philhealth_entry= ttk.Entry(second_frame)
philhealth_entry.grid(row=9, column=1, padx=0, sticky="e")

pagibig_label = tk.Label(second_frame, text="Pag-ibig Contribution: ")
pagibig_label.grid(row=10, column=0, padx=(10, 5), pady=5, sticky="w")

pagibig_entry= ttk.Entry(second_frame)
pagibig_entry.grid(row=10, column=1, padx=0, sticky="e")

incomtax_label = tk.Label(second_frame, text="Income Tax Contribution: ")
incomtax_label.grid(row=11, column=0, padx=(10, 5), pady=5, sticky="w")

incometax_entry= ttk.Entry(second_frame)
incometax_entry.grid(row=11, column=1, padx=0, sticky="e")

otherdeductions = tk.Label(second_frame, text="OTHER DEDUCTIONS", font=("Arial", 12, "bold"))
otherdeductions.grid(row=12, column=0, pady=30, sticky="w")

sssloan_label = tk.Label(second_frame, text="SSS Loan: ")
sssloan_label.grid(row=13, column=0, padx=(10, 5), pady=5, sticky="w")

sssloan_entry= ttk.Entry(second_frame)
sssloan_entry.grid(row=13, column=1, padx=0, sticky="e")

pagibigloan_label = tk.Label(second_frame, text="Pag-ibig Loan: ")
pagibig_label.grid(row=14, column=0, padx=(10, 5), pady=5, sticky="w")

pagibigloan_entry= ttk.Entry(second_frame)
pagibig_entry.grid(row=14, column=1, padx=0, sticky="e")

facultydepo_label= tk.Label(second_frame, text="Faculty Savings Deposit: ")
facultydepo_label.grid(row=15, column=0, padx=(10, 5), pady=5, sticky="w")

facultydepo_entry= ttk.Entry(second_frame)
facultydepo_entry.grid(row=15, column=1, padx=0, sticky="e")

facultysav_label = tk.Label(second_frame, text="Faculty Savings Loan: ")
facultysav_label.grid(row=16, column=0, padx=(10, 5), pady=5, sticky="w")

facultysav_entry= ttk.Entry(second_frame)
facultysav_entry.grid(row=16, column=1, padx=0, sticky="e")

salaryloan_label = tk.Label(second_frame, text="Salary Loan: ")
salaryloan_label.grid(row=17, column=0, padx=(10, 5), pady=5, sticky="w")

salaryloan_entry= ttk.Entry(second_frame)
salaryloan_entry.grid(row=17, column=1, padx=0, sticky="e")

otherloans_label = tk.Label(second_frame, text="Other Loans: ")
otherloans_label.grid(row=18, column=0, padx=(10, 5), pady=5, sticky="w")

otherloans_entry= ttk.Entry(second_frame)
otherloans_entry.grid(row=18, column=1, padx=0, sticky="e")

deduction_headline = tk.Label(second_frame, text = "DEDUCTION SUMMARY: ", font=("Arial", 12, "bold"))
deduction_headline.grid(row = 19, column = 0, padx = 10, pady = 30, sticky = "w")

totaldeduct_label = tk.Label(second_frame, text="Total Deductions: ")
totaldeduct_label.grid(row=20, column=0, padx=(10, 5), pady=5, sticky="w")

totaldeduct_entry= ttk.Entry(second_frame)
totaldeduct_entry.grid(row=20, column=1, padx=0, sticky="e")

buttons_frame = tk.Frame(second_frame)
buttons_frame.grid(row=21, column = 0, rowspan = 2, padx= 10, sticky = "e")

grossincom_button = tk.Button(buttons_frame, text = "GROSS INCOME")
grossincom_button.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

netincom_button = tk.Button(buttons_frame, text = "NET INCOME")
netincom_button.grid(row = 0, column = 1, sticky = "w", padx = 10, pady = 10)

save_button = tk.Button(buttons_frame, text = "SAVE")
save_button.grid(row = 0, column = 2, sticky = "w", padx = 10, pady = 10)

update_button = tk.Button(buttons_frame, text = "UPDATE")
update_button.grid(row = 0, column = 3, sticky = "w", padx = 10, pady = 10)

new_button = tk.Button(buttons_frame, text = "NEW")
new_button.grid(row = 0, column = 4, sticky = "w", padx = 10, pady = 10)
root.mainloop()
