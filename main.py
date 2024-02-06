import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from frame import Frame
from welcome import Welcome


# Création écran de jeu
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Game of Snake")
screen.tracer(0)
screen.update()

# Création Snake
snake = Snake()

# Création de food
food = Food()

# création cadre de jeu
frame = Frame()

# Création du scoreboard
scoreboard = ScoreBoard()

# Add message
welcome = Welcome()

# Récupération du Clavier
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Jeu
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.20)
    snake.move()

    # Detect a collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detection with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.restart()

    # Detection collide with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.restart()

screen.exitonclick()
