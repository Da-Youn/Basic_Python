import turtle
t=turtle.Turtle()
s=turtle.Screen()
def drawit(x,y):    
    t.up()
    t.goto(x,y)
    t.down()
    square(100)
def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

s.onscreenclick(drawit)


