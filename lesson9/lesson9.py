class Robot:
    def __init__(self, pos, armpos, haspiece):
        self.pos = pos #int
        self.armpos = armpos #int
        self.haspiece = haspiece #bool
        self.score = 0

    def move(self,dist):
        self.pos += dist

    def armmove(self,dist):
        self.armpos += dist

    def pickupcube(self):
        if self.pos == 1 and self.armpos == 0:
            self.haspiece = True

    def scorecube(self):
        if self.haspiece and self.pos == 6 and self.armpos == 10:
            self.score += 5
            self.haspiece = False

    def printbot(self): #This function is extra fanciness because I was bored. You do NOT need to have this
        s = ""
        for i in range(0,8):
            if i == self.pos:
                s = s+("|")
            elif i == 2:
                s = s+(",")
            else:
                s = s+(".")
        print s

robot = Robot(0,0,False)
print "Welcome to the Robot game!"
robot.printbot()
print "That is what the field looks like! A | is the robot, a , is the cube and a . is an empty meter of the field. The last dot is the goal! You win once you accumulate 20 points, good luck!"

while robot.score < 20:
    robot.printbot()
    print "Your score is ", robot.score
    print "Your robot's arm is at ", robot.armpos
    if robot.haspiece == True:
        print "Your robot has a cube!"
    goalpos = int(raw_input("How far would you like to move? "))
    goalarmpos = int(raw_input("How far would you like to move the arm? "))
    robot.move(goalpos)
    robot.armmove(goalarmpos)
    if robot.pos == 1 and robot.armpos == 0:
        pickupcube = str(raw_input("Would you like to pick up the cube? (y/n): "))
        if pickupcube == "y":
            robot.pickupcube()
    elif robot.pos == 6 and robot.armpos == 10:
        scorecube = str(raw_input("Would you like to score? (y/n): "))
        if scorecube == "y":
            robot.scorecube()
