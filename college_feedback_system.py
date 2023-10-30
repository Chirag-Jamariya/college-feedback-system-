import tkinter as tk
from tkinter import ttk
import mysql.connector
def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return conn

def submit_feedback():
    name = name_entry.get()
    registration_number = registration_entry.get()
    feedback_category = category_var.get()
    q1 = q1_entry.get()
    q2 = q2_entry.get()
    q3 = q3_entry.get()
    q4 = q4_entry.get()

    # Establish a connection to MySQL
    conn = connect_to_mysql()
    cursor = conn.cursor()

    if feedback_category == "Hostel":
        sql = "INSERT INTO hostel_feedback (name, registrationnumber, q1, q2, q3, q4) VALUES (%s, %s, %s, %s, %s, %s)"
    elif feedback_category == "Mess":
        sql = "INSERT INTO mess_feedback (name, registrationnumber, q1, q2, q3, q4) VALUES (%s, %s, %s, %s, %s, %s)"
    elif feedback_category == "Classroom":
        sql = "INSERT INTO classroom_feedback (name, registrationnumber, q1, q2, q3, q4) VALUES (%s, %s, %s, %s, %s, %s)"

    values = (name, registration_number, q1, q2, q3, q4) 
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def select_category(event):
    selected_category = category_var.get()
    if selected_category == "Hostel":
        q1_label.config(text="Is there any connectivity problem in hostel?")
        q2_label.config(text="Are bathroom and room getting cleaned every day?")
        q3_label.config(text="Is there any problem with devices in the room?")
        q4_label.config(text="Any additional feedback about the hostel?")
    elif selected_category == "Mess":
        q1_label.config(text="Is there any issue with the food in the mess?")
        q2_label.config(text="Is the mess clean and hygienic?")
        q3_label.config(text="Is there any problem with the service in the mess?")
        q4_label.config(text="Any additional feedback about the mess?")
    elif selected_category == "Classroom":
        q1_label.config(text="Are the classrooms well-equipped?")
        q2_label.config(text="Is there any issue with the teaching in the classroom?")
        q3_label.config(text="Is the classroom environment suitable for learning?")
        q4_label.config(text="Any additional feedback about the classrooms?")

root = tk.Tk()
root.title("College Feedback System")

# Name and Registration Number
name_label = tk.Label(root, text="Please enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

registration_label = tk.Label(root, text="Please enter your registration number:")
registration_label.pack()
registration_entry = tk.Entry(root)
registration_entry.pack()
# Feedback Category
category_var = tk.StringVar()
category_var.set("Hostel")  # Default category
category_label = tk.Label(root, text="Please choose the category for feedback:")
category_label.pack()
category_menu = ttk.Combobox(root, textvariable=category_var, values=["Hostel", "Mess", "Classroom"])
category_menu.bind("<<ComboboxSelected>>", select_category)
category_menu.pack()

# Feedback Questions
q1_label = tk.Label(root, text="Is there any connectivity problem in hostel?")
q1_label.pack()
q1_entry = tk.Entry(root)
q1_entry.pack()

q2_label = tk.Label(root, text="Are bathroom and room getting cleaned every day?")
q2_label.pack()
q2_entry = tk.Entry(root)
q2_entry.pack()

q3_label = tk.Label(root, text="Is there any problem with devices in the room?")
q3_label.pack()
q3_entry = tk.Entry(root)
q3_entry.pack()

q4_label = tk.Label(root, text="Any additional feedback?")
q4_label.pack()
q4_entry = tk.Entry(root)
q4_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_button.pack()

root.mainloop()