import turtle

class InitialPos:
    def __init__(self, position, size):
        self.t = turtle.Turtle(shape="circle", visible = False)
        self.t.speed('fastest')
        self.t.shapesize(size)
        self.t.penup()
        self.t.goto(position[0], position[1])
        self.t.showturtle()

    def get_position(self):
        return self.t.pos()

