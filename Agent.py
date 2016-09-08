class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, color, torus):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.name = posX + posY
        self.color = color
        self.torus = torus

        self.pasY = 1
        self.pasX = 1

    def update(self):
        print("update")
        self.move()

    def decide(self):
        nextCell = self.findNextCell()
        if nextCell != None :
            newPasY = nextCell.agent.pasY
            newPasX = nextCell.agent.pasX

            nextCell.agent.pasY = self.pasY
            nextCell.agent.pasX = self.pasX

            self.pasY = newPasY
            self.pasX = newPasX
        elif not self.torus :
            if (posY + self.pasY < 0) or (posY + self.pasY >= self.environment.getNbRow) :
                self.pasX -= self.pasX
            if (posX + self.pasX < 0) or (posX + self.pasX >= self.environment.getNbCol) :
                self.pasY -= self.pasY

    def findNextCell(self):
        nextCellY = self.posY + self.pasY
        nextCellX = self.posX + self.pasX
        outOfBound = False

        if (self.posY + self.pasY < 0) or (self.posY + self.pasY >= self.environment.getNbRow()) or (self.posX + self.pasX < 0) or (self.posX + self.pasX >= self.environment.getNbCol()) :
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
            else :
                outOfBound = True

        if outOfBound :
            nextCell = None
        else :
            nextCell = self.environment.grid[nextCellY][nextCellX]


    def move(self):
        newPosY = self.posY + self.pasY
        newPosX = self.posX + self.pasX

        if self.torus :
            if newPosY + self.pasY < 0 :
                newPosY = self.environment.getNbRow()
            elif newPosY + self.pasY >= self.environment.getNbRow() :
                newPosY = 0

            if newPosX + self.pasX < 0 :
                newPosX = self.environment.getNbCol()
            elif newPosX + self.pasX >= self.environment.getNbCol() :
                newPosX = 0
        else :
            newPosY += self.pasY
            newPosX += self.pasX

        self.environment.setInCell(self.posX, self.posY, None)
        self.environment.setInCell(newPosX, newPosY, self)

        self.posY = newPosY
        self.posX = newPosX
