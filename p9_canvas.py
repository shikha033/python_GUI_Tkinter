from tkinter import *

root = Tk()
 # define the canvas size
'''canvas_width = 800 
canvas_height = 400'''
canvas_width = 1910
canvas_height = 1080

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("GUI")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - 
# corner of top left and corner of bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344,233,244,355)


root.mainloop()
