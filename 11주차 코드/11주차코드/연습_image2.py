from tkinter import *
root=Tk()
root.title("다연")
#root.geometry("400x200+100+100")


e=Entry(root)
e.insert(0,"Hello")
e.pack()
L=Label(root,text="Hello")
L.pack()
b=Button(root,text="닫기")
b.pack()

p1=PhotoImage(file="movie1.gif")
imageL1=Label(root,image=p1)
imageL1.pack(side=LEFT)
p2=PhotoImage(file="movie2.png")
imageL2=Label(root,image=p2)
imageL2.pack()

root.resizable(width=FALSE, height=FALSE)
