import turtle
t= turtle.Turtle()
angle = 360
t.shape("circle")
t.width(3)
t.color("saddlebrown")
for i in range(4):
    for j in range(4):
        t.lt(90)
        t.fd(100)
    t.rt(90)

