# Draw a pattern

import turtle
screen = turtle.Screen()

t = turtle.Turtle()
t.pen(fillcolor="blue", pencolor="blue", pensize=7)
t.shape("turtle")
screen.bgcolor("lightgreen")

for _ in range(12):
    t.speed(5)
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(20)
    t.stamp()
    t.right(180)
    t.forward(220)
    t.right(30)

screen.exitonclick()
