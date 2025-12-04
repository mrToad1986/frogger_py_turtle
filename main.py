import turtle
import math
import time
import random

# Screen setup
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title('Frogger game')
wn.setup(600, 800)
wn.bgcolor('green')
wn.bgpic('media/background.gif')
# Tracer turn off screen update
wn.tracer(0)

# Register shapes
shapes = [
    'media/frog.gif',
    'media/car_left.gif',
    'media/car_right.gif',
    'media/log_full.gif',
    'media/turtle_left.gif',
    'media/turtle_right.gif',
    'media/turtle_left_half.gif',
    'media/turtle_right_half.gif',
    'media/turtle_submerged.gif',
    'media/home.gif',
    'media/frog_home.gif',
]
for shape in shapes:
    wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Create classes
class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def update(self):
        pass

    # AABB check (Axis-Aligned Bounding Box)
    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)


class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision = False

    def up(self):
        self.y += 50

    def down(self):
        self.y -= 50

    def right(self):
        self.x += 50

    def left(self):
        self.x -= 50

    def update(self):
        self.x += self.dx
        if self.x < -300 or self.x > 300:
            self.x = 0
            self.y = -300

class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx

        # Border cheking
        if self.x < - 400:
            self.x = 400
        if self.x > 400:
            self.x = -400

class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx

        # Border cheking
        if self.x < - 400:
            self.x = 400
        if self.x > 400:
            self.x = -400

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = 'full' # half, submerged
        self.full_time = random.randint(8, 12)
        self.half_time = random.randint(4,6)
        self.submerged_time = random.randint(4,6)
        self.start_time = time.time()

    def update(self):
        self.x += self.dx

        # Border cheking
        if self.x < - 400:
            self.x = 400
        if self.x > 400:
            self.x = -400

        # Turtle animation based on state
        if self.state == 'full':
            if self.dx > 0:
                self.image = 'media/turtle_right.gif'
            else:
                self.image = 'media/turtle_left.gif'
        elif self.state == 'half_up' or self.state == 'half_down':
            if self.dx > 0:
                self.image = 'media/turtle_right_half.gif'
            else:
                self.image = 'media/turtle_left_half.gif'
        elif self.state == 'submerged':
            self.image = 'media/turtle_submerged.gif'

        # State timer
        if self.state == 'full' and time.time() - self.start_time > self.full_time:
            self.state = 'half_down'
            self.start_time = time.time()
        elif self.state == 'half_down' and time.time() - self.start_time > self.half_time:
            self.state = 'submerged'
            self.start_time = time.time()
        elif self.state == 'submerged' and time.time() - self.start_time > self.submerged_time:
            self.state = 'half_up'
            self.start_time = time.time()

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

# Create objects
player = Player(0, -325, 40, 40, 'media/frog.gif')

level_1 = [
    Car(0, -275, 121, 40, 'media/car_left.gif', -0.06),
    Car(0, -225, 121, 40, 'media/car_right.gif', 0.06),
    Car(0, -175, 121, 40, 'media/car_left.gif', -0.06),
    Car(0, -125, 121, 40, 'media/car_right.gif', 0.06),
    Car(0, -75, 121, 40, 'media/car_left.gif', -0.06),
    Log(0, 25, 121, 40, 'media/log_full.gif', 0.08),
    Log(0, 75, 121, 40, 'media/log_full.gif', -0.08),
    Turtle(0, 125, 155, 40, 'media/turtle_left.gif', 0.09),
    Turtle(0, 175, 155, 40, 'media/turtle_right.gif', -0.09),
    Log(0, 225, 121, 40, 'media/log_full.gif', -0.08),
]

homes = [
    Home(0, 275, 50, 50, 'media/home.gif'),
    Home(-100, 275, 50, 50, 'media/home.gif'),
    Home(-200, 275, 50, 50, 'media/home.gif'),
    Home(100, 275, 50, 50, 'media/home.gif'),
    Home(200, 275, 50, 50, 'media/home.gif'),
]

# Create list of sprites
sprites = level_1 + homes
sprites.append(player)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, 'w')
wn.onkeypress(player.down, 's')
wn.onkeypress(player.right, 'd')
wn.onkeypress(player.left, 'a')

while True:
    # render and update
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    # check for collisions
    player.dx = 0
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.x = 0
                player.y = -325
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                player.collision = True
                break
            # no collision for submerged turtle
            elif isinstance(sprite, Turtle) and sprite.state != 'submerged':
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home):
                player.x = 0
                player.y = -325
                sprite.image = 'media/frog_home.gif'
                break
    # check for water border crossing
    if player.y > 0 and player.collision != True:
        player.x = 0
        player.y = -325



    #if player.is_collision(car_left) or player.is_collision(car_right):
    #    player.x = 0
    #    player.y = -300

    #if player.is_collision(log_left):
    #    player.dx = log_left.dx
    #else:
    #    player.dx = 0

    #if player.is_collision(log_right):
    #    player.dx = log_right.dx
    #else:
    #    player.dx = 0

    # update screen
    wn.update()

    # clear the pen
    pen.clear()

wn.mainloop()