import random
from world import calculatePos

FAIL_CHANCE = 18
LEARNING_RATE = .01
DISCOUNT_FACTOR = .01


def directionToNumber(direction):
    """
    Returns the list position of a direction
    :param direction: Direction as UP, DOWN, LEFT, RIGHT
    :return: An integer index 0-3
    """
    if direction == "UP":
        return 0
    elif direction == "DOWN":
        return 1
    elif direction == "LEFT":
        return 2
    elif direction == "RIGHT":
        return 3


class bot:
    def __init__(self):
        self.memory = self.defaultMemory()
        self.xPos = -1
        self.yPos = -1

    def defaultMemory(self):
        """
        Creates a blank Q[s][a] state for a 10 x 10 map with 4 directions
        :return: Dictionary containing 4 length list for every (y,x) position
        """
        memoryList = []
        memDict = {}
        for i in range(0, 10):
            for j in range(0, 10):
                memoryList.append((i, j))

        for state in memoryList:
            memDict[state] = [0, 0, 0, 0]

        return memDict

    def updatePos(self, xPos, yPos):
        """
        Updates the x and y position of the bot
        :param xPos: New x position
        :param yPos: New y position
        :return: None
        """
        self.xPos = xPos
        self.yPos = yPos

    def getDirection(self):
        """
        Returns the new direction to take based on the current state
        :return: Direction to take as either UP, DOWN, LEFT, RIGHT
        """
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]

        rewards = self.memory[(self.yPos, self.xPos)]

        # In case of multiple directions with the same reward
        maxValue = max(rewards)
        maxIndex = [i for i, x in enumerate(rewards) if x == maxValue]

        directionPicked = direction[random.choice(maxIndex)]

        # Check if he fails to move the selected direction
        if FAIL_CHANCE >= random.randint(1, 100):
            direction.remove(directionPicked)
            return random.choice(direction)
        else:
            return directionPicked

    def updateReward(self, xPos, yPos, direction, reward):
        """
        Updates the reward for the given x, y position in the bot's memory
        :param xPos: Current x position
        :param yPos: Current y position
        :param direction: Direction the bot tried to move
        :param reward: How much the bot was rewarded on the move
        :return: None
        """
        memory = self.memory[(yPos, xPos)]
        value = memory[directionToNumber(direction)]
        value = value + LEARNING_RATE * (reward + DISCOUNT_FACTOR * self.getMax(xPos, yPos, direction) - value)
        memory[directionToNumber(direction)] = value

        self.memory[(yPos, xPos)] = memory

    def getMax(self, xPos, yPos, direction):
        """
        Returns the max reward available at the x and y position plus the given direction
        :param xPos: Current x position
        :param yPos: Current y position
        :param direction: Direction the bot is moving towards
        :return: Max value at the position moving towards
        """
        xPos, yPos = calculatePos(xPos, yPos, direction)
        return max(self.memory[(yPos, xPos)])

    def printMemory(self):
        """
        Prints the memory in an unsorted order
        :return: None
        """
        for i in list(self.memory):
            print(i, self.memory[i])
