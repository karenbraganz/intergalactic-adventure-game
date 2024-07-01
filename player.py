from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.starting_pos = STARTING_POSITION
        self.goto(self.starting_pos)
        self.setheading(90)

    def move_up(self):
        """Control player's turtle movements when UP key is pressed"""

        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """Reset turtle to starting position"""

        if self.ycor() == 280:
            self.goto(STARTING_POSITION)

    def reach_finish_line(self):
        """Detect when player has passed level and

        reset turtle to starting position for the next level"""

        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

