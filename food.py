from turtle import Turtle
import random

X_POSITION = list(range(-280, 280, 20))
Y_POSITION = list(range(-280, 260, 20))


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Divide by 2 the size of the circle normally equal to 20
        self.color("green")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        random_x = random.choice(X_POSITION)
        random_y = random.choice(Y_POSITION)
        self.goto(-random_x, random_y)
