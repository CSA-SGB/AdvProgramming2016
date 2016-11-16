#Samantha Bennefield
#9/19/16
#Mr. Davis
#states.py

from tkinter import *
from tkinter import ttk

#GUI set up
root = Tk()
root.title("States")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


click = True

def name_click(event):       
    global click

    if click: #Only deletes the text the first time they click
        click = False
        name_entry.delete(0, "end")

def display(name, state_variable):
    ttk.Label(root, text="Hi "+self.name+" from "+self.state_variable).grid(column=2, row=4, sticky=(N, W, E, S))

#Name Entry
name = StringVar()
name.set("Enter your name")
name_entry = ttk.Entry(root, width=20, textvariable=name)
name_entry.grid(column=1, row=1, sticky=(W, E))
name_entry.bind('<FocusIn>', name_click)

#State ComboBox
state_variable=StringVar()
state = ttk.Combobox(root, textvariable=state_variable)
state.grid(column=2, row=3, sticky=(N, W, E, S))

state['values']=('Texas', 'Florida', 'Utah', 'Ohio', 'Oregon')

state.bind('<<ComboboxSelected>>', display)
