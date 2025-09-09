import turtle

# Screen setup
wn = turtle.Screen()
wn.title('Frogger game')
wn.setup(600, 800)
wn.bgcolor('black')

# Tracer turn off screen update
wn.tracer(0)

# Register shapes
wn.register_shape('media/frog.gif')
wn.register_shape('media/car_left.gif')
wn.register_shape('media/car_right.gif')

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

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

    def up(self):
        self.y += 45

    def down(self):
        self.y -= 45

    def right(self):
        self.x += 45

    def left(self):
        self.x -= 45
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx

# Create objects
player = Player(0, -300, 40, 40, 'media/frog.gif')
player.render(pen)

car_left = Car(0, -255, 40, 121, 'media/car_left.gif', -0.05)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, 'w')
wn.onkeypress(player.down, 's')
wn.onkeypress(player.right, 'd')
wn.onkeypress(player.left, 'a')

while True:
    # render
    player.render(pen)
    car_left.render(pen)

    #update objects
    car_left.update()

    # update screen
    wn.update()

    # clear the pen
    pen.clear()

wn.mainloop()