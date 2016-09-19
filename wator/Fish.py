from Agent import *

class Fish(Agent):
    def __init__(self, environment, posX, posY, name):
        super(Fish, self).__init__(environment, posX, posY, name)
        self.breedTime = self.environment.data["fishBreedTime"]
        self.currentBreedTime = 0
        self.previousX = self.posX
        self.previousY = self.posY
        self.color = "Green"

    def decide(self):
        freeNeighbors = self.getDirectionsToFreeNeighbors()
        if freeNeighbors :
            self.setRandomPasIn(freeNeighbors)

    def breed(self):
        if (self.previousX != self.posX or self.previousY != self.posY) and self.currentBreedTime >= self.breedTime :
            baby = Fish(self.environment, self.previousX, self.previousY, str(self.name) + '.1')
            self.environment.setInCell(self.previousX, self.previousY, baby)
            self.currentBreedTime = 0
        else :
            self.currentBreedTime += 1

    def update(self):
        self.color = "Blue"
        self.previousX = self.posX
        self.previousY = self.posY
        self.move()
        self.breed()
        self.previousX = self.posX
        self.previousY = self.posY

