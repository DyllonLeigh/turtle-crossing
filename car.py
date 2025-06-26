from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(1, (randint(2,5)))
        self.penup()
        self.setheading(180)
        self.pace = randint(5, 20)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(position)

    def move_forward(self):
        self.forward(self.pace)