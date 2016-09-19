import random

class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, name):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.pasX = 0
        self.pasY = 0
        self.name = name
        self.torus = self.environment.data["torus"]
        self.trace = self.environment.data["trace"]

    def setRandomColor(self):
        de = ("%02x" %random.randint(0,255))
        re = ("%02x" %random.randint(0,255))
        we = ("%02x" %random.randint(0,255))
        ge = "#"
        self.color = ge + de + re + we

    def setRandomPas(self):
        # maybe a bit gridy but we want to avoid a (0,0) direction
        pasList = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        self.setRandomPasIn(pasList)

    def setRandomPasIn(self, pasList) :
        random.shuffle(pasList)
        pas = pasList[0]
        self.pasX = pas[0]
        self.pasY = pas[1]

    def getDirectionsToFreeNeighbors(self):
        directions = []
        pasList = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for pas in pasList :
            print("pasX", pas[0])
            print("pasY", pas[1])
            nextCoords = self.findNextCellFromPas(pas[0], pas[1])
            print("posX", self.posX)
            print("posY", self.posY)
            print("coords", nextCoords)
            if(nextCoords) :
                nextCell = self.environment.grid[nextCoords[0]][nextCoords[1]]
                if nextCell :
                    directions.append(pas)
        return directions
        
    def update(self):
        raise NotImplementedError("Agent.update needs to be implemented")

    def decide(self):
        raise NotImplementedError("Agent.decide needs to be implemented")

    def findNextCellFromPas(self, pasX, pasY):
        nextCellX = self.posX + self.pasX
        nextCellY = self.posY + self.pasY

        #the marble is on the edge of the environment
        if (nextCellY < 0) or (nextCellY >= self.environment.getNbRow()) or (nextCellX < 0) or (nextCellX >= self.environment.getNbCol()) :
            #the environment is toric
            if self.torus :
                if self.posY + pasY < 0 :
                    nextCellY = self.environment.getNbRow() - 1
                elif self.posY + pasY >= self.environment.getNbRow() :
                    nextCellY = 0

                if self.posX + pasX < 0 :
                    nextCellX = self.environment.getNbCol() - 1
                elif self.posX + pasX >= self.environment.getNbCol() :
                    nextCellX = 0
            #If the environment is not toric
            else :
                return None

        return (nextCellX, nextCellY)

    def findNextCell(self):
        self.findNextCellFromPas(self.pasX, self.pasY)

    def move(self):
        nextCoords = self.findNextCell()

        #moves only if there is a next cell
        if nextCoords :
            newPosX = nextCoords[0]
            newPosY = nextCoords[1]

            #moves only if the next cell is empty
            if self.environment.grid[newPosX][newPosY] == None :
                self.environment.setInCell(self.posX, self.posY, None)
                self.environment.setInCell(newPosX, newPosY, self)

                self.posX = newPosX
                self.posY = newPosY

    def printTrace(self):
        print(self.name, self.posX, self.posY, self.pasX, self.pasY, sep=",")
