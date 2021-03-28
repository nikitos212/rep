from tkinter import *
def fun1(event):
    a=[]
    a.append(int(e1.get()))
    a.append(int(e2.get()))
    a.append(int(e3.get()))
    a.append(int(e4.get()))
    k=0
    for i in range(1,a[0]):
        k+=i*a[1]
    if k==a[3]:
        lab["text"]+=str(a[0])
    else:
        lab["text"]+=str(((k-a[3])//(a[2])))
root=Tk()
t1=Label(text="Введите число корзин")
t2=Label(text="Введите вес настоящей монеты")
t3=Label(text="Введите разницу фальшивой и настоящей монет")
t4=Label(text="Введите общий вес")
e1=Entry()
e2=Entry()
e3=Entry()
e4=Entry()
b1=Button(text="Найти корзину с фальшивыми монетами...")
lab=Label(text="Ответ: ")
t1.pack()
e1.pack()
t2.pack()
e2.pack()
t3.pack()
e3.pack()
t4.pack()
e4.pack()
b1.pack()
b1.bind("<Button-1>",fun1)
lab.pack()
root.mainloop()
a=list(map(int,input().split()))

