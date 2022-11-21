from tkinter import *
mycolor = "black"
def paint (event):
    x1, y1 = (event.x-2),(event.y-2)
    x2, y2 = (event.x+2),(event.y+2)
    c.create_oval(x1,y1,x2,y2,fill=mycolor,width=0)

def red():
    global mycolor
    mycolor = "red"

def black():
    global mycolor
    mycolor = "black"


window = Tk()
c=Canvas(window)
c.pack()
c.bind("<B1-Motion>",paint)
redb = Button(window,text="빨강",command=red)
redb.pack()
blackb = Button(window,text="검정",command=black)
blackb.pack()


window.mainloop()
    
