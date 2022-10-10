from tkinter import * 
from math import *
from math import pi
import os




def funcsqrttriangle():
    try:
        a = int(lbltriangle1.get())
        b = int(lbltriangle2.get())
        c = int(lbltriangle3.get())
        lbltriangle.config(text="Площадь= {}".format((a + b + c) / 2))
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")


def perimTriangle():
    try:
        a = int(lbltriangle1.get())
        b = int(lbltriangle2.get())
        c = int(lbltriangle3.get())
        lbltriangle11.config(text="Периметр= {}".format((a + b + c) / 2))
        return lambda z: (a + b + c) /2
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")

    

def funcasqrtrectangle():
    try:
        a = int(lblrectangle1.get())
        b = int(lblrectangle2.get())
        lblrectangle.config(text="Площадь= {}".format((a * b)))
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")



def funcPerimRectangle():
    try:
        a = int(lblrectangle1.get())
        b = int(lblrectangle2.get())
        lblrectangle11.config(text="Площадь= {}".format((a +b)*2))
        return lambda z: (a + b)*2
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")

def funccircleradius():
    try:
        r= int(lblcircle1.get())
        lblcircle1.config(text="Радиус= {}".format((pi * r ** 2)))
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")


def funccirclersqrt():
    try:
        r= int(lblcircle11.get())
        lblcircle11.config(text="Площадь= {}".format((pi*2*r)))
        return lambda z:(2*pi*r)
    except ValueError:
        lbltriangle.config(text="Ошибка введите цифры")







root = Tk()
root.title(u'Расчет площади фигур')
root.geometry('800x800')





lbltriangle= Label(text="Расчет площади треугольника:", font="Calibri 14")
lbltriangle.place(x=0,y=50)
lbltriangle1= Entry(width=5, font="Calibri 14")
lbltriangle1.place(x=270,y=50)
lbltriangle2= Entry(width=5, font="Calibri 14")
lbltriangle2.place(x=320,y=50)
lbltriangle3= Entry(width=5, font="Calibri 14")
lbltriangle3.place(x=370,y=50)



lbltriangle11= Label(text="Расчет периметра треугольника:", font="Calibri 14")
lbltriangle11.place(x=0,y=370)
lbltriangle1= Entry(width=5, font="Calibri 14")
lbltriangle1.place(x=270,y=370)
lbltriangle2= Entry(width=5, font="Calibri 14")
lbltriangle2.place(x=320,y=370)
lbltriangle3= Entry(width=5, font="Calibri 14")
lbltriangle3.place(x=370,y=370)




lblrectangle= Label(text="Расчет площади прямоугольника:", font="Calibri 14")
lblrectangle.place(x=0,y=150)
lblrectangle1= Entry(width=5, font="Calibri 14")
lblrectangle1.place(x=290,y=150)
lblrectangle2= Entry(width=5, font="Calibri 14")
lblrectangle2.place(x=340,y=150)

lblrectangle11= Label(text="Расчет площади прямоугольника:", font="Calibri 14")
lblrectangle11.place(x=0,y=440)
lblrectangle1= Entry(width=5, font="Calibri 14")
lblrectangle1.place(x=300,y=440)
lblrectangle2= Entry(width=5, font="Calibri 14")
lblrectangle2.place(x=350,y=440)



lblcircle1= Label(text="Расчет радиуса круга:", font="Calibri 14")
lblcircle1.place(x=0,y=220)
lblcircle1= Entry(width=5, font="Calibri 14")
lblcircle1.place(x=220,y=220)


lblcircle11= Label(text="Расчет площади  круга:", font="Calibri 14")
lblcircle11.place(x=0,y=500)
lblcircle11= Entry(width=5, font="Calibri 14")
lblcircle11.place(x=200,y=500)






btntriangle=Button(text="Рассчитать", font= "Calibri 10",command=funcsqrttriangle)
btntriangle.place(x=280,y=80)

btntriangle=Button(text="Рассчитать", font= "Calibri 10",command=funcasqrtrectangle)
btntriangle.place(x=280,y=180)

btncircle=Button(text="Рассчитать", font= "Calibri 10",command=funccircleradius)
btncircle.place(x=210,y=260)

btntriangle11=Button(text="Рассчитать", font= "Calibri 10",command=perimTriangle)
btntriangle11.place(x=300,y=400)

btnrectangle11=Button(text="Рассчитать", font= "Calibri 10",command=funcPerimRectangle)
btnrectangle11.place(x=320,y=470)

btncircle1=Button(text="Рассчитать", font= "Calibri 10",command=funccirclersqrt)
btncircle1.place(x=200,y=520)








root.mainloop()

