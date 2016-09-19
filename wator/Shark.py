from Agent import *
from Fish import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name, data):
        super(Shark, self).__init__(environment, posX, posY, name, data)
        self.breedTime = data["sharkBreedTime"]
        self.starveTime = data["sharkStarveTime"]
        self.currentStarveTime = starveTime
        self.color = "Pink"

    def decide(self):
        raise NotImplementedError("Shark.decide needs to be implemented")

    def starve(self):
        if self.currentStarveTime == 0:
            self.die()
        else:
            self.currentStarveTime -= 1

    def isDead(self):
        raise NotImplementedError("Shark.isDead needs to be implemented")


    def eat(self):
        nextCell = self.findNextCell()
        nextCellAgent = self.environment.grid[nextCell[0]][nextCell[1]]
        if nextCellAgent != None and nextCellAgent.type == Fish:
            #the shark eats
            self.environment.setInCell(nextCell[0], nextCell[1], None)
            self.currentStarveTime = self.starveTime


    def move(self):
        raise NotImplementedError("Shark.move needs to be implemented")

    def breed(self):
        raise NotImplementedError("Shark.breed needs to be implemented")

    def update(self):
        self.starve()
        self.eat()
        self.move()
        self.breed()
