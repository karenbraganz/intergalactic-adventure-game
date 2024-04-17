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

    # Control player's turtle movements when UP key is pressed
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # Reset turtle to starting position
    def reset_turtle(self):
        if self.ycor() == 280:
            self.goto(STARTING_POSITION)

    # Detect when player has passed level and reset turtle to starting position for the next level
    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

