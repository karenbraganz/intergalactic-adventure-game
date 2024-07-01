from turtle import Turtle


class WelcomeScreen(Turtle):
    def __init__(self):
        """Initialize all turtle objects used to display

        welcome instructions, game over message, and buttons"""

        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 50)
        self.trigger = False
        self.back_button = Turtle()
        self.back_button.hideturtle()
        self.next_button = Turtle()
        self.next_button.hideturtle()
        self.game_over_message = Turtle()
        self.game_over_message.hideturtle()
        self.exit_button = Turtle()
        self.exit_button.hideturtle()
        self.replay_button = Turtle()
        self.replay_button.hideturtle()

    def welcome1(self, *args):
        """Display first welcome screen with only the 'Next' button"""

        self.showturtle()
        self.shape("images/welcome_screen1.gif")
        self.back_button.hideturtle()
        self.next_button.penup()
        self.next_button.goto(150, -150)
        self.next_button.shape("images/next.gif")
        self.next_button.showturtle()

        # Add event listener to button to allow player to navigate between screens
        self.next_button.onclick(fun=self.welcome2, add=True)

    def welcome2(self, *args):
        """Display second welcome screen with 'Back' and 'Next' buttons"""

        self.shape("images/welcome_screen2.gif")
        self.back_button.penup()
        self.back_button.goto(-150, -150)
        self.back_button.shape("images/back.gif")
        self.back_button.showturtle()
        self.back_button.onclick(fun=self.welcome1, add=True)
        self.next_button.onclick(fun=self.welcome3, add=False)
        self.next_button.shape("images/next.gif")

    def welcome3(self, *args):
        """Display third welcome screen"""

        self.shape("images/welcome_screen3.gif")
        self.back_button.onclick(fun=self.welcome2, add=False)
        self.next_button.onclick(fun=self.welcome4, add=False)
        self.next_button.shape("images/next.gif")

    def welcome4(self, *args):
        """Display fourth welcome screen replacing 'Next' button with 'Play' button"""

        self.shape("images/welcome_screen4.gif")
        self.back_button.onclick(fun=self.welcome3, add=False)
        self.next_button.shape("images/play.gif")
        self.next_button.onclick(fun=self.game_trigger, add=False)

    def game_trigger(self, *args):
        """Set game trigger to true for game to begin"""

        self.trigger = True

    def lose_screen(self):
        """Display game over screen with 'Replay' and 'Exit' buttons"""

        self.goto(0, 100)
        self.shape("images/alien_monster.gif")
        self.showturtle()
        self.game_over_message.goto(0, -30)
        self.game_over_message.shape("images/game_over_message.gif")
        self.game_over_message.showturtle()
        self.exit_button.penup()
        self.exit_button.goto(150, -150)
        self.exit_button.shape("images/exit.gif")
        self.exit_button.showturtle()
        self.replay_button.penup()
        self.replay_button.goto(-150, -150)
        self.replay_button.shape("images/replay.gif")
        self.replay_button.showturtle()
