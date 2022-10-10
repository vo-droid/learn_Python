from tkinter import *
from winsound import *
import winsound

class Note():
    def __init__(self, name, hz):
        self.name = name
        self.hz = hz

def playnote(note, duration=300):
        winsound.Beep(note.hz, duration)

C = Note("C", 700) # До
D = Note("D", 800) # Ре
E = Note("E", 850) # Ми
F = Note("F", 900) # Фа
G = Note("G", 950) # Соль


root = Tk()
root.title(u'Xylofone')
root.geometry('300x300')


def play1():
    return playnote(C, 600)

def play2():
    return  playnote(D, 800)

def play3():
    return playnote(E, 500)

def play4():
    return playnote(F, 400)

def play5():
    return playnote(G, 300)


def create_window():
    
    window=Toplevel(root)
    window.geometry("300x100")
    window.title("INFORMATION")
    window.resizable(0,0)
    lbl_author= Label(window,text="ПОД ГРИФОМ СЕКРЕТНО :)",font="Calibri 10")
    lbl_author.pack(side=TOP)


def create_windowset(event):
    create_window()



root.bind('<F1>',create_windowset)

btnDO= Button(text="do ", font= "Calibri 16",bg="red",command=play1)
btnDO.place(x=40,y=100)


btnRE= Button(text="re ", font= "Calibri 16",bg="green",command=play2)
btnRE.place(x=80,y=100)


btnMI= Button(text="mi ", font= "Calibri 16",bg="blue",command=play3)
btnMI.place(x=120,y=100)


btnFAA= Button(text="fa ", font= "Calibri 16",bg="green",command=play4)
btnFAA.place(x=160,y=100)

btnSOL= Button(text="sol ", font= "Calibri 16",bg="yellow",command=play5)
btnSOL.place(x=200,y=100)

root.mainloop()




