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
        self.y += 50

    def down(self):
        self.y -= 50

    def right(self):
        self.x += 50

    def left(self):
        self.x -= 50
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

# Create objects
player = Player(0, -300, 40, 40, 'media/frog.gif')
player.render(pen)

car_left = Car(0, -250, 40, 121, 'media/car_left.gif', -0.08)
car_right = Car(0, -200, 40, 121, 'media/car_right.gif', 0.08)

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
    car_right.render(pen)

    #update objects
    car_left.update()
    car_right.update()

    # update screen
    wn.update()

    # clear the pen
    pen.clear()

wn.mainloop()