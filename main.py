# Space War game made by @gimyboya
import os
import random
import turtle

#  setting the turtle module
turtle.speed(0)  # speed of animation 0 is maximum speed
turtle.bgcolor('black')
turtle.ht()  # hide default turtle
turtle.setundobuffer(1)  # limit turtle memory (performance)
turtle.tracer(1)  # speeding the drawing


class Pencil(turtle.Turtle):  # inhirit from turtle module
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)  # animation speed
        self.penup  # nothing on the screen
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        elif self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        elif self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        elif self.ycor() < -290:
            self.sety(-290)
            self.rt(60)



class Player(Pencil):
    def __init__(self, spriteshape, color, startx, starty):
        Pencil.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def brk(self):
        self.speed -= 1

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def borders(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(4)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()


game = Game()
game.borders()
player = Player("triangle", "white", 0, 0)

# keyboard bindings

turtle.onkeypress(player.turn_left, "Left")
turtle.onkeypress(player.turn_right, "Right")
turtle.onkeypress(player.accelerate, "Up")
turtle.onkeypress(player.brk, "Down")
turtle.listen()

#  Main game loop

while True:
    player.move()