import turtle
import random

s=turtle.Screen()
s.setup(width=.8, height=.7)
dog1="C:\\Users\\User\\Desktop\\dog1.gif"
dog2="C:\\Users\\User\\Desktop\\dog2.gif"

s.addshape(dog1); s.addshape(dog2)

t1=turtle.Turtle() ; t2=turtle.Turtle()
t1.color("pink") ; t2.color("blue")
t1.shape(dog1) ; t2.shape(dog2)

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

    if t1.xcor() > t2.xcor():
        t1.write("내가 이겼다",font=("굴림",20,"bold"))
    elif t1.xcor() < t2.xcor():
        t2.write("내가 이겼다",font=("굴림",20,"bold"))
    else:
        t1.write("비겼네",font=("굴림",20,"bold"))
        t2.write("비겼네",font=("굴림",20,"bold"))
s.onkey(start,"Up")
s.listen()


