import random
from world import calculatePos

FAIL_CHANCE = 18
LEARNING_RATE = .01
DISCOUNT_FACTOR = .01

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

    def getDirection(self):
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]

        rewards = self.memory[(self.yPos, self.xPos)]

        # In case of multiple directions with the same reward
        maxValue = max(rewards)
        maxIndex =[i for i, x in enumerate(rewards) if x == maxValue]

        directionPicked = direction[random.choice(maxIndex)]

        # Check if he fails to move the selected direction
        if FAIL_CHANCE >= random.randint(1,100):
            direction.remove(directionPicked)
            return  random.choice(direction)
        else:
            return directionPicked

    def directionToNumber(self, direction):
        if direction == "UP":
            return 0
        elif direction == "DOWN":
            return 1
        elif direction == "LEFT":
            return 2
        elif direction == "RIGHT":
            return 3

    def updateReward(self, xPos, yPos, direction, reward):
        memory = self.memory[(yPos, xPos)]
        value = memory[self.directionToNumber(direction)]
        value =  value + LEARNING_RATE * (reward + DISCOUNT_FACTOR * self.getMax(xPos, yPos, direction) - value)
        memory[self.directionToNumber(direction)] = value

        self.memory[(yPos, xPos)] = memory


    def getMax(self, xPos, yPos, direction):
        xPos, yPos = calculatePos(xPos, yPos, direction)
        return max(self.memory[(yPos, xPos)])


    def printMemory(self):
        for i in list(self.memory):
            print(i, self.memory[i])
