import time
from turtle import Screen, Turtle

from obstacle_generator import ObstacleGenerator
from player import Player
from scoreboard import Scoreboard
from welcome_screen import WelcomeScreen


# Complete initial setup of game
def setup(*args):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

    # Display source of turtle icons
    icon_credit.goto(-240, -285)
    icon_credit.color("white")
    icon_credit.write("Icons by Icon8", move=False, align="center", font=FONT)

    # Add images used in welcome screen turtle objects to screen's available shapes
    for num in range(1, 5):
        screen.addshape(f"images/welcome_screen{num}.gif")
    screen.addshape("images/next.gif")
    screen.addshape("images/back.gif")
    screen.addshape("images/play.gif")

    # Call welcome_screen object methods to display welcome message and instructions
    welcome_screen.welcome1()

    screen.addshape("images/turtle.gif")
    cosmo.shape("images/turtle.gif")
    cosmo.hideturtle()

    screen.listen()
    screen.onkeypress(fun=cosmo.move_up, key="Up")

    # Add images used in obstacle turtle objects to screen's available shapes
    for obs_type in obstacle_generator.types:
        screen.addshape(f"images/{obs_type}.gif")
    check_game_trigger()


# Use Turtle's ontimer function to recursively check whether player has pressed 'Play' button for game to begin
def check_game_trigger():
    if welcome_screen.trigger:
        welcome_screen.goto(-1000, -1000)
        welcome_screen.next_button.goto(-1000, -1000)
        welcome_screen.back_button.goto(-1000, -1000)
        begin_game()
    else:
        screen.update()
        screen.ontimer(check_game_trigger, 100)


# Begin game when player hits 'Play' or 'Replay' buttons
def begin_game():
    cosmo.showturtle()
    level_display.show_level()
    play_game = True
    screen.update()

    # Call obstacle_generator methods to create obstacles and move them forward
    obstacle_generator.create_obstacles()
    obstacle_generator.obstacle_move()

    # Detect collision between obstacle and turtle
    for c in obstacle_generator.all_obstacles:
        if cosmo.distance(c) <= 20:
            time.sleep(0.3)
            screen.tracer(0)

            # Iterate over obstacle list, hide turtle, and append to recycle list since this game round is over,
            # and they should not be visible on the end game screen
            for num in range(len(obstacle_generator.all_obstacles)):
                obstacle_generator.all_obstacles[num].hideturtle()
                obstacle_generator.recycle.append(obstacle_generator.all_obstacles[num])
            obstacle_generator.all_obstacles = []

            cosmo.hideturtle()

            # Call function to display end game screen
            end_game()

            play_game = False
            break

    # Detect if player has completed current level
    if cosmo.reach_finish_line():
        level_display.refresh_level()
        obstacle_generator.level_up()

    # Recursively call begin_game function if game is still on
    if play_game:
        screen.ontimer(fun=begin_game, t=100)


def end_game():
    screen.bgcolor("black")

    # Add end game screen turtle image shapes to screen's available shapes
    screen.addshape("images/game_over_message.gif")
    screen.addshape("images/alien_monster.gif")
    screen.addshape("images/replay.gif")
    screen.addshape("images/exit.gif")

    # Call lose_screen method to display game over message and ask player to replay or exit
    lose_screen.lose_screen()
    lose_screen.exit_button.onclick(fun=exit_screen, add=True)
    lose_screen.replay_button.onclick(fun=replay_game, add=True)
    screen.update()


# Reset screen if player chooses to replay and call the begin_game function
def replay_game(*args):
    lose_screen.goto(-1000, -1000)
    lose_screen.exit_button.goto(-1000, -1000)
    lose_screen.replay_button.goto(-1000, -1000)
    lose_screen.game_over_message.goto(-1000, -1000)
    obstacle_generator.level = 0
    level_display.clear()
    level_display.level = 0
    cosmo.goto(cosmo.starting_pos)
    begin_game()


# Exit game screen if player clicks on the 'Exit' button
def exit_screen(*args):
    screen.clearscreen()
    screen.bye()


# Initialize objects used in game and call setup function
if __name__ == "__main__":
    screen = Screen()
    screen.tracer(0)
    cosmo = Player()
    welcome_screen = WelcomeScreen()
    obstacle_generator = ObstacleGenerator()
    lose_screen = WelcomeScreen()
    level_display = Scoreboard()
    icon_credit = Turtle()
    icon_credit.hideturtle()
    FONT = ("Courier", 8, "normal")
    setup()
    screen.mainloop()