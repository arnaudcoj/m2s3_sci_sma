import random

class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, name, torus, trace):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.name = name
        self.torus = torus
        self.trace = trace
        self.create()

    def create(self):
        raise NotImplementedError("Agent.create needs to be implemented")

    def update(self):
        self.move()

    def decide(self):
        raise NotImplementedError("Agent.decide needs to be implemented")

    def findNextCell(self):
        nextCellX = self.posX + self.pasX
        nextCellY = self.posY + self.pasY

        #the marble is on the edge of the environment
        if (nextCellY < 0) or (nextCellY >= self.environment.getNbRow()) or (nextCellX < 0) or (nextCellX >= self.environment.getNbCol()) :
            #the environment is toric
            if self.torus :
                if self.posY + self.pasY < 0 :
                    nextCellY = self.environment.getNbRow() - 1
                elif self.posY + self.pasY >= self.environment.getNbRow() :
                    nextCellY = 0

                if self.posX + self.pasX < 0 :
                    nextCellX = self.environment.getNbCol() - 1
                elif self.posX + self.pasX >= self.environment.getNbCol() :
                    nextCellX = 0
            #If the environment is not toric
            else :
                return None

        return (nextCellX, nextCellY)


    def move(self):
        nextCoords = self.findNextCell()

        #moves only if there is a next cell
        if(nextCoords != None) :
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
