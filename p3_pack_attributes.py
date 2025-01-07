from tkinter import *
root= Tk()  

root.geometry("444x233")
root.title("GUI USING TKINTER")

# IMPORTANT LABEL OPTIONS---

# text - adds the text
# bg- background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE 
#----relief=SUNKEN----for border styling

title_label = Label(text ='''It tells the story of Veronika, 
                   \n a 24-year-old Slovenian who appears to have everything in life going for her, 
                    \nbut who decides to kill herself.''', 
                    bg ="red", fg="white", padx=13, pady=94, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)

title_label.pack()

# Important Pack options
# anchor = nw , E, SE, S, SW, W, NW,SE ANY DIRECTION that background  will move  if not in all window
# side = top, bottom, left, right
# fill ---if not fill then it will take the size of the speified background
# ---- and if we slide he window it willl still be that size only not cover the whole window
# padx
# pady

title_label.pack(anchor ="sw", side = "top", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


