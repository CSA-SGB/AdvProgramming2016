#Samantha Bennefield
#9/16/16
#Mr. Davis
#Name/Age

from tkinter import *
from tkinter import ttk

#GUI set up
root = Tk()
root.title("no_yes")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

click = True
click2 = True

def name_click(event):       
    global click

    if click: #Only deletes the text the first time they click
        click = False
        name_entry.delete(0, "end")

def age_click(event):
    global click2

    if click2: #Only deletes the text the first time they click
        click2 = False
        age_entry.delete(0, "end")

def sel():
    print("")

def clear():
    pass

#Setting up the button
button = Button(root, text="Submit", command=clear)
button.grid(column=2, row=6, sticky=W)

var = IntVar()
R1 = Radiobutton(root, text="Male", variable=var, value=1, command=sel)
R1.grid(column=1, row=5, sticky=(W, E))
R2 = Radiobutton(root, text="Female", variable=var, value=2, command=sel)
R2.grid(column=2, row=5, sticky=(W, E))
R3 = Radiobutton(root, text="Other", variable=var, value=3, command=sel)
R3.grid(column=3, row=5, sticky=(W, E))

#Name Entry
name = StringVar()
name.set("Enter your name")
name_entry = ttk.Entry(root, width=20, textvariable=name)
name_entry.grid(column=1, row=1, sticky=(W, E))
name_entry.bind('<FocusIn>', name_click)


#Age Entry
age = StringVar()
age.set("Enter your age")
age_entry = ttk.Entry(root, width=20, textvariable=age)
age_entry.grid(column=1, row=2, sticky=(W, E))
age_entry.bind('<FocusIn>', age_click)
