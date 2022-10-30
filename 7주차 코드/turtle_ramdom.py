import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
for _ in range(30):
    length=random.randint(1,100)
    t.fd(length)
# angle=random.choice([-180,180,0,90,180])
    angle=random.randrange(-180,181,90)
    t.right(angle)
