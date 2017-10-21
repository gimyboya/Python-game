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


class Soul(turtle.Turtle):  # inhirit from turtle module
    def __init__(self, soulshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=soulshape)
        self.speed(0)  # animation speed
        self.penup()  # nothing on the screen
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
    # Collision detection
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
                return True
        else:
            return False




class Player(Soul): # inhirit from Pencil class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
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

class Evil(Soul): # inhirit from Pencil class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))

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
enemy = Evil("circle", "red", -100, 0)

# keyboard bindings

turtle.onkeypress(player.turn_left, "Left")
turtle.onkeypress(player.turn_right, "Right")
turtle.onkeypress(player.accelerate, "Up")
turtle.onkeypress(player.brk, "Down")
turtle.listen()

#  Main game loop

while True:
    player.move()
    enemy.move()

    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    #collision with enemy
    if(player.is_collision(enemy)):
        enemy.goto(x,y)