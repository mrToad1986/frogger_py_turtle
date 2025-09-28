import turtle
import math

# Screen setup
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title('Frogger game')
wn.setup(600, 800)
wn.bgcolor('black')

# Tracer turn off screen update
wn.tracer(0)

# Register shapes
wn.register_shape('media/frog.gif')
wn.register_shape('media/car_left.gif')
wn.register_shape('media/car_right.gif')
wn.register_shape('media/log_full.gif')

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

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

    # AABB check (Axis-Aligned Bounding Box)
    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)


class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

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

# Create objects
player = Player(0, -300, 40, 40, 'media/frog.gif')
car_left = Car(0, -250, 121, 40, 'media/car_left.gif', -0.06)
car_right = Car(0, -200, 121, 40, 'media/car_right.gif', 0.06)
log_left = Log(0, -100, 121, 40, 'media/log_full.gif', -0.08)
log_right = Log(0, -150, 121, 40, 'media/log_full.gif', 0.08)

# Create list of sprites
sprites = [player, car_left, car_right, log_left, log_right]

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
    if player.is_collision(car_left) or player.is_collision(car_right):
        player.x = 0
        player.y = -300

    if player.is_collision(log_left):
        player.dx = log_left.dx
    else:
        player.dx = 0

    if player.is_collision(log_right):
        player.dx = log_right.dx
    else:
        player.dx = 0

    # update screen
    wn.update()

    # clear the pen
    pen.clear()

wn.mainloop()