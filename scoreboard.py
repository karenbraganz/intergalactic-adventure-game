from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("white")
        # Read highscore for display
        with open("highscore.txt") as self.file:
            self.highscore = int(self.file.read())

    def show_level(self):
        """Displays game level and highscore on the screen"""

        self.goto(0, 250)
        self.write(f"Level: {self.level}         High Score: {self.highscore}", move=False, align="center", font=FONT)

    def refresh_level(self):
        """Increment game level when a level is cleared"""

        self.level += 1
        # Update highscore if current level is higher
        if self.level > self.highscore:
            self.highscore = self.level
            with open("highscore.txt", mode="w") as self.file:
                self.file.write(str(self.highscore))
        self.clear()
        self.show_level()
