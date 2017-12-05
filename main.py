from bot import *
from world import *

NUM_OF_ITERATIONS = 100000000

if __name__ == '__main__':
    tinnyT = bot()
    basement = world()

    # Initialize random position for bot
    while True:
        xPos = random.randint(0, 9)
        yPos = random.randint(0, 9)
        if basement.map[yPos][xPos] != "W":
            tinnyT.updatePos(xPos, yPos)
            break

    # Run for the number of iterations desired
    for i in range(NUM_OF_ITERATIONS):
        # Find the direction tinny wants to move
        direction = tinnyT.getDirection()

        # Find the reward and new position
        # The position could not change if a wall collision occurs
        reward, xPos, yPos = basement.timeStep(tinnyT.xPos, tinnyT.yPos, direction)

        # Update rewards and position
        tinnyT.updateReward(xPos, yPos, direction, reward)
        tinnyT.updatePos(xPos, yPos)

    basement.printValueMap(tinnyT.memory)
    basement.printArrowMap(tinnyT.memory)
