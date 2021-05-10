from tkinter import *
from solution import solve
from gui import runing


finaal=Tk()
finaal.title("INDIA COVID PREDICTION")
finaal.geometry()
def do():
    solve()
def do2():
    runing()
f1=Button(finaal, text='Run The Model', command=do)
f1.pack()
f2=Button(finaal, text='get Prediction', command=do2)
f2.pack()

finaal.mainloop()
