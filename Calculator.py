import tkinter as tk

new=cur=None

def getdigit(n):
    global new , cur
    try:
        cur = result_label['text']
        new = cur + str(n)
        result_label.config(text=new)
    except TypeError:
        result_label.config(text='do all clear')

def allclear():
    result_label.config(text='')

def getresult():
    global new
    try:
        result_label.config(text=(round(eval(new),2)))
    except TypeError:
        result_label.config(text=('put operators'))
    except SyntaxError:
        result_label.config(text=('check expression'))

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")
root.iconbitmap("calicon.ico")
root.geometry("280x400")
root.resizable(0,0)
root.configure(background='grey')

#button
btn7=tk.Button(root,text='7',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('7'))
btn7.grid(row=2,column=0)
btn7.config(font=('arial',16))

btn8=tk.Button(root,text='8',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('8'))
btn8.grid(row=2,column=1)
btn8.config(font=('arial',16))

btn9=tk.Button(root,text='9',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('9'))
btn9.grid(row=2,column=2)
btn9.config(font=('arial',16))

btn4=tk.Button(root,text='4',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('4'))
btn4.grid(row=3,column=0)
btn4.config(font=('arial',16))

btn5=tk.Button(root,text='5',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('5'))
btn5.grid(row=3,column=1)
btn5.config(font=('arial',16))

btn6=tk.Button(root,text='6',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('6'))
btn6.grid(row=3,column=2)
btn6.config(font=('arial',16))

btn1=tk.Button(root,text='1',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('1'))
btn1.grid(row=4,column=0)
btn1.config(font=('arial',16))

btn2=tk.Button(root,text='2',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('2'))
btn2.grid(row=4,column=1)
btn2.config(font=('arial',16))

btn3=tk.Button(root,text='3',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('3'))
btn3.grid(row=4,column=2)
btn3.config(font=('arial',16))

btnpl=tk.Button(root,text='+',background='black',fg='white' , width=5,height=2,command=lambda : getdigit("+"))
btnpl.grid(row=5,column=3)
btnpl.config(font=('arial',16))

btnmn=tk.Button(root,text='-',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('-'))
btnmn.grid(row=3,column=3)
btnmn.config(font=('arial',16))

btnml=tk.Button(root,text='*',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('*'))
btnml.grid(row=4,column=3)
btnml.config(font=('arial',16))

btndv=tk.Button(root,text='/',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('/'))
btndv.grid(row=2,column=3)
btndv.config(font=('arial',16))

btnc=tk.Button(root,text='AC',background='blue',fg='white' , width=5,height=2,command=lambda : allclear())
btnc.grid(row=1,column=0)
btnc.config(font=('arial',16))

btn0=tk.Button(root,text='0',background='black',fg='white' , width=5,height=2,command=lambda : getdigit(0))
btn0.grid(row=5,column=1)
btn0.config(font=('arial',16))

btnd=tk.Button(root,text='.',background='black',fg='white' , width=5,height=2,command=lambda : getdigit('.'))
btnd.grid(row=5,column=2)
btnd.config(font=('arial',16))

btnc=tk.Button(root,text='C',background='black',fg='white' , width=5,height=2,command=lambda :result_label.config(text=str(result_label['text'])[:len(str(result_label['text']))-1]))
btnc.grid(row=5,column=0)
btnc.config(font=('arial',16))

btn=tk.Button(root,text='=',background='orange',fg='white' , width=5,height=2,command=getresult)
btn.grid(row=1,column=3)
btn.config(font=('arial',16))

btn=tk.Button(root,text='(',background='black',fg='white' , width=5,height=2,command=lambda:getdigit('('))
btn.grid(row=1,column=1)
btn.config(font=('arial',16))

btn=tk.Button(root,text=')',background='black',fg='white' , width=5,height=2,command=lambda:getdigit(')'))
btn.grid(row=1,column=2)
btn.config(font=('arial',16))

# Display the result
#result = tk.StringVar()
result_label = tk.Label(root,text='',background='grey',fg='white')
result_label.grid(row=0, column=0, columnspan=10, pady=(20,10), sticky='w')
result_label.config(font=('arial',20,'bold'))

# Start the main loop
root.mainloop()