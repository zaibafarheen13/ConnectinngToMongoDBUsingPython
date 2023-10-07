import tkinter as tk
from tkinter import messagebox
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["healthcare_database"]
collection = db["patients"]

def create_record():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    condition = condition_var.get()
    doctor = doctor_entry.get()
    data = {"name": name, "age": age, "gender": gender, "condition": condition, "doctor": doctor}
    
    try:
        inserted_record = collection.insert_one(data)
        messagebox.showinfo("Success", f"Patient record with ID {inserted_record.inserted_id} created successfully.")
        clear_inputs()
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def read_records():
    try:
        records = collection.find()
        record_text = ""
        for record in records:
            record_text += f"Name: {record['name']}, Age: {record['age']}, Gender: {record['gender']}, Condition: {record['condition']}, Doctor: {record['doctor']}\n"
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, record_text)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def update_record():
    existing_name = existing_name_entry.get()
    new_name = new_name_entry.get()
    new_age = new_age_entry.get()
    new_gender = new_gender_var.get()
    new_condition = new_condition_var.get()
    new_doctor = new_doctor_entry.get()
    
    query = {"name": existing_name}
    new_data = {"$set": {"name": new_name, "age": new_age, "gender": new_gender, "condition": new_condition, "doctor": new_doctor}}
    
    try:
        updated_record = collection.update_one(query, new_data)
        if updated_record.modified_count > 0:
            messagebox.showinfo("Success", "Patient record updated successfully.")
            clear_inputs()
        else:
            messagebox.showinfo("Info", "No records matched the query.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def delete_record():
    name_to_delete = delete_name_entry.get()
    query = {"name": name_to_delete}
    
    try:
        deleted_record = collection.delete_one(query)
        if deleted_record.deleted_count > 0:
            messagebox.showinfo("Success", "Patient record deleted successfully.")
            clear_inputs()
        else:
            messagebox.showinfo("Info", "No records matched the query.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def clear_inputs():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")  # Clear gender selection
    condition_var.set("")  # Clear condition selection
    doctor_entry.delete(0, tk.END)
    existing_name_entry.delete(0, tk.END)
    new_name_entry.delete(0, tk.END)
    new_age_entry.delete(0, tk.END)
    new_gender_var.set("")  # Clear new gender selection
    new_condition_var.set("")  # Clear new condition selection
    new_doctor_entry.delete(0, tk.END)
    delete_name_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Healthcare System")

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)
gender_label = tk.Label(root, text="Gender:")
gender_var = tk.StringVar(root)
gender_choices = ["Male", "Female", "Other"]
gender_dropdown = tk.OptionMenu(root, gender_var, *gender_choices)

condition_label = tk.Label(root, text="Condition:")
condition_var = tk.StringVar(root)
condition_choices = ["Condition 1", "Condition 2", "Condition 3"]
condition_dropdown = tk.OptionMenu(root, condition_var, *condition_choices)

doctor_label = tk.Label(root, text="Doctor:")
doctor_entry = tk.Entry(root)

create_button = tk.Button(root, text="Create Patient", command=create_record)
read_button = tk.Button(root, text="Read Patients", command=read_records)
clear_button = tk.Button(root, text="Clear Inputs", command=clear_inputs)

existing_name_label = tk.Label(root, text="Existing Name:")
existing_name_entry = tk.Entry(root)
new_name_label = tk.Label(root, text="New Name:")
new_name_entry = tk.Entry(root)
new_age_label = tk.Label(root, text="New Age:")
new_age_entry = tk.Entry(root)
new_gender_label = tk.Label(root, text="New Gender:")
new_gender_var = tk.StringVar(root)
new_gender_dropdown = tk.OptionMenu(root, new_gender_var, *gender_choices)
new_condition_label = tk.Label(root, text="New Condition:")
new_condition_var = tk.StringVar(root)
new_condition_dropdown = tk.OptionMenu(root, new_condition_var, *condition_choices)
new_doctor_label = tk.Label(root, text="New Doctor:")
new_doctor_entry = tk.Entry(root)

update_button = tk.Button(root, text="Update Patient", command=update_record)

delete_label = tk.Label(root, text="Delete:")
delete_name_label = tk.Label(root, text="Name to Delete:")
delete_name_entry = tk.Entry(root)
delete_button = tk.Button(root, text="Delete Patient", command=delete_record)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)
gender_label.grid(row=2, column=0)
gender_dropdown.grid(row=2, column=1)
condition_label.grid(row=3, column=0)
condition_dropdown.grid(row=3, column=1)
doctor_label.grid(row=4, column=0)
doctor_entry.grid(row=4, column=1)
create_button.grid(row=5, column=0)
read_button.grid(row=5, column=1)
clear_button.grid(row=5, column=2)

existing_name_label.grid(row=6, column=0)
existing_name_entry.grid(row=6, column=1)
new_name_label.grid(row=7, column=0)
new_name_entry.grid(row=7, column=1)
new_age_label.grid(row=8, column=0)
new_age_entry.grid(row=8, column=1)
new_gender_label.grid(row=9, column=0)
new_gender_dropdown.grid(row=9, column=1)
new_condition_label.grid(row=10, column=0)
new_condition_dropdown.grid(row=10, column=1)
new_doctor_label.grid(row=11, column=0)
new_doctor_entry.grid(row=11, column=1)
update_button.grid(row=12, column=1)

delete_label.grid(row=13, column=0)
delete_name_label.grid(row=14, column=0)
delete_name_entry.grid(row=14, column=1)
delete_button.grid(row=15, column=1)

result_text = tk.Text(root, width=60, height=10)
result_text.grid(row=16, column=0, columnspan=3)

root.mainloop()
