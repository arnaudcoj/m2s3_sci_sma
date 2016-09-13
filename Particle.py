import random

from Agent import *

class Particle(Agent):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, name, torus, trace):
        super(Particle, self).__init__(environment, posX, posY, name, torus, trace)

    def create(self):
        self.setRandomColor()
        self.setRandomPas()

    def setRandomColor(self):
        de = ("%02x" %random.randint(0,255))
        re = ("%02x" %random.randint(0,255))
        we = ("%02x" %random.randint(0,255))
        ge = "#"
        self.color= ge + de + re + we

    def setRandomPas(self):
        # maybe a bit gridy but we want to avoid a (0,0) direction
        pasList = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        random.shuffle(pasList)
        pas = pasList[0]
        self.pasX = pas[0]
        self.pasY = pas[1]

    def decide(self):
        nextCoords = self.findNextCell()
        dirChanged = False

        if(nextCoords != None) :
            nextCell = self.environment.grid[nextCoords[0]][nextCoords[1]]
            #There is an agent on the next cell
            if nextCell != None :
                newPasX = nextCell.pasX
                newPasY = nextCell.pasY

                nextCell.pasX = self.pasX
                nextCell.pasY = self.pasY

                self.pasX = newPasX
                self.pasY = newPasY

                dirChanged = True
        #the environment is not toric and the marble is on its edge
        else :
            #the border is on the top or the bottom
            if (self.posY + self.pasY < 0) or (self.posY + self.pasY >= self.environment.getNbRow()) :
                self.pasY = -self.pasY
                dirChanged = True
            #the border is on the left or the right
            if (self.posX + self.pasX < 0) or (self.posX + self.pasX >= self.environment.getNbCol()) :
                self.pasX = -self.pasX
                dirChanged = True

        if self.trace and dirChanged:
            self.printTrace()
