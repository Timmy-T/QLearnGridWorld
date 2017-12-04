import random

DONUT_REWARD = 10
TILE_REWARD = -10
WALL_REWARD = -1
STEP_REWARD = 0

class world:
    def __init__(self):
        self.map = self.getMap()
        self.donutSet = False
        self.donutPos = (-1,-1)


    def getMap(self):
        myMap = """
        WWWWWWWWWW
        WD_T____DW
        W_W_WWWT_W
        W_W_T____W
        W_W___W__W
        W_T___W__W
        W___WTWT_W
        W_T_W____W
        WD__W___DW
        WWWWWWWWWW
        """

        myArray = myMap.split()
        return myArray

    def timeStep(self, xPos, yPos, dir):
        self.placeDonut()
        reward, moveSuccess = self.posReward(xPos, yPos, dir)

        # Check to make sure move was successful
        if moveSuccess:
            xPos, yPos = self.calculatePos(xPos, yPos, dir)

        return reward, xPos, yPos

    def posReward(self, xPos, yPos, dir):
        # Gets new position
        xPos, yPos = self.calculatePos(xPos, yPos, dir)

        # Gets a donut
        if(yPos, xPos) == self.donutPos and self.donutSet:
            self.donutPos = (-1,-1)
            self.donutSet = False
            return DONUT_REWARD,True

        # Check if hit by a tile
        elif self.map[yPos][xPos] == "T":
            coinFlip = random.randint(0,1)
            if coinFlip == 1:
                return TILE_REWARD, True

        # Check if runs into wall
        elif self.map[yPos][xPos] == "W":
            return WALL_REWARD,False

        return STEP_REWARD, True

    def placeDonut(self):
        if not self.donutSet:
            donutPlace = random.randint(0,3)
            if donutPlace == 0:
                donutLoc = random.randint(0,3)
                if donutLoc == 0:
                    self.donutPos = (1,1)
                elif donutLoc == 1:
                    self.donutPos = (1,8)
                elif donutLoc == 2:
                    self.donutPos = (8,1)
                elif donutLoc == 3:
                    self.donutPos = (8,8)

                self.donutSet = True


    def calculatePos(self, xPos, yPos, dir):
        if dir == "UP":
            yPos += 1
        elif dir == "DOWN":
            yPos -= 1
        elif dir == "LEFT":
            xPos -= 1
        elif dir == "RIGHT":
            xPos += 1

        return xPos, yPos