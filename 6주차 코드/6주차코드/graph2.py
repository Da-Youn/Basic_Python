def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(height,font=("굴림",16,"bold"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


import turtle
t=turtle.Turtle()

data=[]
t.color("black","red")
t.width(3)
while True:
    n=input("원하는 숫자를 입력하세요: (끝:q)")
    if n=="q":
        break
    data.append(int(n))

for i in data:
    drawBar(i)
