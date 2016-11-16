#Samantha Bennefield
#9/12/16
#Mr. Davis
#DataBase1

from tkinter import *
from tkinter import ttk
import csv

def sel(state_variable): #This function could probably be removed
    print("")

def check_yes(): #This function could probably be removed
    if (yes.get()==1):
        print("")
    else:
        pass

def button_press(): #When the button is pressed it checks to see if everything is filled
    if first_name is not "":
        if last_name is not "":
            if var.get() >= 0:
                if state_variable is not "":
                    if yes.get()==1:
                        database = open('database.csv', 'w')
                        database.write(""+first_name.get()+last_name.get()+var.get()+state_variable.get())
    else:
        ttk.Label(root, text="Form must be complete to submit").grid(column=1, row=8, sticky=W)

#GUI set up
root = Tk()
root.title("Entry Form")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


#First name entry box
first_name = StringVar()
ttk.Label(root, text="First Name: ").grid(column=1, row=1, sticky=W)
first_entry = ttk.Entry(root, width=7, textvariable=first_name)
first_entry.grid(column=2, row=1, sticky=(W, E))

#Last name entry box
last_name = StringVar()
ttk.Label(root, text="Last Name: ").grid(column=1, row=2, sticky=W)
last_entry = ttk.Entry(root, width=7, textvariable=last_name)
last_entry.grid(column=2, row=2, sticky=(W, E))


#Radio Button
var = IntVar()
R1 = Radiobutton(root, text="Business", variable=var, value=1)
R1.grid(column=1, row=3, sticky=(W, E))
R2 = Radiobutton(root, text="Residence", variable=var, value=2)
R2.grid(column=2, row=3, sticky=(W, E))
R3 = Radiobutton(root, text="Other", variable=var, value=3)
R3.grid(column=3, row=3, sticky=(W, E))


#ComboBox
state_variable=StringVar()
ttk.Label(root, text="State: ").grid(column=1, row=4, sticky=W)
state = ttk.Combobox(root, textvariable=state_variable)
state.grid(column=2, row=4, sticky=(N, W, E, S))
state['values']= ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
state.bind('<<ComboboxSelected>>', sel)


#Check Box
yes = IntVar()
ttk.Label(root, text="Accept User Policy: ").grid(column=1, row=5, sticky=W)
yes_box = Checkbutton(root, text="yes", variable=yes, command=check_yes)
yes_box.grid(column=2, row=5, sticky=W)


#Button
button = Button(root, text="Submit", command=button_press)
button.grid(column=3, row=7, sticky=W)
#button.config(state='disabled') #Disabling the button at the start
