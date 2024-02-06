from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
X_POSITION = 0
Y_POSITION = 280


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def end_of_game(self):
        self.goto(x=0, y=0)
        self.write(f"END!", align=ALIGNMENT, font=FONT)


