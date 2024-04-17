from turtle import Turtle
import random
import time

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 310


class ObstacleGenerator:
    def __init__(self):
        self.all_obstacles = []
        self.level = 0
        self.types = ["spaceship", "regular_asteroid", "fiery_asteroid"]
        self.recycle = []

    # Create obstacles and append to list for tracking
    def create_obstacles(self):
        # Control frequency of created obstacles
        obstacle_number = random.randint(0, 3)

        # Obstacles are created at a higher frequency at higher levels to keep up with the increased speed of obstacles
        if obstacle_number <= 0 + self.level:
            if not self.recycle:
                obstacle = Turtle()
                obstacle.penup()
                obstacle_type = random.choice(self.types)
                obstacle.shape(f"images/{obstacle_type}.gif")
            else:
                # Recycle obstacles once they are off the screen to avoid continuously creating more objects
                obstacle = self.recycle.pop()
                obstacle.hideturtle()
            obstacle.penup()
            y_pos = random.randint(-230, 230)
            x_pos = 310
            obstacle.setheading(180)
            self.all_obstacles.append(obstacle)
            obstacle.goto(x_pos, y_pos)
            obstacle.showturtle()

    # Move obstacles forward with speed in accordance with game level
    def obstacle_move(self):
        for i in self.all_obstacles:
            # Remove obstacle from the all_obstacles list and add to recycle list once it is off the screen
            if i.xcor() <= -350:
                self.all_obstacles.remove(i)
                self.recycle.append(i)
            else:
                i.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level))

    # Record increase in player level
    def level_up(self):
        self.level += 1
        self.obstacle_move()

