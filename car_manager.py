from turtle import Turtle
import random

#Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        #List to contain all cars
        self.all_cars = []
        #Setting car speed
        self.car_speed = STARTING_MOVE_DISTANCE
    
    #Creating a single car
    def create_car(self):
        random_chance = random.randint(1,10)
        #Only creating a car if random_chance is 1
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250,250)             #Returns and integer betweeon -250 and 250, both included
            new_car.goto(300,random_y)
            new_car.setheading(180)
            #Appending new car to all_cars list
            self.all_cars.append(new_car)
        
    #Moving all the cars
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            
    #Increasing car speed once a level has been successfully completed
    def level_up(self):
        self.car_speed += MOVE_INCREMENT