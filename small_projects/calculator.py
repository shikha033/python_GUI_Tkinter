'''import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the input
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#2C3E50")  # Set background color of the window

# Entry widget to display the input/output
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#ECF0F1", fg="#34495E")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styling
button_style = {
    "width": 5,
    "height": 2,
    "font": ("Arial", 18),
    "relief": "solid",
    "borderwidth": 2,
    "fg": "white",  # White text color
}

# Button layout (including number buttons, operators, clear, and equals)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add them to the grid with custom styling
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear, **button_style, bg="#E74C3C")  # Red for 'C'
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate, **button_style, bg="#27AE60")  # Green for '='
    else:
        button = tk.Button(root, text=text, command=lambda value=text: on_button_click(value), **button_style, bg="#2980B9")  # Light blue for default buttons
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()'''
import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the input
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="white")  # Set background color of the window

# Entry widget to display the input/output
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="white", fg="#34495E")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styling
button_style = {
    "width": 5,
    "height": 2,
    "font": ("Arial", 18),
    "relief": "solid",
    "borderwidth": 2,
    "fg": "white",  # White text color
}

# Button layout (including number buttons, operators, clear, and equals)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add them to the grid with custom styling
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear, **button_style, bg="red")  # Red for 'C'
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate, **button_style, bg="green")  # Green for '='
    else:
        button = tk.Button(root, text=text, command=lambda value=text: on_button_click(value), **button_style, bg="blue")  # Light blue for default buttons
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
