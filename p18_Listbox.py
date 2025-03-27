'''
from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i = 0
root = Tk()
root.geometry("455x233")
root.title("Listbox tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()

'''
# Another example---
from tkinter import *

def add_task():
    task = entry.get()
    if task != "":
        lbx.insert(END, task)
        entry.delete(0, END)

def remove_task():
    try:
        index = lbx.curselection()[0]  # Get the index of the selected task
        lbx.delete(index)
    except IndexError:
        pass

def clear_tasks():
    lbx.delete(0, END)

# Set up the main window
root = Tk()
root.geometry("400x300")
root.title("To-Do List")

# Create the Listbox
lbx = Listbox(root, height=10, width=40)
lbx.pack(pady=20)

# Create the Entry widget for typing tasks
entry = Entry(root, width=40)
entry.pack(pady=10)

# Create buttons to add, remove, and clear tasks
Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
Button(root, text="Remove Task", width=20, command=remove_task).pack(pady=5)
Button(root, text="Clear All Tasks", width=20, command=clear_tasks).pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
