#Samantha Bennefield
#9/6/16
#Mr. Davis
#rot 13 login

import codecs

from tkinter import *
from tkinter import ttk

def encode():
    un=open('names_pws.txt','r')
    en=open('rot13.txt','r+')
    for y in un:
        i=y.split()
        print(i)
        e=[]
        e.append(codecs.encode(i[0],'rot13'))
        e.append(codecs.encode(i[1],'rot13'))
        j=' '.join(e)
        print(j)
        en.write(j)
        en.write('\n')
    un.close()
    en.close()

#Tk code
root = Tk()
root.title("Login")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

username=StringVar()
password=StringVar()


#Getting username
user_entry=ttk.Entry(mainframe, width=7, textvariable=username)
user_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=username).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Username", relief=RAISED).grid(column=1, row=1, sticky=W)


#Getting password
pass_entry=ttk.Entry(mainframe, width=7, textvariable=password)
pass_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=username).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Password", relief=RAISED).grid(column=1, row=2, sticky=W)



#The button
ttk.Button(mainframe, text="Login", command=encode).grid(column=3, row=6, sticky=W)
