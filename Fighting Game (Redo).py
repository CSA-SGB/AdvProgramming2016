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
11/2/16
Mr. Davis
Fighting Game (Redo)
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.title("Reduced Earthbound")
mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

ttk.Sizegrip().grid(column=20, row=20, sticky=(S, E))


#=====About Function for Toolbar=====
def about():
    messagebox.showinfo(title="Reduced Earthbound", message='''Reduced Earthbound Version 2.0

A basic fighting simulator based off of Earthbound.

Choose a character from each list to get started. Then choose an action to battle.
-Fight: A basic attack against the enemy
-Defend: Attempt to block the enemy's attack
-PSI: A magic attack against the enemy
-Run: Attempt to flee the battle''')


#=====Toolbar=====
root.option_add('*tearOff', FALSE)

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu) #File Dropdown
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)

secondMenu = Menu(topMenu) #Help Dropdown
topMenu.add_cascade(label="Help", menu=secondMenu)
secondMenu.add_cascade(label="About", command=about)


#=====Enemy Turn Function=====
def enemy_turn(): #Function for the enemy character to counter
    move_select = random.randint(1, 3)

    if move_select==1: #The enemy's "Fight" option
        damage = random.randint(1, atk2.get())
        success = random.randint(0, 1)
        message = ("")
        damagestr = str(damage)
        
        if success==0:
            message=("You take "+damagestr+" damage!")
            newhp=hp1.get()-damage
            hp1.set(newhp)
            HPmsg1.set(newhp)
            status1()
        else:
            message=("You dodge!")

        messagebox.showinfo(title="Fight", message="You're attacked! "+message)

    elif move_select==2: #The enemy's "Defend" option
        damage = random.randint(1, atk1.get())
        success = random.randint(0,1)
        message = ("")
        damagestr = str(damage)

        if success==0:
            message=('''You break through!
You deal '''+damagestr+" damage!")
            newhp=hp2.get()-damage
            hp2.set(newhp)
            HPmsg2.set(newhp)
            status2()
        else:
            message=("You're attack is blocked!")

        messagebox.showinfo(title="Defend", message="They defend! "+message)

    elif move_select==3: #The enemy's "PSI (magic)" option
        damage = random.randint(1, atk2.get())
        success = random.randint(0, 1)
        message = ("")
        damagestr = str(damage)
        
        if success==0:
            message=("You take "+damagestr+" damage!")
            newhp=hp1.get()-damage
            hp1.set(newhp)
            HPmsg1.set(newhp)
            status1()
        else:
            message=("You dodge!")

        messagebox.showinfo(title="PSI", message="You're attacked with magic! "+message)


#=====Win Function=====
def win_check(): #Function that runs between turns to check hp
    if hp1.get()<=0: #If your health hits 0
        loser=ttk.Label(mainframe, text=nm1.get()).grid(column=3, row=4, padx=2, pady=2)
        winner=ttk.Label(mainframe, text=nm2.get()).grid(column=3, row=2, padx=2, pady=2)

        #Disables the buttons once a winner is determined
        fight_btn.configure(state=DISABLED)
        defend_btn.configure(state=DISABLED)
        PSI_btn.configure(state=DISABLED)
        run_btn.configure(state=DISABLED)
        
    elif hp2.get()<=0: #If the enemy's health hits 0
        winner=ttk.Label(mainframe, text=nm1.get()).grid(column=3, row=2, padx=2, pady=2)
        loser=ttk.Label(mainframe, text=nm2.get()).grid(column=3, row=4, padx=2, pady=2)

        #Disables the buttons once a winner is determined
        fight_btn.configure(state=DISABLED)
        defend_btn.configure(state=DISABLED)
        PSI_btn.configure(state=DISABLED)
        run_btn.configure(state=DISABLED)
        
    else:
        enemy_turn()


#=====Fight Function=====
def fight():
    damage = random.randint(1, atk1.get())
    success = random.randint(0,1)
    message = ("")
    damagestr = str(damage)

    if success==0:
        message=("You deal "+damagestr+" damage!")
        newhp=hp2.get()-damage
        hp2.set(newhp)
        HPmsg2.set(newhp)
        status2()
    else:
        message=("You miss!")

    messagebox.showinfo(title="Fight", message="You attack! "+message)
    win_check()


#=====Defend Function=====
def defend():
    damage = random.randint(1, atk2.get())
    success = random.randint(0, 1)
    message = ("")
    damagestr = str(damage)

    if success==0:
        message=('''Your guard breaks!
You take '''+damagestr+''' damage!''')
        newhp=hp1.get()-damage
        hp1.set(newhp)
        HPmsg1.set(newhp)
        status1()
    else:
        message=("You block the attack!")
    
    messagebox.showinfo(title="Defend", message="You defend! "+message)
    win_check()


#=====PSI (Magic) Function=====
def psi():
    damage = random.randint(1, atk1.get())
    success = random.randint(0,1)
    message = ("")
    damagestr = str(damage)

    if success==0:
        message=("You deal "+damagestr+" damage!")
        newhp=hp2.get()-damage
        hp2.set(newhp)
        HPmsg2.set(newhp)
        status2()
    else:
        message=("You miss!")

    messagebox.showinfo(title="PSI", message="You cast a spell! "+message)
    win_check()


