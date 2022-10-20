import turtle
t=turtle.Turtle()
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
drawit(0,0,100)
drawit(200,0,100)

