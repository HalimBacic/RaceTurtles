from turtle import Turtle
import random
from constants import constants


class TurtleRacer:
    def __init__(self, color):
        self.position = 0
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")

    def start_line(self, param):
        self.turtle.penup()
        x = -constants.winx/2
        y = param * constants.trackHeigth + constants.startPosition
        self.turtle.goto(x, y)

    def race(self):
        while self.position < constants.winx:
            self.position += random.randint(0, constants.speed)
            self.turtle.forward(self.position)
        return self