#=====Run Function=====
def run():
    messagebox.showinfo(title="Run Away", message="Can't escape!")
    win_check()


#=====Variables 1=====
HPmsg1 = StringVar()
HPmsg1.set('')

ATKmsg1 = StringVar()
ATKmsg1.set('')

DEFmsg1 = StringVar()
DEFmsg1.set('')

nm1 = StringVar() #=Name
hp1 = IntVar()
atk1 = IntVar()
def1 = IntVar()


#=====Variables 2=====
HPmsg2 = StringVar()
HPmsg2.set('')

ATKmsg2 = StringVar()
ATKmsg2.set('')

DEFmsg2 = StringVar()
DEFmsg2.set('')

nm2 = StringVar() #=Name
hp2 = IntVar()
atk2 = IntVar()
def2 = IntVar()


#=====Status Labels 1=====
def status1():
    ttk.Label(mainframe, text="HP").grid(column=1, row=5, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=HPmsg1.get()).grid(column=2, row=5)

    ttk.Label(mainframe, text="ATK").grid(column=1, row=6, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=ATKmsg1.get()).grid(column=2, row=6)

    ttk.Label(mainframe, text="DEF").grid(column=1, row=7, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=DEFmsg1.get()).grid(column=2, row=7)

status1()


#=====Status Labels 2=====
def status2():
    ttk.Label(mainframe, text="HP").grid(column=4, row=5, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=HPmsg2.get()).grid(column=5, row=5)
    
    ttk.Label(mainframe, text="ATK").grid(column=4, row=6, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=ATKmsg2.get()).grid(column=5, row=6)

    ttk.Label(mainframe, text="DEF").grid(column=4, row=7, sticky=(N, W, E, S))
    ttk.Label(mainframe, text=DEFmsg2.get()).grid(column=5, row=7)
    
status2()


#=====List Box 1=====
#Characters and their stats
charac_names1 = ('Ness', 'Paula', 'Jeff', 'Poo')
charac_hp1 = [165, 90, 105, 135]
charac_atk1 = [37, 26, 22, 44]
charac_def1 = [12, 8, 14, 37]

c_names1=StringVar(value=charac_names1) #<-- Used in Listbox

def show_stats1(*args):
    idxs = box1.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        box1.see(idx)
        name1=charac_names1[idx]
        healthPoints1=charac_hp1[idx]
        attack1=charac_atk1[idx]
        defense1=charac_def1[idx]
        
        HPmsg1.set(healthPoints1)
        ATKmsg1.set(attack1)
        DEFmsg1.set(defense1)

        nm1.set(name1) #For use in functions
        hp1.set(healthPoints1) #For use in functions
        atk1.set(attack1) #For use in functions
        def1.set(defense1) #For use in functions
        
        status1()

#The box itself
box1 = Listbox(mainframe, listvariable=c_names1, height=4, exportselection=0)
box1.grid(column=1, row=2, columnspan=2)

#Adding color to the box
for i in range(0,len(charac_names1),2):
    box1.itemconfigure(i, background='#f0f0ff')

box1.bind('<<ListboxSelect>>', show_stats1)


#=====List Box 2=====
#Characters and their stats
charac_names2 = ('Scalding Coffee Cup', 'Skelpion', 'Kraken', 'Giygas')
charac_hp2 = [175, 137, 200, 400]
charac_atk2 = [35, 31, 38, 40]
charac_def2 = [20, 23, 27, 40]

c_names2=StringVar(value=charac_names2) #<-- Used in Listbox

def show_stats2(*args):
    idxs = box2.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        box2.see(idx)
        name2=charac_names2[idx]
        healthPoints2=charac_hp2[idx]
        attack2=charac_atk2[idx]
        defense2=charac_def2[idx]
        
        HPmsg2.set(healthPoints2)
        ATKmsg2.set(attack2)
        DEFmsg2.set(defense2)

        nm2.set(name2) #For use in functions
        hp2.set(healthPoints2) #For use in functions
        atk2.set(attack2) #For use in functions
        def2.set(defense2) #For use in functions
        
        status2()


#The box itself
box2 = Listbox(mainframe, listvariable=c_names2, height=4, exportselection=0)
box2.grid(column=4, row=2, columnspan=2)

#Adding color to the box
for i in range(0,len(charac_names2),2):
    box2.itemconfigure(i, background='#f0f0ff')

box2.bind('<<ListboxSelect>>', show_stats2)


#=====Win/Lose Labels=====
ttk.Label(mainframe, text="Win").grid(column=3, row=1, padx=2, pady=2)
winner=ttk.Label(mainframe, text="----").grid(column=3, row=2, padx=2, pady=2)

ttk.Label(mainframe, text="Lose").grid(column=3, row=3, padx=2, pady=2)
loser=ttk.Label(mainframe, text="----").grid(column=3, row=4, padx=2, pady=2)


#=====Buttons=====
fight_btn = Button(root, text="Fight", command=fight)
fight_btn.grid(column=1, row=1)

defend_btn = Button(root, text="Defend", command=defend)
defend_btn.grid(column=2, row=1)

PSI_btn = Button(root, text="PSI (Magic)", command=psi)
PSI_btn.grid(column=1, row=2)

run_btn = Button(root, text="Run Away", command=run)
run_btn.grid(column=2, row=2)
