import turtle
import random

s=turtle.Screen()
s.setup(width=.8, height=.7)
dog1="C:\\Users\\User\\Desktop\\dog1.gif"
dog2="C:\\Users\\User\\Desktop\\dog2.gif"

s.addshape(dog1)
s.addshape(dog2)

t1=turtle.Turtle()
t1.color("pink")
t1.shape(dog1)

t2=turtle.Turtle()
t2.color("blue")
t2.shape(dog2)

t1.up()
t1.goto(-400,100)
t1.down()

t2.up()
t2.goto(-400,-100)
t2.down()

def start():
    for _ in range(50):
        d1=random.randint(1,30)
        t1.fd(d1)
    
        d2=random.randint(1,30)
        t2.fd(d2)

    t1.write(t1.xcor(),font=("굴림",20))
    t2.write(t2.xcor(),font=("굴림",20))

s.onkey(start,"Up")
s.listen()


