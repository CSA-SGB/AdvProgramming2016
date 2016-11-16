#Samantha Bennefield
#9/7/16
#Mr. Davis
#Multiple Item Order Form

global item1_price
global item2_price
global item3_price
global item4_price
global shipping

from tkinter import *
from tkinter import ttk

def find_shipping(*args):
    global shipping
    ship_days_int = shipping_days.get()

    if ship_days_int == 2:
        shipping = 25
    elif ship_days_int == 3:
        shipping = 10
    elif ship_days_int == 5:
        shipping = 5
    else:
        shipping = 5

def calculate4(*args):
    global item4_price
    global item4_quantity
    item4_string = str(item1.get())
    item4_int = item4_quantity.get()
    
    try:
        file=open("inventory.txt", 'r')
        for line in file:
            if item4_string in line:
                location = line.index(item4_string)
                item4_price = line[location+1]
                break
            else:
                print("")

        if item4_int >= 4:
            item4_int=1
        else:
            item4_price=item4_price*item4_int

    except ValueError:
        pass

def calculate3(*args):
    global item3_price
    global item3_quantity
    item3_string = str(item3.get())
    item3_int = item3_quantity.get()
    
    try:
        file=open("inventory.txt", 'r')
        for line in file:
            if item3_string in line:
                location = line.index(item3_string)
                item3_price = line[location+1]
                break
            else:
                print("")

        if item3_int >= 4:
            item3_int = 1
        else:
            item3_price=item3_price*item3_int

    except ValueError:
        pass

def calculate2(*args):
    global item2_price
    global item2_quantity
    item2_string = str(item2.get())
    item2_int = item2_quantity.get()
    
    try:
        file=open("inventory.txt", 'r')
        for line in file:
            if item2_string in line:
                location = line.index(item2_string)
                item2_price = line[location+1]
                break
            else:
                print("")

        if item2_int >= 4:
            item2_int = 1
        else:
            item2_price=item2_price*item2_int

    except ValueError:
        pass

def calculate1(*args):
    global item1_price
    global item1_quantity
    item1_string = str(item1.get())
    item1_int = item1_quantity.get()
    
    try:
        file=open("inventory.txt", 'r')
        for line in file:
            if item1_string in line:
                location = line.index(item1_string)
                item1_price = line[location+1]
                break
            else:
                print("")

        if item1_int >= 4:
            item1_int = 1
        else:
            item1_price=item1_price*item1_int

    except ValueError:
        pass
        
        
def calculate(*args) :
    find_shipping()
    calculate1()
    calculate2()
    calculate3()
    calculate4()
    find_total()

def find_total(*args) :
    tax = .0825
    
    total = item1_price+item2_price+item3_price+item4_price+shipping*tax
    
    ttk.Label(mainframe, text=total).grid(column=2, row=10, sticky=W)
    


#GUI window set up
root = Tk()
root.title("Order Form")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


#Variable set up
item1 = StringVar()
item2 = StringVar()
item3 = StringVar()
item4 = StringVar()

item1_quantity = IntVar()
item2_quantity = IntVar()
item3_quantity = IntVar()
item4_quantity = IntVar()

shipping_days = IntVar()


#item & quantity entry 1
item_entry = ttk.Entry(mainframe, width=7, textvariable=item1)
item_entry.grid(column=3, row=3, sticky=(W, E))

num_entry = ttk.Entry(mainframe, width=7, textvariable=item1_quantity)
num_entry.grid(column=1, row=3, sticky=(W, E))


#item & quantity entry 2
item_entry = ttk.Entry(mainframe, width=7, textvariable=item2)
item_entry.grid(column=3, row=4, sticky=(W, E))

num_entry = ttk.Entry(mainframe, width=7, textvariable=item2_quantity)
num_entry.grid(column=1, row=4, sticky=(W, E))


#item & quantity entry 3
item_entry = ttk.Entry(mainframe, width=7, textvariable=item3)
item_entry.grid(column=3, row=5, sticky=(W, E))

num_entry = ttk.Entry(mainframe, width=7, textvariable=item3_quantity)
num_entry.grid(column=1, row=5, sticky=(W, E))


#item & quantity entry 4
item_entry = ttk.Entry(mainframe, width=7, textvariable=item4)
item_entry.grid(column=3, row=6, sticky=(W, E))

num_entry = ttk.Entry(mainframe, width=7, textvariable=item4_quantity)
num_entry.grid(column=1, row=6, sticky=(W, E))


#ship entry
ship_entry = ttk.Entry(mainframe, width=7, textvariable=shipping_days)
ship_entry.grid(column=1, row=8, sticky=(W, E))

ttk.Label(mainframe, text="").grid(column=2, row=7, sticky=(W, E))
ttk.Label(mainframe, text="Shipping").grid(column=3, row=8, sticky=W)


#the button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=11, sticky=W)


#extra labels
ttk.Label(mainframe, text="Item").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Quantity").grid(column=1, row=1, sticky=W)


ttk.Label(mainframe, text="Tax: 8.25%").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="Total: ").grid(column=1, row=10, sticky=W)
