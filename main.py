from turtle import Screen
from constants import constants
from models import TurtleRacer

blank = Screen()
blank.setup(constants.winx + constants.gap, constants.winy + constants.gap)
blank.bgcolor("lightgreen")
turtles = []
finishLine = []
c = 0

for item in constants.colors:
    raceTurtle = TurtleRacer.TurtleRacer(item)
    raceTurtle.start_line(c)
    c += 1
    turtles.append(raceTurtle)

for turtle in turtles:
    turtle.race()

blank.mainloop()
