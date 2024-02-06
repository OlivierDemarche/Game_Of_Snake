from turtle import Turtle
COORDINATE1 = (-290,-290)
COORDINATE2 = (290,-290)
COORDINATE3 = (290,270)
COORDINATE4 = (-290,270)

class Frame(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.draw_frame()

    def draw_frame(self):
        self.goto(COORDINATE1)
        self.pendown()
        self.pencolor("white")
        self.goto(COORDINATE2)
        self.goto(COORDINATE3)
        self.goto(COORDINATE4)
        self.goto(COORDINATE1)
        self.hideturtle()