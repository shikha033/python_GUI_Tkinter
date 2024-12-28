from tkinter import *
root= Tk()  # small k

root.geometry("444x244")

# images  related widgets
photo=PhotoImage(file="img.png")
label1=Label(image=photo)
label1.pack()




root.mainloop() # IF NOT USED THEN WINDOW WILL FLUTTER