import turtle
t= turtle.Turtle()
t.shape("circle")

t.width(6)
t.color("saddlebrown")


t.fillcolor("rosybrown")
t.begin_fill()
for i in range(2):
    t.fd(200)
    t.lt(120)   
    t.fd(100)
    t.lt(60)
t.end_fill()

t.width(3)
t.up()
t.goto(0,0)
t.down()
t.fillcolor("seashell")
t.begin_fill()
for i in range(4):
    t.rt(90)
    t.fd(100)
for i in range(2):
    t.fd(200)
    t.rt(90)
    t.fd(100)
    t.rt(90)
t.end_fill()

t.width(6)
t.fillcolor("saddlebrown")
for i in range(3):
    t.lt(120)   
    t.fd(100)
    t.stamp()

t.up()
t.goto(-75,0)
t.lt(90)
t.down()
t.fd(10)
for i in range(8):
    t.fd(10)
    t.rt(360/16)
t.fd(20)
t.rt(90)
t.fd(55)
t.up()
t.goto(0,0)
t.rt(180)
t.down()

for i in range(4):
    t.fd(25)
    t.lt(120)
    t.fd(100)
    t.rt(120)
    t.fd(25)
    t.rt(60)
    t.fd(100)
    t.lt(60)
t.rt(180)
t.fd(200)


t.width(3)
t.up()
t.goto(-85,-100)
t.down()

t.fillcolor("brown")
t.begin_fill()
for i in range(3):
    t.rt(90)
    t.fd(70)
t.end_fill()
t.rt(90)
t.fd(35)
t.rt(90)
t.fd(70)

t.up()
t.goto(100,-40)
t.down()
t.fillcolor("whitesmoke")
t.begin_fill()
for i in range(2):
    for j in range(2):
        t.fd(25)
        t.rt(90)
        t.fd(75)
        t.rt(90)
    t.lt(180)
    
for i in range(2):
    for j in range(2):
        t.rt(90)
        t.fd(75)
        t.rt(90)
        t.fd(25)
    t.lt(180)
t.end_fill()

t.up()
t.goto(15,-100)
t.down()
t.color("olive")
t.fillcolor("olive")
t.begin_fill()
t.width(6)

for i in range(7):
    for j in range(8):
        t.fd(4.75)
        t.rt(360/16)
    t.fd(4.75)
    t.lt(180)
t.lt(90)
t.fd(180)
t.end_fill()



    
