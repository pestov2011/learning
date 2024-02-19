from turtle import *

t = Turtle()
t.color("blue")
t.width(3)
t.shape("circle")
t.pendown()
t.speed(3)

def draw(x, y):
    t.goto(x, y)

t.ondrag(draw)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

scr = t.getscreen()
scr.onscreenclick(move)

t.ondrag(draw)

def setGreen():
    t.color("green")

scr = t.getscreen()

scr.listen()
scr.onkey(setGreen, "g")

scr.onscreenclick(move)
t.ondrag(draw)

def stepRight():
    t.goto(t.xcor() + 5, t.ycor())

scr = t.getscreen()
scr.listen()
scr.onkey(stepRight, 'Right')