from tkinter import *
root= Tk()  # small k
from PIL import Image, ImageTk # before this install pillow

root.geometry("1920x1080")

# images  related widgets
photo=PhotoImage(file="img.png")
label1=Label(image=photo)
label1.pack()

# for jpgimages--
'''image2=Image.open("img2.jpeg")
photo2=ImageTk.PhotoImage(image2)
label2=Label(image=photo2)
label2.pack()'''


root.mainloop() # IF NOT USED THEN WINDOW WILL FLUTTER