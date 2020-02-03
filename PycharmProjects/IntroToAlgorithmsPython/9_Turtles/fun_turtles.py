# Drawing Class

# Library(read) vs Framework(blueprint)
# - React, ... (Library)
# - Android, iOS, MacOS, Windows, .NET, ... (Framework)

import turtle

# Screen
screen = turtle.Screen()

# Turtle
t = turtle.Turtle()
turtle.pensize(10)

t.shape("turtle")
t.color("red")

for _ in range(8):
    t.forward(100)
    t.right(45)
t.color("blue")
for _ in range(8):
    t.forward(95)
    t.right(45)
t.color("green")
for _ in range(8):
    t.forward(90)
    t.right(45)

screen.exitonclick()
