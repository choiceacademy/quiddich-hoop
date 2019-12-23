# Quddich 
from turtle import *
t = Turtle()
t.speed(80)
t.pensize(5)

def q():
  t.pendown()
  t.forward(150)
  t.right(90)
  t.circle(50)

# Move turtle to begin center quiddich
t.penup()
t.setpos(0,-100)
t.left(90)
q()

# Move turtle to begin left quiddich
t.penup()
t.setpos(-110,-150)
t.left(90)
q()

# Move turtle to begin right quiddich
t.penup()
t.setpos(110,-150)
t.left(90)

# Draw right quiddich
t.pendown()
t.forward(150)
t.right(90)
t.circle(50)
t.penup()
t.setpos(-30,-400)
