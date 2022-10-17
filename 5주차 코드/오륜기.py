import turtle

x=[-230,0,230,-130,130]
y=[0,0,0,-100,-100]
color=['blue','black','red','gold','green']

t=turtle.Turtle()
t.width(20)

for i in range(5):
    t.color(color[i])    
    t.up()
    t.goto(x[i],y[i])
    t.down()
    t.circle(100)
