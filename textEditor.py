import sys
from tkinter import *
from tkinter import filedialog
#except:
 #   import Tkinter as tkinter
#import tkinter.tkFileDialog


root=Tk("Text Editor")
text=Text(root)
text.pack(side="bottom")

def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
button=Button(root, text="Save",bg="black",fg="white", command=saveas) 
button.pack(padx=10,pady=10,side="left")
def FontHelvetica():
    global text
    text.config(font="Helvetica")
def Times_new():
    global text
    text.config(font="Times")

def FontCourier():
    global text
    text.config(font="Courier")
def Font_size1():
	global text
	text.config(font=("",12))
	
def Font_size2():
	global text
	text.config(font=("",14))
	
def Font_size3():
	global text
	text.config(font=("",16))
	
def Font_size4():
	global text
	text.config(font=("",18))
	
font=Menubutton(root, text="Font",bg="black",fg="white") 
font.pack(padx=10,pady=10,side="left") 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu

size=Menubutton(root, text="Size",bg="black",fg="white") 
size.pack(padx=10,pady=10,side="left") 
size.menu=Menu(size, tearoff=0) 
size["menu"]=size.menu

helvetica=IntVar() 
courier=IntVar()
times=IntVar()
size1=IntVar()
size2=IntVar()
size3=IntVar()
size4=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)
font.menu.add_checkbutton(label="Times new", variable=times, 
command=Times_new)

size.menu.add_checkbutton(label="12", variable=size1, 
command=Font_size1)
size.menu.add_checkbutton(label="14", variable=size2, 
command=Font_size2)
size.menu.add_checkbutton(label="16", variable=size3, 
command=Font_size3)
size.menu.add_checkbutton(label="18", variable=size4, 
command=Font_size4)
root.mainloop()
