import random
import math
from bot import *
from world import *

NUM_OF_ITERATIONS = 10000000

if __name__ == '__main__':
    tinnyT = bot()
    basement = world()

    # Initiliaze random position for bot
    while True:
        xPos = random.randint(0,9)
        yPos = random.randint(0,9)
        if basement.map[yPos][xPos] != "W":
            tinnyT.updatePos(xPos, yPos)
            break

    for i in range(NUM_OF_ITERATIONS):
        direction = tinnyT.getDirection()
        reward, xPos, yPos = basement.timeStep(tinnyT.xPos, tinnyT.yPos, direction)
        tinnyT.updateReward(xPos, yPos, direction, reward)
        tinnyT.updatePos(xPos, yPos)


    tinnyT.printMemory()
    basement.printArrowMap(tinnyT.memory)
