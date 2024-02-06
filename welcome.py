from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
X_POSITION = 0
Y_POSITION = 310


class Welcome(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.color("white")
        self.write_welcome_message()

    def write_welcome_message(self):
        self.write("Welcome to The Game Of Snake!", align=ALIGNMENT, font=FONT)
