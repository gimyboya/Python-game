# Space War game made by @gimyboya
import pygame
import random
import turtle
import time

#  setting the turtle module
turtle.speed(0)  # speed of animation 0 is maximum speed
turtle.bgcolor('black')
turtle.bgpic(picname="cache.gif")
turtle.title("I am a legend")
turtle.ht()  # hide default turtle
turtle.setundobuffer(1)  # limit turtle memory (performance)
turtle.tracer(0)  # speeding the drawing

# int pygame
pygame.mixer.init(frequency=44100, size=-16, channels=4, buffer=4096)
pygame.init()

# background soundfx
pygame.mixer.Channel(0).play(pygame.mixer.Sound("Creepy.ogg"), loops=-1)

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
            self.rt(90)
        elif self.xcor() < -290:
            self.setx(-290)
            self.rt(90)
        elif self.ycor() > 290:
            self.sety(290)
            self.rt(90)
        elif self.ycor() < -290:
            self.sety(-290)
            self.rt(90)
    # Collision detection
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 40)) and \
            (self.xcor() <= (other.xcor() + 40)) and \
            (self.ycor() >= (other.ycor() - 40)) and \
            (self.ycor() <= (other.ycor() + 40)):
                return True
        else:
            return False




class Player(Soul): # inhirit from Soul class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
        self.speed = 2
        self.lives = 7
        self.setheading(90)

    def turn_left(self):
        self.shape("player-l.gif")
        self.setheading(180)

    def turn_right(self):
        self.shape("player-r.gif")
        self.setheading(0)

    def up(self):
        self.shape("player-u.gif")
        self.setheading(90)

    def down(self):
        self.shape("player-d.gif")
        self.setheading(270)

class Zombie(Soul): # inhirit from Soul class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
        self.speed = 1
        self.goto(random.randint(-300, 300), random.randint(-300, 300))

    def turn(self):
        if(self.heading() == 0 ):
            self.shape("zombie-r.gif")
        if (self.heading() == 90):
            self.shape("zombie-u.gif")
        if (self.heading() == 180):
            self.shape("zombie-l.gif")
        if (self.heading() == 270):
            self.shape("zombie-d.gif")

        
        
class Bullet(Soul): # inhirit from Soul class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 80
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            pygame.mixer.init()
            pygame.mixer.music.load("fire.mp3")
            pygame.mixer.music.play(loops=0, start=2.2)
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "shooting"

    def move(self):
        if self.status == "ready":
            self.goto(-2000, 2000)

        if self.status == "shooting":
            self.fd(self.speed)

        # border check
        if self.xcor() > 290 or \
            self.xcor() < -290 or \
            self.ycor() > 290 or \
            self.ycor() < -290:

            self.goto(-2000, 2000)
            self.status = "ready"

class Blood(Soul): # inhirit from Soul class
    def __init__(self, soulshape, color, startx, starty):
        Soul.__init__(self, soulshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.speed = 10
        self.goto(-2000, 2000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1
        if self.frame > 10:
            self.frame = 0
            self.goto(-2000, 2000)



class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    # def borders(self):
    #     self.pen.speed(0)
    #     self.pen.color("white")
    #     self.pen.pensize(4)
    #     self.pen.penup()
    #     self.pen.goto(-500, 415)
    #     self.pen.pendown()
    #     for side in range(4):
    #         self.pen.fd(600)
    #         self.pen.rt(90)
    #     self.pen.penup()
    #     self.pen.ht()
    #     self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        self.pen.color("white")
        msg = "Score: %s  Lives: %s" % (self.score, player.lives)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

# Game initialization
game = Game()


# player shapes
turtle.register_shape("player-u.gif")
turtle.register_shape("player-d.gif")
turtle.register_shape("player-r.gif")
turtle.register_shape("player-l.gif")

turtle.register_shape("zombie-u.gif")
turtle.register_shape("zombie-d.gif")
turtle.register_shape("zombie-r.gif")
turtle.register_shape("zombie-l.gif")


player = Player("player-u.gif", "white", 0, 0)
missile = Bullet("triangle", "yellow", 0, 0)
enemies = []
blood = []
game.show_status()
for i in range(7):
    enemies.append(Zombie("zombie-u.gif", "red", -100, 0))

for i in range(20):
    blood.append(Blood("circle", "red", 0, 0))
# keyboard bindings

turtle.onkeypress(player.turn_left, "Left")
turtle.onkeypress(player.turn_right, "Right")
turtle.onkeypress(player.up, "Up")
turtle.onkeypress(player.down, "Down")
turtle.onkeypress(missile.fire, "space")
turtle.listen()

START_TICKS = pygame.time.get_ticks() #start time

#  Main game loop

while game.state == "playing":
    turtle.update()
    time.sleep(0.03)
    # create a count down
    seconds = (pygame.time.get_ticks() - START_TICKS) / 1000  # calculate how many seconds
    minutes = seconds / 60

    if minutes > 1: # if more than 1 minutes close the game
        break

    player.move()
    missile.move()

    for zombie in enemies:
        zombie.turn()
        zombie.move()
        # collision of player with zombie
        if (player.is_collision(zombie)):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            zombie.goto(x, y)
            player.goto(0,0)
            pygame.mixer.init()
            pygame.mixer.music.load("Death.mp3")
            pygame.mixer.music.play(loops=0, start=10.6)
            player.lives -= 1
            game.show_status()
            if player.lives == 0:
                game.state = "game over"

        # collision of missile with zombie
        if (zombie.is_collision(missile)):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            zombie.goto(x, y)
            pygame.mixer.init()
            pygame.mixer.music.load("Death.mp3")
            pygame.mixer.music.play(loops=0, start=5.7)
            missile.status = "ready"
            game.score += 10
            game.show_status()
            for drop in blood:
                drop.explode(missile.xcor(), missile.ycor())

    for drop in blood:
        drop.move()