import lesson9class
from lesson9class import *
# The .pyc file is supposed to be there! Don't delete it :)

robot = Robot(0,0,False)

print "Welcome to the Robot game!"

robot.printbot()
print "That is what the field looks like! A | is the robot, a , is the cube and a . is an empty meter of the field. The last dot is the goal! You win once you accumulate 20 points, good luck!\n"

while robot.score < 20:
    robot.printbot()
    print "Your score is", robot.score
    print "Your robot's arm is at", robot.armpos
    print "Your robot is at position", robot.pos

    if robot.haspiece == True:
        print "Your robot has a cube!"

    if robot.pos == 3 and robot.armpos == 0 and not robot.haspiece:
        pickupcube = str(raw_input("Would you like to pick up the cube? (y/n): "))
        if pickupcube == "y":
            robot.pickupcube()
    elif robot.pos == 7 and robot.armpos == 10 and robot.haspiece:
        scorecube = str(raw_input("Would you like to score? (y/n): "))
        if scorecube == "y":
            robot.scorecube()

    goalpos = int(raw_input("How far would you like to move? "))
    goalarmpos = int(raw_input("How far would you like to move the arm? "))
    robot.move(goalpos)
    robot.armmove(goalarmpos)
