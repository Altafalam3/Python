from tkinter import *

def add(a,b):
   return a+b

def sub(a,b):
   return a-b

def mult(a,b):
   return a*b

def div(a,b):
   return a/b

def mod(a,b):
   return a%b

def lcm(a,b):
   L=a if a>b else b
   while L <= a*b:
      if L%a==0 and L%b==0:
         return L
      L+=1

def hcf(a,b):
   H=a if a<b else b
   while H>=1:
      if a%H==0 and b%H==0:
         return H
      H-=1

operations = { 'ADD':add , 'ADDITION':add ,'SUM':add ,'PLUS':add,
           'SUM':sub , 'DIFFERENCE':sub, 'MINUS':sub,'SUBTRACT':sub,
           'LCM':lcm , 'HCF':hcf,
           'PRODUCT':mult,'MULTIPLICATION':mult,'MULTIPLY':mult,
           'DIVISION':div,'DIV':div,'DIVIDE':div,
           'MOD':mod , 'REMAINDER':mod ,'MODULUS':mod
}


win=Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg='lightskyblue')

l1 = Label(win,text='Hey, I am smarty .',width=20,padx=3)
l1.place(x=160,y=10)

l2 = Label(win,text='You can run any mathematical calculations here',padx=3)
l2.place(x=110,y=40)

l3 = Label(win,text='Enter the problem :',padx=3)
l3.place(x=160,y=100)

textin= StringVar()
e1 = Entry(win, width=40,textvariable=textin)
e1.place(x=100,y=130)

b1= Button(win, text='Click')
b1.place(x=210,y=160)

list = Listbox(win,width=30,height=3)
list.place(x=140,y=200)

win.mainloop()