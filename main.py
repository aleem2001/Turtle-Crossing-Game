import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Initializing Screen and its properties
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#Creating Player
player = Player()

#Listening for key strokes to move the player up
screen.listen()
screen.onkeypress(player.move,"Up")

#Creating Car Manager
car_manager = CarManager()

#Creating Scoreboard
scoreboard = Scoreboard()


#Creating the Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Creating the cars
    car_manager.create_car()
    
    #Moving the cars
    car_manager.move_cars()
    
    #Detecting collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect if player successfully crosses, if yes then taking player back to start and updating the level, which means increasing the level number and the car speed
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

#Screen does not close until it is clicked
screen.exitonclick()