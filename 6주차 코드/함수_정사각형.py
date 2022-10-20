import turtle
t = turtle.Turtle()

def drawit(x,y,length):
    t.up()
    t.goto(x,y)
    t.down()
    square(length)

def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

drawit(-200,0,100)


#클릭하는 대로 그리기

def drawit_click(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    square(100)

s = turtle.Screen() # 그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit_click)  # 마우스 클릭 이벤트 처리 함수를 등록한다.
