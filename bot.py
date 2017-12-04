import random

class bot:
    def __init__(self):
        self.memory = []
        self.xPos = -1
        self.yPos = -1

    def updatePos(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def getDir(self):
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]
        return random.choice(direction)