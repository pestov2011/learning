import turtle
from turtle import *


class Sprite(Turtle):

    def __init__(self, x, y, step=10, shp='circle', clr='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def make_step(self):
        if self.xcor() <= -200:
            self.dir = 'Right'
        if self.xcor() >= 200:
            self.dir = 'Left'
        if self.ycor() <= -200:
            self.dir = 'Up'
        if self.ycor() >= 200:
            self.dir = 'Down'

        if self.dir == 'Left':
            self.goto(self.xcor() - self.step, self.ycor())
        elif self.dir == 'Right':
            self.goto(self.xcor() + self.step, self.ycor())
        elif self.dir == 'Up':
            self.goto(self.xcor(), self.ycor() + self.step)
        elif self.dir == 'Down':
            self.goto(self.xcor(), self.ycor() - self.step)

    def is_collide(self):
        if self.xcor() == self.target.xcor() and self.ycor() == self.target.ycor():
            print("collide")
            self.count += 1
            if self.count == 3:
                print("win")
                trap1.ht()
                trap2.ht()

    def is_traps_collide(self):
        if (self.xcor() == self.trap1.xcor() and self.ycor() == self.trap1.ycor()) or \
                (self.xcor() == self.trap2.xcor() and self.ycor() == self.trap2.ycor()):
            print("collide trap")
            self.ht()


class Player(Sprite):

    def __init__(self, x, y, step=10, shp='circle', clr='black'):
        super().__init__(x, y, step, shp, clr)


class Trap(Sprite):

    def __init__(self, player, x, y, step=10, shp='circle', clr='black', dir='Left'):
        super().__init__(x, y, step, shp, clr)
        self.dir = dir
        self.player = player

    def make_step(self):
        super().make_step()

        if self.player and self.xcor() == self.player.xcor() and self.ycor() == self.player.ycor():
            print("collide trap")
            player.ht()

        self.getscreen().listen()
        self.getscreen().ontimer(self.make_step, 100)


class Target(Sprite):

    def __init__(self, player, x, y, step=10, shp='circle', clr='black', dir='Down', count=3):
        super().__init__(x, y, step, shp, clr)
        self.player = player
        self.count = count
        self.dir = dir

    def make_step(self):

        super().make_step()

        if self.player and self.xcor() == self.player.xcor() and self.ycor() == self.player.ycor():
            self.count -= 1
            print('collide')
            if self.count == 0:
                print("win")
                trap1.ht()
                trap2.ht()

        self.getscreen().listen()
        self.getscreen().ontimer(self.make_step, 100)

box = turtle.Turtle()
box.hideturtle()
box.pensize(3)
box.penup()
box.goto(-200, 200)
box.pendown()
box.color('black')

# рисуем рамку
for side in range(4):
    box.fd(400)
    box.right(90)

player = Player(0, -100, 10, 'circle', 'orange')

trap1 = Trap(player, -200, 100, 5, 'square', 'red')
trap2 = Trap(player, 200, 150, 10, 'square', 'red')

scr1 = trap1.getscreen()
scr1.listen()

scr2 = trap2.getscreen()
scr2.listen()

scr1.ontimer(trap1.make_step, 100)
scr2.ontimer(trap2.make_step, 100)

finish = Target(player, 0, 170, 10, 'triangle', 'green', 'Down')

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

scr3 = finish.getscreen()
scr3.listen()
scr3.ontimer(finish.make_step, 100)

turtle.exitonclick()
