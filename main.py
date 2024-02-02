from turtle import Screen
from constants import constants
from models import TurtleRacer

blank = Screen()
blank.setup(constants.winx + constants.gap, constants.winy + constants.gap)
blank.bgcolor("lightgreen")
turtles = []
finishLine = []
finished = 0
is_race_on = True

for item in constants.colors:
    raceTurtle = TurtleRacer.TurtleRacer(item)
    raceTurtle.start_line(len(turtles))
    turtles.append(raceTurtle)

while is_race_on is True:
    for turtle in turtles:
        turtle.race()
        if turtle.status is True:
            finished += 1
        if finished == len(constants.colors):
            is_race_on = False


blank.mainloop()
