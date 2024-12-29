def login1():
    user_name = E1.get()
    l1.configure(text=f'Welcome, {user_name}!')
    welcome.tkraise()
    


# overlap--two frames
import tkinter as tk
root=tk.Tk()
container=tk.Frame(root,bg='red') # if we want to put anything inside this frame then  f1 will be parent
container.pack(fill="both",expand=True )
container.rowconfigure(0,weight=1)
container.columnconfigure(0,weight=1)

welcome=tk.Frame(container,bg="green")
l1=tk.Label(welcome, text='Welcome!!')
l1.pack(pady=100)
#welcome.pack(fill='both',expand=True) # cannot use pack here---as it will be in the container taking their divided section
# so we will use  grid---
welcome.grid(row=0,column=0,sticky='nsew')

login=tk.Frame(container,bg="yellow")
login.grid(row=0,column=0,sticky='nsew')

l2=tk.Label(login, text='Name')
l2.pack(pady=20)
E1=tk.Entry(login) # for taking user input
E1.pack(pady=20)
b1=tk.Button(login, text='Login',command=login1)
b1.pack()
root.mainloop()