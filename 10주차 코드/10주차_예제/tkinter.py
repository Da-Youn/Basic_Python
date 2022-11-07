from tkinter import*
root=Tk()
root.title("데이앤")

#버튼 누르면 "안녕하세요" 출력 (앞에 와야 함)
def hello():
    print("안녕하세요")

e=Entry(root)
e.pack()
e.insert(0,"hello World")

L=Label(root,text="Hello World") #레이블
L.pack()

b=Button(root, text="Hello World",command=hello) #버튼
b.pack()


