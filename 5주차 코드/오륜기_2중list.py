import turtle

x=[[-230,0,'blue'],[0,0,'black'],[230,0,'red'],[-130,-100,'gold'],[130,-100,'green']]

t=turtle.Turtle()
t.width(20)

for i in range(5):
    t.color(x[i][2])    
    t.up()
    t.goto(x[i][0],x[i][1])
    t.down()
    t.circle(100)
