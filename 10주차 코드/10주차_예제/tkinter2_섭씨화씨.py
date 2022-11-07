from tkinter import *
root = Tk()

def ctemp():
    ftemp=float(e1.get()) #e1의 값을 가져온다
    ctemp=round((ftemp-32)*5/9,2)
    e2.delete(0,END)
    e2.insert(0,ctemp)

def ftemp():
    ctemp=float(e1.get()) #e1의 값을 가져온다
    ftemp=round((ctemp*9/5)+32)
    e2.delete(0,END)
    e2.insert(0,ftemp)    


L1 = Label(root, text="화씨")
L2 = Label(root, text="섭씨")
L1.pack() ; L2.pack()

e1 = Entry(root) 
e2 = Entry(root)
e1.pack() ; e2.pack()

b1 = Button(root, text="화씨->섭씨", command=ctemp)
b2 = Button(root, text="섭씨->화씨", command=ftemp)
b1.pack() ; b2.pack()

root.mainloop( )
