import turtle
t=turtle.Turtle()

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

data=[120,96,300,220]
t.color("black","red")
t.width(3)

for i in data:
    drawBar(i)

