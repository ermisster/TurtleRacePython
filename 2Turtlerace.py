import turtle
scn=turtle.Screen()
scn.bgcolor("black")
x=turtle.Turtle()
y=turtle.Turtle()
x.penup()
y.penup()
x.pencolor("green")
y.pencolor("blue")

x.home()
y.home()
x.goto(-100,100)
y.goto(-100,-100)
x.goto(200,100)
y.goto(200,-100)
x.pendown()
y.pendown()
x.circle(60)
y.circle(60)
x.penup()
y.penup()
x.goto(-100,150)
y.goto(-100,-50)
import random
while x.pos() < (200,100) and y.pos() < (200,-100):
    x.fd(random.randint(0,10))
    y.fd(random.randint(0,10))

if x.pos()>(200,100):
        print("green won")
else:
        print("blue won")











turtle.exitonclick()
