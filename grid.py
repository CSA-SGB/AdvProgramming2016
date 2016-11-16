#Samantha Bennefield
#10/6/16
#Mr. Davis
#Grid

from tkinter import *
from tkinter import ttk


def clear():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

 
#Creating the window
root = Tk()
root.title("Grid")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


#"File" Dropdown
topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)



#The Username entry
un = StringVar()

ttk.Label(root, text="Username :").grid(column=1, row=1, sticky=W)
username_entry = ttk.Entry(root, textvariable=un)
username_entry.grid(column=2, row=1, padx=10, pady=10)


#The Password entry
pw = StringVar()

ttk.Label(root, text="Password :").grid(column=1, row=2, sticky=W)
password_entry = ttk.Entry(root, textvariable=pw)
password_entry.grid(column=2, row=2, padx=10, pady=10)


#The Login Button
button = Button(root, text="Login", command=clear)
button.grid(column=2, row=3, columnspan=2, sticky='NSEW')
