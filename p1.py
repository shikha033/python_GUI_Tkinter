from tkinter import *
namra_root= Tk()  # small k

# GUI LOGIC ---

namra_root.geometry("644x434")
namra_root.minsize(200,100)

namra_root.maxsize(1200,900)

label1= Label(text = "This is used for labelling")
#have to pack then label will work
label1.pack()


namra_root.mainloop() # IF NOT USED THEN WINDOW WILL FLUTTER