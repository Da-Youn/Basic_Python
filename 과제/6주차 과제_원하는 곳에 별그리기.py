import turtle
t = turtle.Turtle()
t.width(5)

def draw_star(x,y,color,length):
    t.color(color)
    t.up()
    t.goto(x,y)
    t.down()
    star(length)
    
def star(length):
    for i in range(5):
        t.fd(length)
        t.lt(144)

draw_star(10,10,"blue",100)
draw_star(-150,150,"brown",200)
draw_star(-150,-50,"orange",50)
