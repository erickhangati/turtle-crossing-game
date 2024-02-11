from turtle import Turtle


class Scoreboard(Turtle):
    scores = 0
    level = 1

    def __init__(self, score_type):
        super().__init__()
        self.score_type = score_type
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score_position()
        self.display_score()

    def score_position(self):
        if self.score_type == "scores":
            self.goto(120, 280)
        else:
            self.goto(-150, 280)

    def display_score(self):
        """
        Display contact on screen
        :return: None
        """
        if self.score_type == "scores":
            self.write(f"Scores: {self.scores}", font=('Courier', 12, "normal"), align="center")
        else:
            self.write(f"Level: {self.level}", font=('Courier', 12, "normal"), align="center")

    def update_scores(self):
        """
        Update score after contact with food
        :return: None
        """
        self.clear()
        self.scores += 1
        self.display_score()

    def game_over(self):
        """
        Display GAME OVER
        :return:
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", font=('Courier', 12, "normal"), align="center")
