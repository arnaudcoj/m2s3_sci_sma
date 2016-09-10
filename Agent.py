import random

class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, torus):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.name = posX + posY
        self.torus = torus
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
        print("posX:",self.posX)
        print("posY:",self.posY)
        nextCoords = self.findNextCell()
        print("nextCoords:", nextCoords)
        if(nextCoords != None) :
            nextCell = self.environment.grid[nextCoords[0]][nextCoords[1]]
            #There is an agent on the next cell
            if nextCell != None :
                print("occupied")
                newPasX = nextCell.pasX
                newPasY = nextCell.pasY

                nextCell.pasX = self.pasX
                nextCell.pasY = self.pasY

                self.pasX = newPasX
                self.pasY = newPasY
        #the environment is not toric and the marble is on its edge
        else :
            #the border is on the top or the bottom
            if (self.posY + self.pasY < 0) or (self.posY + self.pasY >= self.environment.getNbRow()) :
                print("None + Top / Bottom")
                self.pasY = -self.pasY
            #the border is on the left or the right
            if (self.posX + self.pasX < 0) or (self.posX + self.pasX >= self.environment.getNbCol()) :
                print("None + Left / Right")
                self.pasX = -self.pasX

    def findNextCell(self):
        nextCellX = self.posX + self.pasX
        nextCellY = self.posY + self.pasY

        #the marble is on the edge of the environment
        if (nextCellY < 0) or (nextCellY >= self.environment.getNbRow() - 1) or (nextCellX < 0) or (nextCellX >= self.environment.getNbCol() - 1) :
            #the environment is toric
            if self.torus :
                if self.posY + self.pasY < 0 :
                    print(self.name, "Y O")
                    nextCellY = self.environment.getNbRow() - 1
                elif self.posY + self.pasY >= self.environment.getNbRow() :
                    print(self.name, "Y 1")
                    nextCellY = 0

                if self.posX + self.pasX < 0 :
                    print(self.name, "X O")
                    nextCellX = self.environment.getNbCol() - 1
                elif self.posX + self.pasX >= self.environment.getNbCol() :
                    print(self.name, "X 1")
                    nextCellX = 0
            #If the environment is not toric
            else :
                return None

        return (nextCellX, nextCellY)


    def move(self):
        print("pasX:",self.pasX)
        print("pasY:",self.pasY)
        newPosX = self.posX + self.pasX
        newPosY = self.posY + self.pasY

        #The environment is toric
        if self.torus :
            #The marble touches the top border
            if self.posY + self.pasY < 0 :
                newPosY = self.environment.getNbRow() - 1
            #The marble touches the bottom border
            elif self.posY + self.pasY >= self.environment.getNbRow() :
                newPosY = 0

            #The marble touches the left border
            if self.posX + self.pasX < 0 :
                newPosX = self.environment.getNbCol() -1
            #The marble touches the right border
            elif self.posX + self.pasX >= self.environment.getNbCol() :
                newPosX = 0

        print("newPosX:",newPosX)
        print("newPosY:",newPosY)
        #moves only if the next cell is empty
        if self.environment.grid[newPosX][newPosY] == None :
            self.environment.setInCell(self.posX, self.posY, None)
            self.environment.setInCell(newPosX, newPosY, self)

            self.posX = newPosX
            self.posY = newPosY
