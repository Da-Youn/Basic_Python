from tkinter import *
root=Tk()
L1=Label(root,text="화씨")
L2=Label(root,text="섭씨")
L1.grid(row=0, column=0)
L2.grid(row=1,column=0)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


b1=Button(root, text="화씨->섭씨", command=ctemp)
b2=Button(root, text="섭씨->화씨", command=ftemp)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

root.mainloop()

