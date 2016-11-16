'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
10/31/16
Mr. Davis
Travel Log
'''

from tkinter import *
from tkinter import ttk

from tkinter import messagebox

root = Tk()
root.title("Travel Log")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


click = True

def desc_click(event):
    global click

    if click: #Only deletes the text the first time they click
        click = False
        entry.delete(0, "end")
        p["value"] = 50

def submit():
    p["value"] = 100

def clear():
    entryvar.set("")
    p["value"] = 0

def about():
    messagebox.showinfo(title="Travel Log", message='''Travel Log Version 1.0
A program to log the location of your trip and a description of the location''')

#Menu
root.option_add('*tearOff', FALSE)

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)

secondMenu = Menu(topMenu) 
topMenu.add_cascade(label="Help", menu=secondMenu)
secondMenu.add_cascade(label="About", command=about)


#List of countries and scrollbar
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N, S, E, W))

s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N, S))

l['yscrollcommand'] = s.set

ttk.Sizegrip().grid(column=20, row=20, sticky=(S, E))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)

countries=['Afghanistan', 'The Bahamas', 'Cambodia', 'Denmark', 'Ecuador', 'Finland', 'Greece', 'Hong Kong', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Malaysia', 'Nepal', 'Oman', 'Romania', 'Switzerland', 'Taiwan', 'United States of America', 'Venezuela', 'Yemen', 'Zimbabwe']

for i in countries:
    l.insert(END, i)


#Description Box
ttk.Label(root, text="Description").grid(column=0, row=8)

entryvar = StringVar()
entryvar.set("Type something!")
entry = ttk.Entry(root, width=20, textvariable=entryvar)
entry.grid(column=0, row=9, sticky=(W, E))
entry.bind('<FocusIn>', desc_click)


#Submit/Clear Buttons
subBtn = Button(root, text="Submit", command=submit)
subBtn.grid(column=3, row=0, padx=2, pady=2, sticky=W)

clearBtn = Button(root, text="Clear", command=clear)
clearBtn.grid(column=3, row=1, padx=2, pady=2, sticky=W)


#Progress Bar
p = ttk.Progressbar(root, orient=VERTICAL, length=200, mode='determinate', value=0)
p.grid(column=5, row=0, padx=2, pady=2, sticky=(N,S))
