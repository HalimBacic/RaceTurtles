from turtle import Screen, Turtle
from constants import constants
from models import TurtleRacer

blank = Screen()
blank.setup(constants.winx + constants.gap, constants.winy + constants.gap)
blank.bgcolor("lightgreen")
turtles = []
finishLine = []
finished = 0
is_race_on = True


def showMessage(color):
    msgScreen = Screen()
    msg = Turtle()
    msg.penup()
    msg.goto(0, 0)
    msg.hideturtle()
    msg.write(f"Winner is {color}", align="center", font=("Arial", 14, "normal"))
    msgScreen.mainloop()


for item in constants.colors:
    raceTurtle = TurtleRacer.TurtleRacer(item)
    raceTurtle.start_line(len(turtles))
    turtles.append(raceTurtle)

while is_race_on is True:
    for turtle in turtles:
        turtle.race()
        if turtle.status is True:
            finished += 1
            finishLine.append(turtle)
        if finished == len(constants.colors):
            is_race_on = False
            showMessage(finishLine[0].turtle.color())

blank.mainloop()
