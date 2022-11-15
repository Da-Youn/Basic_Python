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
p=PhotoImage(file="movie1.gif")
imageL=Label(root,image=p)
imageL.pack()

root.resizable(width=FALSE, height=FALSE)
