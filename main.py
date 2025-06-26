from turtle import Turtle, Screen
from car import Car
import time

LANE_1_X = 592
LANE_1_Y = 430
TOTAL_LANES = 30

screen = Screen()
screen.setup(1200, 900)
screen.tracer(0)
screen.colormode(255)

turtle = Turtle()
turtle.penup()
turtle.shape("turtle")
turtle.color("darkgreen")
turtle.setheading(90)
turtle.goto(0, -430)

cars = []
new_y = LANE_1_Y
for _ in range(0, TOTAL_LANES):
    car = Car(LANE_1_X, new_y)
    cars.append(car)
    new_y -= 25
game_over = False

def move_up():
    global game_over
    if turtle.ycor() < 430:
        turtle.goto(turtle.xcor(), turtle.ycor() + 20)
    else:
        game_over = True

def move_down():
    if turtle.ycor() > -430:
        turtle.goto(turtle.xcor(), turtle.ycor() - 20)

def move_right():
    if turtle.xcor() < 580:
        turtle.goto(turtle.xcor() + 20, turtle.ycor())

def move_left():
    if turtle.xcor() > -590:
        turtle.goto(turtle.xcor() - 20, turtle.ycor())

screen.listen()
screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_right,"d")
screen.onkeypress(move_left,"a")

start_update = False
while not game_over:
    for car in cars:
        car.move_forward()
        if car.traveling_left:
            if car.xcor() < -600:
                car.reset_car()
                start_update = True
        else:
            if car.xcor() > 600:
                car.reset_car()
                start_update = True
    if start_update:
        screen.update()
        time.sleep(0.05)

print("You Win!")

screen.exitonclick()
