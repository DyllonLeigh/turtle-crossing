from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1, (randint(2,5)))
        self.penup()
        if randint(0, 1) == 0:
            self.setheading(0)
            self.traveling_left = False
            self.new_x = x_pos * -1
        else:
            self.setheading(180)
            self.traveling_left = True
            self.new_x = x_pos
        self.pace = randint(10, 25)
        self.pace = randint(10, 30)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(self.new_x, y_pos)

    def move_forward(self):
        self.forward(self.pace)

    def reset_car(self):
        self.goto(self.new_x, self.ycor())