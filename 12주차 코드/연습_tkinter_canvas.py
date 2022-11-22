from tkinter import *
window=Tk()

c=Canvas(window, width=500, height=500,background="pink")
c.pack()
c.create_oval(100,50,200,100)
c.create_line(0,0,100,30, fill="blue", width=5)
c.create_line(0,30,100,50, 200,30,300,50, fill="yellow", width=5)
c.create_rectangle(50,150,150,250,width=5,fill="skyblue",outline="purple" )
