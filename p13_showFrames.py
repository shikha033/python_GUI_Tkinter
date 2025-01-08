import tkinter as tk
root = tk.Tk()

def show_frame(frame):
    frame.tkraise()
# Create a container for the frames
container = tk.Frame(root) 
container.pack(fill="both", expand=True)
# Create frames (screens)
screen1 = tk.Frame(container, bg="lightblue")
screen2 = tk.Frame(container, bg="lightgreen")
# Add frames to the container
for frame in (screen1, screen2):
    frame.grid(row=0, column=0, sticky="nsew")
# Screen 1 content
tk.Label(screen1, text="Welcome to Screen 1", font=("Arial", 16), bg="lightblue").pack(pady=20)
tk.Button(screen1, text="Go to Screen 2", command=lambda: show_frame(screen2)).pack()
# Screen 2 content
tk.Label(screen2, text="This is Screen 2", font=("Arial", 16), bg="lightgreen").pack(pady=20)
tk.Button(screen2, text="Back to Screen 1", command=lambda: show_frame(screen1)).pack()
# Show the first screen initially
show_frame(screen1)
root.mainloop()