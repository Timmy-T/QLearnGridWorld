import random
import math
from bot import *
from world import *


NUM_OF_ITERATIONS = 1000000

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

    totalReward = 0
    for i in range(NUM_OF_ITERATIONS):
        reward, xPos, yPos = basement.timeStep(tinnyT.xPos, tinnyT.yPos, tinnyT.getDir())
        print(reward, xPos, yPos, sep="\t")

        totalReward += reward

        tinnyT.updatePos(xPos, yPos)

    print(totalReward)