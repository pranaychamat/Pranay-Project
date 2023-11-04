#Pyhton Program for Conversion of Temperature
from tkinter import *
f,c = 0,0

def outf(f):
    output = Text(root, width=15, height=1)
    output.grid(row=2, column=1, padx=(0, 0), pady=(10, 0))
    f=str(f)+'°F'
    output.insert(END, f)
    output.config(font=('arial', 16, 'bold'), state=DISABLED)

def outc(c):
    output = Text(root, width=15, height=1)
    output.grid(row=6, column=1, padx=(0, 0), pady=(10, 0))
    c=str(c)+'°C'
    output.insert(END, c)
    output.config(font=('arial', 16, 'bold'), state=DISABLED)

#Celcius to Fahrenheit
def cel_to_fahr():
    global c,f
    try:
        n=b1.get()
        c=float(n)
        f=round((c)*(9/5)+32,2)
        outf(f)
    except ValueError:
        output = Text(root, width=15, height=1)
        output.grid(row=2, column=1, padx=(0, 0), pady=(10, 0))
        output.insert(END, 'Enter Numbers')
        output.config(font=('arial', 16, 'bold'), state=DISABLED)


#Fahrenheit to Celcius
def fahr_to_cel():
    global c,f
    try:
        n=b2.get()
        f=float(n)
        c=round((f-32)*(5/9),2)
        outc(c)
    except ValueError:
        output = Text(root, width=15, height=1)
        output.grid(row=6, column=1, padx=(0, 0), pady=(10, 0))
        output.insert(END, 'Enter Numbers')
        output.config(font=('arial', 16, 'bold'), state=DISABLED)

#GUI for Temp. Conv.
root = Tk()
root.title('Temperature Convertor')
root.geometry('600x420')
root.resizable(0,0)
root.configure(background='#FFD39B')

lb1=Label(root, text="Celcius to Fahrenheit", fg='#8A360F', background='white')
lb1.grid(row=0, column=0,columnspan= 10, pady=(20,10),padx=(10,0))
lb1.config(font=('arial',30,'bold'))

lb2=Label(root, text="Enter Temp in Celcius :", fg='#8A360F', background='white')
lb2.grid(row=1, column=0)
lb2.config(font=('arial',16,'bold'))

lb3=Label(root, text="°C", fg='#8A360F', background='white')
lb3.grid(row=1, column=3)
lb3.config(font=('arial',16,'bold'))

b1=Entry(root,font=('arial',14),)
b1.grid(row=1, column=1)
b1.bind("<Return>",lambda n: cel_to_fahr())

b3=Button(root, text="Temp in Fahrenheit :", fg='#8A360F', background='orange',command=lambda : cel_to_fahr())
b3.grid(row=2, column=0,pady=(10,10))
b3.config(font=('arial',12,'bold'))

lb=Label(root, text="=========OR==========", fg='#8A360F', background='white')
lb.grid(row=3, column=0,columnspan=10, padx=(10,10),pady=(20,10))
lb.config(font=('arial',26,'bold'))

lb4=Label(root, text="Fahrenheit to Celcius", fg='#8A360F', background='white')
lb4.grid(row=4, column=0,columnspan=10, pady=(20,10),padx=(10,0))
lb4.config(font=('arial',30,'bold'))

lb5=Label(root, text="Enter Temp in Fahrenheit :", fg='#8A360F', background='white')
lb5.grid(row=5, column=0, padx=(10,10))
lb5.config(font=('arial',16,'bold'))

b2=Entry(root, font=('arial',14),)
b2.grid(row=5, column=1)
b2.bind("<Return>",lambda n:fahr_to_cel())

lb6=Label(root, text="°F", fg='#8A360F', background='white')
lb6.grid(row=5, column=3)
lb6.config(font=('arial',16,'bold'))

b4=Button(root, text="Temp in Celcius :", fg='#8A360F', background='orange', command=lambda : fahr_to_cel())
b4.grid(row=6, column=0, pady=(10,10))
b4.config(font=('arial',12,'bold'))

mainloop()