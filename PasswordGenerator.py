#program for sample Password
import random as r
from tkinter import *
from tkinter import scrolledtext
s=''
er='Enter only positive integers'
cc="ABCDEFGHIJK0123456789LMNOPQRabcdefghijklmnopqrstuvwxyzSTUVWXYZ!@#$%^&*_+%$"
res=[]
def on_enter_key1(event):
    # Shift focus to the second entry box
    b2.focus_set()

def out(k):
    output = Text(root, width=25, height=15)
    output.grid(row=4, column=1, padx=(5, 0), pady=(15, 0))
    output.insert(END, k)
    output.config(font=('arial', 12,'bold'), state=DISABLED)

def generate():
    global res, s
    try:
        s=''
        j = int(b1.get())
        n = int(b2.get())
        for i in range(1,j+1):
            res="Password #"+str(i)+" : "+str("".join(r.sample(cc,k=n)))+'\n'
            s=s+str(res)
            res=[]
        out(s)
    except ValueError:
        out(er)

root = Tk()
root.title('Password Generator')
root.geometry('500x550')
root.resizable(0,0)
root.configure(background='light grey')

lb1=Label(root, text="GENERATE PASSWORD", fg='grey', background='white')
lb1.grid(row=0, column=0,columnspan= 10, pady=(20,10),padx=(10,0))
lb1.config(font=('arial',30,'bold'))

lb2=Label(root, text="How many passwords : ", fg='black', background='light grey')
lb2.grid(row=1, column=0, pady=(20,10))
lb2.config(font=('arial',16))

b1=Entry(root, font=('arial',14),)
b1.grid(row=1, column=1)
b1.bind("<Return>", on_enter_key1)

lb3=Label(root, text="Length of Password : ", fg='black', background='light grey')
lb3.grid(row=2, column=0, pady=(20,10))
lb3.config(font=('arial',16))

b2=Entry(root, font=('arial',14))
b2.grid(row=2, column=1)
b2.bind("<Return>",lambda m:generate())

lb4=Label(root, text="Your Passwords : ", fg='black', background='light grey')
lb4.grid(row=4, column=0, pady=(20,10),sticky='n')
lb4.config(font=('arial',20))

btn=Button(root, text='Generate', command=generate)
btn.grid(row=3,column=1)
btn.config(font=('arial',12))

root.mainloop()
