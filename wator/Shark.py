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

    def findFishDirection(self):
        pasList = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        random.shuffle(pasList)
        for pas in pasList :
            coords = self.findNextCellFromPas(pas[0], pas[1])
            if(coords) :
                cell = self.environment.grid[coords[0]][coords[1]]
                if cell :
                    return pas
        return None

    def decide(self):
        direction = self.findFishDirection()
        if direction == None :
            freeNeighbors = self.getDirectionsToFreeNeighbors()
            if freeNeighbors :
                self.setRandomPasIn(freeNeighbors)
        else :
            self.pasX = direction[0]
            self.pasY = direction[1]

    def starve(self):
        self.currentStarveTime -= 1

    def eat(self):
        nextCell = self.findNextCell()
        nextCellAgent = self.environment.grid[nextCell[0]][nextCell[1]]
        if nextCellAgent != None and type(nextCellAgent) == Fish:
            #the shark eats
            nextCellAgent.die()
            self.currentStarveTime = self.starveTime
        elif self.currentStarveTime < 0:
            self.die()

    def breed(self):
        if (self.previousX != self.posX or self.previousY != self.posY) and self.currentBreedTime >= self.breedTime :
            baby = Shark(self.environment, self.previousX, self.previousY, str(self.name) + '.1')
            self.environment.addAgent(baby, self.previousX, self.previousY)
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
        return self.currentStarveTime < 0
