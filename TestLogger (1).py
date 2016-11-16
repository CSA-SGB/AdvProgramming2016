import getpass
import csv
import time
import os
import re
import hashlib
#import RPi.GPIO as io
from datetime import datetime
# io.setmode(io.BCM)
# pir_pin = 24
# power_pin = 27
# os.system("clear")
# io.setup(pir_pin, io.IN)
# io.setup(power_pin, io.OUT)
# io.output(power_pin, False)
# PERIOD_OF_TIME = 1800

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Creating the window
root = Tk()
root.title("Login")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def forgot_password(): #<--Function for Forgot Password dropdown option
    print("you forgot it!")

def doNothing():
    loginoffline()

#The Login Button
button = Button(root, text="Login", command=doNothing)
button.grid(column=2, row=3, sticky=W)

def loginoffline(*args):
    try:
        var=False
        f2 = open('hashd.csv', 'r')
        f = open("Logins.txt","a")
        students=csv.reader(f2)
        username=un.get()
        password=pw.get()
        username_rowgetnumyo=2 #change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
        password_rowgetnum=3 #master_row to the schools student list
        salt="gnuvie:^)"
        for hosts_rowyo in students:
            row = 1
            username=username.replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].zfill(4)
            #print(str(hashlib.sha256(username.encode("UTF-8")).hexdigest())+" username "+hosts_rowyo[username_rowgetnumyo]+"\n"+str(hashlib.sha256(password.encode("UTF-8")).hexdigest())+" password "+hosts_rowyo[password_rowgetnum])
            if(username=="displayport:^)"):
                exit()
            if (hashlib.md5((salt+username).encode("UTF-8")).hexdigest() == hosts_rowyo[username_rowgetnumyo]) & (hashlib.md5((salt+password).encode("UTF-8")).hexdigest() == hosts_rowyo[password_rowgetnum]):
                #print("Logging in.", end=""),
                #time.sleep(1)
                #print(".", end=""),
                #time.sleep(1)
                #print(".")
                #time.sleep(3)
                #os.system("clear")
                messagebox.showinfo("Login", "Logging in complete! Plug in your chromebook now;")
                f.write(username+" "+str(datetime.now())+"\n")
                f.close()
                start = time.time()
                while True :
                    # io.output(power_pin, True)
                    #
                    # if time.time() > start + PERIOD_OF_TIME:
                    #     print("POWER OFF")
                    #     time.sleep(1)
                    #     io.output(power_pin, False)
                    #     time.sleep(3)
                    #     loginoffline()
                    #     break
                    print("It works!")
                    var=True
                    break
                break
        if var==False:
            #print("Logging in.", end=""),
            #time.sleep(1)
            #print(".", end=""),
            #time.sleep(1)
            #print(".")
            #time.sleep(3)
            #os.system("clear")
            messagebox.showinfo("Login", "Error logging in, please try again!")
            #loginoffline()
        f2.close()
        f.close()
    except KeyboardInterrupt:
        print("Error, please try again! ")
        loginoffline()


#The Username entry box
un = StringVar()

ttk.Label(root, text="Username :").grid(column=1, row=1, sticky=W)
username_entry = ttk.Entry(root, textvariable=un)
username_entry.grid(column=2, row=1, sticky=W)


#The Password entry box
pw = StringVar()

ttk.Label(root, text="Password :").grid(column=1, row=2, sticky=W)
password_entry = ttk.Entry(root, textvariable=pw, show="*")
password_entry.grid(column=2, row=2, sticky=W)

#loginoffline()
