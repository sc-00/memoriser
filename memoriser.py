import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

root = Tk()
root.geometry("400x300")
root.title("memoriser")
root.config(background = "orange")

def openfile():
    file = askopenfile(title = "open")
    listbox1.delete(0,END)
    items = file.readlines()
    for i in items:
        listbox1.insert(END,i.strip())

def savefile():
    file2 = asksaveasfile(defaultextension = ".txt")
    for i in listbox1.get(0,END):
        print(i.strip(),file = file2)
        listbox1.delete(0,END)

saveb = Button(root,text = "SAVE",command = savefile, width = 20)
saveb.place(x = 265,y = 0)

openb = Button(root,text = "OPEN",command = openfile, width = 20)
openb.place(x = 2,y = 0)

deleteb = Button(root,text = "DELETE",command = openfile, width = 20)
deleteb.place(x = 135,y = 0)

listbox1 = Listbox(root, width = 62, height = 11)
for i in range(1,10):
    listbox1.insert(END,str(i))
listbox1.place(x = 10, y = 90)

entrybox = Entry(root,width = 35)
entrybox.place(x =20,y = 40)

root.mainloop()