from cgitb import text
from tkinter import *

window=Tk()

window.title('Converting Weights')

def weight():
    grams=float(kg_value.get()) * 1000
    pounds=float(kg_value.get()) * 2.20462
    ounces=float(kg_value.get()) * 35.274
    g.insert(END, grams)
    lb.insert(END, pounds)
    oz.insert(END, ounces)

label=Label(window, text="Kg")
label.grid(row=0, column=0)

b=Button(window, text="Convert", command=weight)
b.grid(row=0, column=2)

kg_value=StringVar()
kg=Entry(window, textvariable=kg_value)
kg.grid(row=0, column=1)

g=Text(window, height=1, width=20)
g.grid(row=1, column=0)

lb=Text(window, height=1, width=20)
lb.grid(row=1, column=1)

oz=Text(window, height=1, width=20)
oz.grid(row=1, column=2)

window.mainloop()