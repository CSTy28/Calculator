# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:54:48 2020

@author: bigfe
"""

from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title('Scientific Calculator')
root.configure(background = 'gray')
root.resizable(width=False, height = False)
root.geometry('468x568+0+0')

calc = Frame(root)
calc.grid()

menubar = Menu(calc)


#====================MENU FUNCTIONS==============================
def isExit():
    isExit = tkinter.messagebox.askyesno('Scientific Calculator', 'Do you want to exit?')
    if(isExit == True):
        root.destroy()
        return
    
def scientific():
    root.resizable(width=False, height = False)
    root.geometry('944x568+0+0')
    
def standard():
    root.resizable(width=False, height = False)
    root.geometry('468x568+0+0')

#==========================MENU==========================
# Adding Menu items and commands 
filemenu = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = filemenu) 
filemenu.add_command(label ='Standard', command = standard) 
filemenu.add_command(label ='Scientific', command = scientific) 
filemenu.add_separator()
filemenu.add_command(label ='Exit', command = isExit) 

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Cut', command = None)
editmenu.add_command(label = 'Copy', command = None)
editmenu.add_command(label = 'Paste', command = None)

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = helpmenu)
helpmenu.add_command(label = 'ViewHelp', command = None)

#==========================NUMBER BUTTONS==========================

#============TEXTBOX===============
equ = 5
textbox = Entry(calc, font = ('arial',20, 'bold'), bd = 30, width = 27, bg = 'gray', justify=RIGHT)
textbox.grid(row = 0, column = 0, columnspan = 4, pady=1 )
#This is what is shown in the entry box
textbox.insert(0, 0)

def numEnter(num):
    if(textbox.get() == '0'): 
        textbox.delete(0, END)
    current = textbox.get()
    textbox.delete(0, END)
    ak = textbox.insert(0, str(current) + str(num))
      
    
def clear():
    
    textbox.delete(0, END)
    textbox.insert(0, 0)
    
def allClear():
    global f_num
    textbox.delete(0, END)
    textbox.insert(0, 0)
    f_num = 0
    
def add():
    firstnum = textbox.get()
    global f_num
    global op
    f_num = float(firstnum)
    op = 'addition'
    textbox.delete(0, END)
    
def subtract():
    firstnum = textbox.get()
    global f_num
    global op
    f_num = float(firstnum)
    op = 'subtraction'
    textbox.delete(0, END)
    
def multiply():
    firstnum = textbox.get()
    global f_num
    global op
    f_num = float(firstnum)
    op = 'multiplication'
    textbox.delete(0, END)
    
def divide():
    firstnum = textbox.get()
    global f_num
    global op
    f_num = float(firstnum)
    op = 'division'
    textbox.delete(0, END)
    
def pm():
    firstnum = textbox.get()
    global f_num
    f_num = float(firstnum)
    textbox.delete(0, END)
    textbox.insert(0, -(f_num))
    
def squareroot():
    firstnum = textbox.get()
    global f_num
    global op
    
    f_num = float(firstnum)
    textbox.delete(0, END)
    textbox.insert(0, math.sqrt(f_num))
    
def pi():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    textbox.insert(0, float(math.pi))
    global frst
    frst = textbox.get()
    
def twopi():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    textbox.insert(0, float(2*(math.pi)))
    global frst
    frst = textbox.get()
    
def e():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    textbox.insert(0, float(math.e))
    global frst
    frst = textbox.get()
    
def cos():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.cos(math.radians((frst)))))
    
def cosh():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.cosh(math.radians((frst)))))
    
def acosh():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.asinh(math.radians((frst)))))
    
def sin():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.sin(math.radians((frst)))))
    
def sinh():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.sinh(math.radians((frst)))))
    
def asinh():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.asinh(math.radians((frst)))))
    
def tan():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.tan(math.radians((frst)))))
    
def tanh():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.tanh(math.radians((frst)))))
    
def exp():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.exp(math.radians((frst)))))
    
def mod():
    firstnum = textbox.get()
    global f_num
    global op
    f_num = float(firstnum)
    op = 'modulus'
    textbox.delete(0, END)
    
def log():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.log(frst)))
    
def log2():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.log2(frst)))
    
def log10():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.log10(frst)))
    
def log1p():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.log1p(frst)))
    
def lgamma():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.lgamma(frst)))
    
def expm1():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.expm1(frst)))
    
def deg():
    if(textbox.get() == 0): 
        textbox.delete(0, END)
    global frst
    frst = float(textbox.get())
    textbox.insert(0, float(math.degrees(frst)))

        
    
    
def equal():
    if (op == 'addition'):
        second_num = textbox.get()
        textbox.delete(0, END)
        global ans
        ans = (f_num + float(second_num))
        print(type(ans))
        textbox.insert(0, ans)
        
    elif (op == 'subtraction'):
        second_num = textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, f_num - float(second_num))
        
    elif (op == 'multiplication'):
        second_num = textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, f_num * float(second_num))
        
    elif (op == 'division'):
        second_num = textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, f_num / float(second_num))
        
    elif (op == 'modulus'):
        second_num = textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, f_num % float(second_num))
            
    


#==========================STANDARD BUTTONS==========================
btn7 = Button(calc, text='7', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(7)).grid(row=2, column=0, pady=1, padx=1)

btn8 = Button(calc, text='8', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(8)).grid(row=2, column=1, pady=1, padx=1)

btn9 = Button(calc, text='9', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(9)).grid(row=2, column=2, pady=1, padx=1)

btn4 = Button(calc, text='4', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(4)).grid(row=3, column=0, pady=1, padx=1)

btn5 = Button(calc, text='5', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(5)).grid(row=3, column=1, pady=1, padx=1)

btn6 = Button(calc, text='6', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(6)).grid(row=3, column=2, pady=1, padx=1)

btn1 = Button(calc, text='1', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(1)).grid(row=4, column=0, pady=1, padx=1)

btn2 = Button(calc, text='2', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(2)).grid(row=4, column=1, pady=1, padx=1)

btn3 = Button(calc, text='3', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(3)).grid(row=4, column=2, pady=1, padx=1)

btn0 = Button(calc, text='0', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  command=lambda: numEnter(0)).grid(row=5, column=0, pady=1, padx=1)

btnClear = Button(calc, text=chr(67), width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=lambda: clear()).grid(row=1, column=0, pady=1, padx=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=lambda: allClear()).grid(row=1, column=1, pady=1)

btnsqrt = Button(calc, text='√', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=squareroot).grid(row=1, column=2, pady=1)

btnadd = Button(calc, text='+', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command= add).grid(row=1, column=3, pady=1)

btnsub = Button(calc, text='-', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=subtract).grid(row=2, column=3, pady=1)

btnmult = Button(calc, text='×', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=multiply).grid(row=3, column=3, pady=1)

btndiv = Button(calc, text='÷', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=divide).grid(row=4, column=3, pady=1)

btnequal = Button(calc, text='=', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=equal).grid(row=5, column=3, pady=1)

btnpm = Button(calc, text='±', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=pm).grid(row=5, column=2, pady=1)

btndot = Button(calc, text='.', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=lambda: numEnter(".")).grid(row=5, column=1, pady=1)

'''btnzero = Button(calc, text='0', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543').grid(row=5, column=0, pady=1)'''


#==========================SCIENTIFIC===============================
btnpi = Button(calc, text='π', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=pi).grid(row=1, column=4, pady=1, padx=1)

btncos = Button(calc, text='cos', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=cos).grid(row=1, column=5, pady=1)

btntan = Button(calc, text='tan', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=tan).grid(row=1, column=6, pady=1)

btnsin = Button(calc, text='sin', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=sin).grid(row=1, column=7, pady=1)

btn2pi = Button(calc, text='2π', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=twopi).grid(row=2, column=4, pady=1)


btncosh = Button(calc, text='cosh', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=cosh).grid(row=2, column=5, pady=1)

btntanh = Button(calc, text='tanh', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=tanh).grid(row=2, column=6, pady=1)

btnsinh = Button(calc, text='sinh', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=sinh).grid(row=2, column=7, pady=1)


btnlog = Button(calc, text='log', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=log).grid(row=3, column=4, pady=1)

btnexp = Button(calc, text='Exp', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=exp).grid(row=3, column=5, pady=1)

btnmod = Button(calc, text='Mod', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=mod).grid(row=3, column=6, pady=1)

btne = Button(calc, text='e', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=e).grid(row=3, column=7, pady=1)

btnlog2 = Button(calc, text='log2', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=log2).grid(row=4, column=4, pady=1)

btndeg = Button(calc, text='deg', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=deg).grid(row=4, column=5, pady=1)

btnacosh = Button(calc, text='acosh', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=acosh).grid(row=4, column=6, pady=1)

btnasinh = Button(calc, text='asinh', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=asinh).grid(row=4, column=7, pady=1)

btnlog10 = Button(calc, text='log10', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=log10).grid(row=5, column=4, pady=1)

btnlog1p = Button(calc, text='log1p', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=log1p).grid(row=5, column=5, pady=1)

btnexpm1 = Button(calc, text='expm1', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=expm1).grid(row=5, column=6, pady=1)

btnlgamma = Button(calc, text='lgamma', width=6, height = 2, font = ('arial',20, 'bold'), bd=4, 
                  bg='#f7b543', command=lgamma).grid(row=5, column=7, pady=1)



#Display the menu
root.config(menu=menubar)

#Open the window
root.mainloop()