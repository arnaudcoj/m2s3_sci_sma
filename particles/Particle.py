import random

# Main.py should have added ../core to the include paths
from Agent import *

class Particle(Agent):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, name):
        super(Particle, self).__init__(environment, posX, posY, name)
        self.setRandomColor()
        self.setRandomPas()

    def decide(self):
        nextCoords = self.findNextCell()
        dirChanged = False

        if(nextCoords) :
            nextCell = self.environment.grid[nextCoords[0]][nextCoords[1]]
            #There is an agent on the next cell
            if nextCell :
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

    def update(self):
        self.move()
