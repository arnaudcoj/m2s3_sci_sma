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

    def update(self):
        self.move()

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
