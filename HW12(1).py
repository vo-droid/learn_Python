
from operator import le
from tkinter import * 
from tkinter import messagebox as mb


 

def select_gender():
    level=level_var.get()
    if level==1:
        print("Male")
    elif level==2:
        print("Female")

def func1():
    try:
        x = int(entry1.get())
        z= int(110)
        label.config(text="Ваш идельный вес  {}".format(x - z))
    except ValueError:
        label.config(text="Ошибка введите цифры")

def func():
    try:
        x = int(entry1.get())
        z= int(100)
        label.config(text="Ваш идельный вес  {}".format(x - z))
    except ValueError:
        label.config(text="Ошибка введите цифры")


    
    
    
    


root = Tk()
root.title(u'Норма веса ')
root.geometry('600x600')

level_var=IntVar()
Label(root,text="Выберете пол").pack()
Radiobutton(root,text="Мужской",variable=level_var,value=1,command=select_gender).pack()
Radiobutton(root,text="Женский",variable=level_var,value=2,command=select_gender).pack()

lblentry1= Label(text="Введите рост:", font="Calibri 14")
lblentry1.place(x=80,y=250)

lblentry2= Label(text="Введите вес:", font="Calibri 14")
lblentry2.place(x=80,y=200)

label = Label(root, text=" Рассчитаем ваш вес")
label.pack()


entry1 = Entry(width=14,text="Введите рост:",font="Calibri 14")
entry1.place(x=240,y=200)

entry2 = Entry(width=14,text="Bведите вес:",font="Calibri 14")
entry2.place(x=240,y=250)

btnAuth= Button(text="Рассчитать для мужчины ", font= "Calibri 16", command = func)
btnAuth.place(x=400,y=200)

btnAuth1= Button(text="Рассчитать для женщины ", font= "Calibri 16", command = func)
btnAuth1.place(x=400,y=250)


 



root.mainloop()


