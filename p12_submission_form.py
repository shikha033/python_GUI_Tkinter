import tkinter as tk
root = tk.Tk()
root.title("Submission Form System")
def submit_form(): 
# Retrieve input values 
    name = name_entry.get() 
    email = email_entry.get() 
    age = age_entry.get() 
    print(f"Name: {name}\nEmail: {email}\nAge: {age}") 
# Clear the fields after submission 
    name_entry.delete(0, tk.END) 
    email_entry.delete(0, tk.END) 
    age_entry.delete(0, tk.END)


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e") 
name_entry = tk.Entry(root) 
name_entry.grid(row=0, column=1, padx=10, pady=5) 
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e") 
email_entry = tk.Entry(root) 
email_entry.grid(row=1, column=1, padx=10, pady=5) 
tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e") 
age_entry = tk.Entry(root) 
age_entry.grid(row=2, column=1, padx=10, pady=5) 
# Add Submit Button 
submit_button = tk.Button(root, text="Submit", command=submit_form) 
submit_button.grid(row=3, column=0, columnspan=2, pady=10)



root.mainloop()