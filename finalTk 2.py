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
11/7/16
Mr. Davis
Final Tk
'''

from tkinter import *
from tkinter import ttk

from tkinter import messagebox

from decimal import *

root = Tk()
root.title("Order Form")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


def retrieve(): #Function for Retrieve button
    try:
        file=open("Purchase Order.txt",'r')
        PO=POvar.get() #gets shipping entry
        for line in file.readlines(): #check line by line for it
            if PO==line:
                #.set() everything
                break
            else:
                messagebox.showinfo(title="Error", message="Purchase Order could not be found.")
                break
        
    except ValueError:
        pass


def write():
        file=open("Purchase Order.txt",'w')
        
        file.write(POvar.get())
        file.write("\n")
        file.write(FNvar.get())
        file.write("\n")
        file.write(LNvar.get())
        file.write("\n")
        file.write(streetvar.get())
        file.write("\n")
        file.write(streetvar2.get())
        file.write("\n")
        file.write(cityvar.get())
        file.write("\n")
        file.write(zipvar.get())
        file.write("\n")
        file.write(monthvar.get())
        file.write("\n")
        file.write(dayvar.get())
        file.write("\n")
        file.write(yearvar.get())
        file.write("\n")
        file.write(shipdaysvar.get())
        file.write("\n")
        file.write(statevar.get())

        messagebox.showinfo(title="Submit", message="Your purchase order has been submitted.")

        file.close

def submit(): #Function for Submit button
    try:
        file=open("Purchase Order.txt",'w')

        if len(POvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a P.O.")
        elif len(FNvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter first name.")
        elif len(LNvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter last name.")
        elif len(streetvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter street.")
        elif len(cityvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter city.")
        elif len(zipvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a zip code.")
        elif len(monthvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a month.")
        elif len(dayvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a day.")
        elif len(yearvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a year.")
        elif len(shipdaysvar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter shipping days.")
        elif len(statevar.get())==0:
            messagebox.showinfo(title="Missing field", message="Please enter a state.")
        else:
            write()
            
    except ValueError:
        pass


def checkPrice():
    price=int (pricevar.get())
    ship=int (shipdaysvar.get())
    tax=8.25

    if price<=0:
        messagebox.showinfo(title="Error", message="Invalid price")
    else:

        if ship==1:
            price=price+6
            price=price*8.25
            ttk.Label(mainframe, text="$"+price).grid(column=5, row=4, padx=4, pady=4)
        elif ship==2:
            price=price+4
            price=price*8.25
            ttk.Label(mainframe, text="$"+price).grid(column=5, row=4, padx=4, pady=4)
        elif ship==3:
            price=price+3
            price=price*8.25
            ttk.Label(mainframe, text="$"+price).grid(column=5, row=4, padx=4, pady=4)
        elif ship==4:
            price=price+2
            price=price*8.25
            ttk.Label(mainframe, text="$"+price).grid(column=5, row=4, padx=4, pady=4)
        elif ship==5:
            price=price+1
            price=price*8.25
            ttk.Label(mainframe, text="$"+price).grid(column=5, row=4, padx=4, pady=4)
        else:
            submit()



def checkPO():
    file=open("Purchase Order.txt",'r')
    PO=POvar.get() #gets shipping entry
    for line in file.readlines(): #check line by line for it
        if PO==line:
            messagebox.showinfo(title="Error", message="P.O. already exist.")
            file.close
            break
        else:
            checkPrice()


def about(): #Function for About dropdown option
    messagebox.showinfo(title="Order Form", message='''Order Form Version 1.0
