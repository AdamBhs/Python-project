from tkinter import *
from tkinter import ttk,messagebox
import turtle as tur
import tools
import colorsys as cs
import time

def draw():
    x=cbox.get()
    if x=="graph1":
        fiz.goto(x=0,y=0)
        colors=["red","dark red"]
        fiz.speed(0)
        for i in range(400):
            fiz.forward(i+1)
            fiz.right(89)
            fiz.pencolor(colors[i%2])

    elif x=="graph2":
        fiz.goto(x=0,y=0)
        fiz.width(2)
        fiz.speed(0)
        for j in range(25):
            for i in range(15):
                fiz.color(cs.hsv_to_rgb(i/15,j/25,1))
                fiz.right(90)
                fiz.circle(100-j*4,90)
                fiz.left(90)
                fiz.circle(100-j*4,90)
                fiz.right(180)
                fiz.circle(50,24)
    elif x=="graph3":
        fiz.goto(x=0,y=0)
        fiz.width(4)
        fiz.speed(0)
        def square(x):
            for i in range(3):
                fiz.forward(x)
                fiz.left(90)
            fiz.forward(x)
        for j in range(20):
            for i in range(10):
                fiz.color(cs.hsv_to_rgb(i/10,1-j/20,1))
                fiz.right(135)
                square(100-j*4)
                fiz.right(135)
                fiz.circle(50,36)
def delete():
    canvas.delete("all")

root=Tk()
root.title("Turtle Console")
root.geometry("850x500")
root.config(bg='white')


canvas=Canvas(root,bg="blue",width=550,height=500)
canvas.grid(row=0,columnspan=6)

graphs=["graph1","graph2","graph3","graph4"]

cbox=ttk.Combobox(root, values=graphs)
cbox.config(font=("arial",12,"underline"),width=14)
cbox.set("Take option")
cbox.grid(row=1,column=4)
cbox['state']="readonly"
cbox.place(x=620,y=200)
fiz=tur.RawTurtle(canvas)
fiz.color("white")

canvas.config(bg="black")
b1=Button(root,text="Play",bg="#51C4D3",width=10,height=2,command=draw)
b1.place(x=620,y=400)
b2=Button(root,text="Exit",bg="#51C4D3",width=10,height=2,command=root.destroy)
b2.place(x=720,y=400)
b3=Button(root,text="Clear",bg="#51C4D3",width=10,height=2,command=delete)
b3.place(x=670,y=340)
root.mainloop()



