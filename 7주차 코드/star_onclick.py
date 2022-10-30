import turtle
t=turtle.Turtle()
t.width(10)
s_color=["red","blue","pink","green"]
c=0

def star(x,y):
    global c
    t.up()
    t.goto(x,y)
    t.down()
    t.color(s_color[c])
    c+=1
    #print(len(s_color))
    if c >= len(s_color):
        c=0

    for i in range (5):   
        t.fd(100)
        t.lt(144)

s=turtle.Screen()
s.onscreenclick(star)

