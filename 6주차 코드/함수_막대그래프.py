import turtle
t = turtle.Turtle()

data = []
t.color("black","red")
t.width(3)

def drawBar(height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(height,font=("굴림",16,"bold"))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

while True:
    n=int(input("원하는 숫자를 입력하세요: (끝:0)"))
    if n == 0:
        break
    data.append(n)

for i in data:
    drawBar(i)
