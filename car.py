from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1, (randint(2,5)))
        self.penup()
        self.pace = randint(10, 30)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.new_x = x_pos
        self.setheading(180)
        if randint(0, 1) == 0:
            self.new_x = x_pos * -1
            self.setheading(0)
        self.goto(self.new_x, y_pos)

    def move_forward(self):
        self.forward(self.pace)

    def reset_car(self):
        self.goto(self.new_x, self.ycor())