
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")
# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root, text="How many dollars do you want?").pack()
