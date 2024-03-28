from turtle import Turtle

#Constants
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()
        
    #Updating Scoreboard
    def update_scoreboard(self):   
        self.clear()
        self.write(f"Level: {self.level}", align="left", font = FONT)

    #Increasing the Level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    #Game Over text
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)