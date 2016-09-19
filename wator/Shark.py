from Agent import *
from Fish import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name):
        super(Shark, self).__init__(environment, posX, posY, name)
        self.breedTime = self.environment.data["sharkBreedTime"]
        self.starveTime = self.environment.data["sharkStarveTime"]
        self.currentStarveTime = self.starveTime
        self.currentBreedTime = 0
        self.previousX = self.posX
        self.previousY = self.posY
        self.color = "Pink"

    def decide(self):
        self.setRandomPas()

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

    def breed(self):
        if (self.previousX != self.posX or self.previousY != self.posY) and self.currentBreedTime >= self.breedTime :
            baby = Shark(self.environment, self.previousX, self.previousY, str(self.name) + '.1')
            self.environment.setInCell(self.previousX, self.previousY, baby)
            self.currentBreedTime = 0
        else :
            self.currentBreedTime += 1

    def update(self):
        self.color = "Red"
        self.starve()
        self.eat()
        self.move()
        self.breed()
        
    def isDead(self):
        return self.currentStarveTime <= 0
