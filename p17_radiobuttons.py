from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Radiobutton tutorial")

def order():

    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()

Button(text="Order Now", command=order).pack()
root.mainloop()