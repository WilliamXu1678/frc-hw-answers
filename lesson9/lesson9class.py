class Robot:
    def __init__(self, pos, armpos, haspiece):
        self.pos = pos #int
        self.armpos = armpos #int
        self.haspiece = haspiece #bool
        self.score = 0

    def move(self,dist):
        if self.pos + dist > 7:
            self.pos = 7
        elif self.pos + dist < 0:
            self.pos = 0
        else:
            self.pos += dist

    def armmove(self,dist):
        self.armpos += dist

    def pickupcube(self):
        self.haspiece = True

    def scorecube(self):
        self.score += 5
        self.haspiece = False

    def printbot(self): #This function is extra fanciness because I was bored. You do NOT need to have this
        s = ""
        for i in range(0,8):
            if i == self.pos:
                s = s+("|")
            elif i == 3:
                s = s+(",")
            else:
                s = s+(".")
        print s
