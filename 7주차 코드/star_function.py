import turtle
t=turtle.Turtle()
t.width(10)
s_color=["red","blue","pink","green"]

def star(x,y):
    c=0
    t.up()
    t.goto(x,y)
    t.down()
    t.color(s_color[c])
    c+=1
    for i in range (5):   
        t.fd(100)
        t.lt(144)

s=turtle.Screen()
s.onscreenclick(star)

