import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()

cars = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=my_turtle.move_upwards)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.spawn_cars()
    cars.move_cars()

    # detect collision with car
    for car in cars.all_cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect turtle crossing
    if my_turtle.is_at_finish_line():
        my_turtle.go_to_start()
        cars.level_up()
        scoreboard.level_up()


screen.exitonclick()

