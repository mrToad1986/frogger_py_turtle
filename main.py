import turtle

# Screen setup
wn = turtle.Screen()
wn.title('Frogger game')
wn.setup(600, 800)
wn.bgcolor('black')
# tracer turn off screen update
wn.tracer(0)
wn.register_shape('media/frog.gif')

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

# Create objects
player = Player(0, -300, 40, 40, 'media/frog.gif')
player.render(pen)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, 'w')
wn.onkeypress(player.down, 's')
wn.onkeypress(player.right, 'd')
wn.onkeypress(player.left, 'a')

while True:
    # render
    player.render(pen)
    # update screen
    wn.update()
    # clear the pen
    pen.clear()

wn.mainloop()