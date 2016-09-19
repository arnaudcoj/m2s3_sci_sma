from Agent import *
from Fish import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name, data):
        super(Shark, self).__init__(environment, posX, posY, name, data)
        self.breedTime = data["sharkBreedTime"]
        self.starveTime = data["sharkStarveTime"]
        self.currentStarveTime = self.starveTime
        self.color = "Pink"

    def decide(self):
        raise NotImplementedError("Shark.decide needs to be implemented")

    def update(self):
        self.starve()
        self.eat()
        self.move()
        self.breed()

    def starve(self):
        self.currentStarveTime -= 1

    def eat(self):
        nextCell = self.findNextCell()
        nextCellAgent = self.environment.grid[nextCell[0]][nextCell[1]]
        if nextCellAgent != None and type(nextCellAgent) == Fish:
            #the shark eats
            self.environment.setInCell(nextCell[0], nextCell[1], None)
            self.currentStarveTime = self.starveTime

    def move(self):
        raise NotImplementedError("Shark.move needs to be implemented")

    def breed(self):
        raise NotImplementedError("Shark.breed needs to be implemented")
        
    def isDead(self):
        return self.currentStarveTime <= 0
