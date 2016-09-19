from Agent import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name):
        super(Shark, self).__init__(environment, posX, posY, name)
        self.breedTime = self.environment.data["sharkBreedTime"]
        self.starveTime = self.environment.data["sharkStarveTime"]
        self.currentBreedTime = 0
        self.previousX = self.posX
        self.previousY = self.posY
        self.color = "Pink"

    def decide(self):
        self.setRandomPas()

    def starve(self):
        pass

    def eat(self):
        pass

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