How to use:
Submit: To submit a Purchase Order fill out all required fields and press submit
Retrieve: To retrieve a Purchase Order fill in the P.O. and press retrieve''')
    

#=====Dropdown Menu=====
root.option_add('*tearOff', FALSE)

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu) #File Dropdown
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)

secondMenu = Menu(topMenu) #Help Dropdown 
topMenu.add_cascade(label="Help", menu=secondMenu)
secondMenu.add_cascade(label="About", command=about)


#=====Entry Boxes and Labels=====

#PO Entry
ttk.Label(mainframe, text="P.O.").grid(column=0, row=1, padx=4, pady=4)

POvar = StringVar()
PO = ttk.Entry(mainframe, width=20, textvariable=POvar)
PO.grid(column=1, row=1, padx=4, pady=4, sticky=(W, E))

#First Name Entry
ttk.Label(mainframe, text="First Name").grid(column=0, row=2, padx=4, pady=4)

FNvar = StringVar()
FN = ttk.Entry(mainframe, width=20, textvariable=FNvar)
FN.grid(column=1, row=2, padx=4, pady=4, sticky=(W, E))

#Last Name Entry
ttk.Label(mainframe, text="Last Name").grid(column=0, row=3, padx=4, pady=4)

LNvar = StringVar()
LN = ttk.Entry(mainframe, width=20, textvariable=LNvar)
LN.grid(column=1, row=3, padx=4, pady=4, sticky=(W, E))

#Street Entry
ttk.Label(mainframe, text="Street").grid(column=0, row=4, padx=4, pady=4)

streetvar = StringVar()
street = ttk.Entry(mainframe, width=20, textvariable=streetvar)
street.grid(column=1, row=4, padx=4, pady=4, sticky=(W, E))

#Street Optional Entry
ttk.Label(mainframe, text="Street (Optional)").grid(column=0, row=5, padx=4, pady=4)

streetvar2 = StringVar()
street2 = ttk.Entry(mainframe, width=20, textvariable=streetvar2)
street2.grid(column=1, row=5, padx=4, pady=4, sticky=(W, E))

#City Entry
ttk.Label(mainframe, text="City").grid(column=2, row=6, padx=4, pady=4)

cityvar = StringVar()
city = ttk.Entry(mainframe, width=20, textvariable=cityvar)
city.grid(column=3, row=6, padx=4, pady=4, sticky=(W, E))

#Zip Code Entry
ttk.Label(mainframe, text="Zip").grid(column=0, row=7, padx=4, pady=4)

zipvar = StringVar()
zipcode = ttk.Entry(mainframe, width=20, textvariable=zipvar)
zipcode.grid(column=1, row=7, padx=4, pady=4, sticky=(W, E))

#Price Entry
ttk.Label(mainframe, text="Price").grid(column=4, row=1, padx=4, pady=4)

pricevar = StringVar()
price = ttk.Entry(mainframe, width=20, textvariable=pricevar)
price.grid(column=5, row=1, padx=4, pady=4, sticky=(W, E))

#Tax Labels
ttk.Label(mainframe, text="Tax").grid(column=4, row=2, padx=4, pady=4)

ttk.Label(mainframe, text="8.25").grid(column=5, row=2, padx=4, pady=4)

#Total Labels
ttk.Label(mainframe, text="Total").grid(column=4, row=4, padx=4, pady=4)

ttk.Label(mainframe, text="$0.00").grid(column=5, row=4, padx=4, pady=4)


#=====Combobox Entries=====

#Purchase Date Entry
ttk.Label(mainframe, text="Date of Purchase").grid(column=4, row=5, padx=4, pady=4)

monthvar = StringVar()
month = ttk.Combobox(mainframe, textvariable=monthvar, state='readonly')
month.grid(column=5, row=5, padx=4, pady=4)

month['values']=("January", "February", "March",
"April", "May", "June", "July", "August",
"September", "October", "November", "December")

dayvar = StringVar()
day = ttk.Combobox(mainframe, textvariable=dayvar, state='readonly')
day.grid(column=6, row=5, padx=4, pady=4)

day['values']=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")

yearvar = StringVar()
year = ttk.Combobox(mainframe, textvariable=yearvar, state='readonly')
year.grid(column=7, row=5, padx=4, pady=4)

year['values']=("2016", "2017", "2018", "2019", "2020", "2021", "2022",
"2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031",
"2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040")

#Shipping Days Entry
ttk.Label(mainframe, text="Shipping Days").grid(column=4, row=3, padx=4, pady=4)

shipdaysvar = StringVar()
shipdays = ttk.Combobox(mainframe, textvariable=shipdaysvar, state='readonly')
shipdays.grid(column=5, row=3, padx=4, pady=4)

shipdays['values']=("Overnight", "2 days", "3 days", "5 days", "7 days")

#State Entry
ttk.Label(mainframe, text="State").grid(column=0, row=6, padx=4, pady=4)

statevar = StringVar()
state = ttk.Combobox(mainframe, textvariable=statevar, state='readonly')
state.grid(column=1, row=6, padx=4, pady=4, sticky=(W))

state['values']=("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")


#=====Text Box=====
ttk.Label(mainframe, text="Description").grid(column=0, row=8, padx=4, pady=4)

desc = Text(mainframe, height=8, width=25)
desc.grid(column=1, row=8, padx=4, pady=4)


#=====Buttons=====
submit_btn = Button(mainframe, text="Submit", command=checkPO)
submit_btn.grid(column=7, row=8)

retrieve_btn = Button(mainframe, text="Retrieve", command=retrieve)
retrieve_btn.grid(column=7, row=9)

mainloop()
