import random

DONUT_REWARD = 10
TILE_REWARD = -10
WALL_REWARD = -1
STEP_REWARD = 0


class world:
    def __init__(self):
        self.map = self.getMap()
        self.donutSet = False
        self.donutPos = (-1, -1)

    def getMap(self):
        """
        Creates the map given in the assignment
        :return: The map as a string
        """
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

    def timeStep(self, xPos, yPos, direction):
        """
        Take a single move time step placing donuts and moving the bot
        :param xPos: x position of the bot
        :param yPos: y position of the bot
        :param direction:  direction the bot is trying to move
        :return: 
        """
        self.placeDonut()
        reward, moveSuccess = self.posReward(xPos, yPos, direction)

        # Check to make sure move was successful
        if moveSuccess:
            xPos, yPos = calculatePos(xPos, yPos, direction)

        return reward, xPos, yPos

    def posReward(self, xPos, yPos, direction):
        """
        Calculates the reward for the position
        :param xPos: x position of the bot
        :param yPos: y position of the bot
        :param direction: direction the bot is moving
        :return: The reward as an integer and a boolean to indicate if move 
                 was successful 
        """
        # Gets new position
        xPos, yPos = calculatePos(xPos, yPos, direction)

        # Gets a donut
        if (yPos, xPos) == self.donutPos and self.donutSet:
            self.donutPos = (-1, -1)
            self.donutSet = False
            return DONUT_REWARD, True

        # Check if hit by a tile
        elif self.map[yPos][xPos] == "T":
            coinFlip = random.randint(0, 1)
            if coinFlip == 1:
                return TILE_REWARD, True

        # Check if runs into wall
        elif self.map[yPos][xPos] == "W":
            return WALL_REWARD, False

        return STEP_REWARD, True

    def placeDonut(self):
        """
        Attempts to place a donut if a donut is not placed yet setting the donut
        position and donut set boolean for the world
        :return: None
        """
        if not self.donutSet:
            donutPlace = random.randint(0, 3)
            if donutPlace == 0:
                donutLoc = random.randint(0, 3)
                if donutLoc == 0:
                    self.donutPos = (1, 1)
                elif donutLoc == 1:
                    self.donutPos = (1, 8)
                elif donutLoc == 2:
                    self.donutPos = (8, 1)
                elif donutLoc == 3:
                    self.donutPos = (8, 8)

                self.donutSet = True

    def printArrowMap(self, memory):
        """
        Prints to std an arrow map indicating which direction the bot is trying to move
        :param memory: The values of the bot
        :return: None
        """
        for i in range(0, 10):
            yPos = i
            for j in range(0, 10):
                xPos = j
                if self.map[yPos][xPos] == "W":
                    print(" W ", end="")
                else:
                    rewards = memory[(yPos, xPos)]

                    maxValue = max(rewards)
                    maxIndex = [k for k, x in enumerate(rewards) if x == maxValue]

                    if len(maxIndex) >= 2:
                        print(" _ ", end="")
                    else:
                        if maxIndex[0] == 0:
                            print(" \u2191 ", end="")
                        elif maxIndex[0] == 1:
                            print(" \u2193 ", end="")
                        elif maxIndex[0] == 2:
                            print(" \u2190 ", end="")
                        elif maxIndex[0] == 3:
                            print(" \u2192 ", end="")
            print(" ")

    def printValueMap(self, memory):
        """
        Prints the expected reward value of each square
        :param memory: The values of the bot
        :return: None
        """
        for i in range(0, 10):
            yPos = i
            for j in range(0, 10):
                xPos = j
                if self.map[yPos][xPos] == "W":
                    print("   WWWW   ", end="\t")
                else:
                    temp = '{: .3e}'.format((max(memory[(yPos, xPos)])))
                    print(temp, end="\t")
            print(" ")


    def printRewardMatrix(self, memory):
        for i in range(0, 10):
            for j in range(0, 10):
                temp ='{: .3e}'.format((max(memory[(i, j)])))
                print(temp, end="\t")
            print(" ")


def calculatePos(xPos, yPos, direction):
    """
    Calculates the new position given a direction
    :param xPos: Current x position
    :param yPos: Current y position
    :param direction:  Direction moving
    :return: Tuple of form (x,y)
    """
    if direction == "UP":
        yPos += 1
    elif direction == "DOWN":
        yPos -= 1
    elif direction == "LEFT":
        xPos -= 1
    elif direction == "RIGHT":
        xPos += 1

    return xPos, yPos
