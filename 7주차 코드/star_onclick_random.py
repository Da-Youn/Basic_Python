import turtle
import random

t=turtle.Turtle()
s=turtle.Screen()


s_color=["red","blue","yellow","purple","skyblue","green","pink"]
s.bgcolor("black")
t.width(10)

def star(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    # t.color(random.choice(s_color))
    t.color(s_color[random.randrange(len(s_color))])
    length = random.randrange(30,150)
    for i in range (5):   
        t.fd(length)
        t.lt(144)

s.onscreenclick(star)

