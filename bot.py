import random

FAIL_CHANCE = 18

class bot:
    def __init__(self):
        self.memory = self.defaultMemory()
        self.xPos = -1
        self.yPos = -1

    def defaultMemory(self):
        memoryList = []
        memDict = {}
        for i in range(0,10):
            for j in range(0,10):
                memoryList.append((i,j))

        for state in memoryList:
            memDict[state] = [0,0,0,0]

        return memDict

    def updatePos(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def getDir(self):
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]
        return random.choice(direction)

    def directionNumber(self, dir):
        if dir == "UP":
            return 0
        elif dir == "DOWN":
            return 1
        elif dir == "LEFT":
            return 2
        elif dir == "RIGHT":
            return 3

    def updateReward(self, xPos, yPos, direction, reward):
        tempList = self.memory[(yPos, xPos)]
        tempList[self.directionNumber(direction)] += reward

        self.memory[(yPos, xPos)] = tempList


    def printMemory(self):
        for i in list(self.memory):
            print(i, self.memory[i])
