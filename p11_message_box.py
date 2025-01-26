import tkinter as tk
from tkinter import messagebox

# Sample user data (username, password)
users = {
    "Naina": "6788",
    "Aditya": "8799",
    "Rehan": "3456"
}

# Function to verify the login credentials
def verify_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username exists and password matches
    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!") #2nd after !
    else:
        messagebox.showerror("Invalid Credentials", "Invalid ID or Password") # first argument in upper bar 2nd after cross

# Create the main window
root = tk.Tk()
root.title("Login System")

# Create and place labels and entry widgets for username and password
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")  # The 'show' option hides the password input
entry_password.pack(pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=verify_login)
login_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
