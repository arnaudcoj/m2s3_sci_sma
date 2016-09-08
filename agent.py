class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, color, torus):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.color = color
        self.torus = torus

        self.pasY = 1
        self.pasX = 1

    def update():
    	decide()
    	move()

    def decide():
        if nextCell != None :
            newPasY = nextCell.agent.pasY
            newPasX = nextCell.agent.pasX

            nextCell.agent.pasY = self.pasY
            nextCell.agent.pasX = self.pasX

            self.pasY = newPasY
            self.pasX = newPasX
        elif !self.torus :
            if (posY + self.pasY < 0 || posY + self.pasY > environment.getNbRow) :
                self.pasX -= self.pasX
            if (posX + self.pasX < 0 || posX + self.pasX > environment.getNbCol) :            
                self.pasY -= self.pasY

    def find_nextCell():
        nextCellY = self.posY + self.pasY
        nextCellX = self.posX + self.pasX

        if self.torus :
            if self.posY + self.pasY < 0 :
                self.posY = environment.getNbRow
            elif self.posY + self.pasY > environment.getNbRow : 
                self.posY = 0

            if self.posX + self.pasX < 0 :
                self.posX = environment.getNbCol
            elif self.posX + self.pasX > environment.getNbCol : 
                self.posX = 0

        nextCell = environment.grid[nextCellY][nextCellX]


    def move():
        if self.torus :
            if self.posY + self.pasY < 0 :
                self.posY = environment.getNbRow
            elif self.posY + self.pasY > environment.getNbRow : 
                self.posY = 0

            if self.posX + self.pasX < 0 :
                self.posX = environment.getNbCol
            elif self.posX + self.pasX > environment.getNbCol : 
                self.posX = 0
        else :
        	self.posY += self.pasY
            self.posX += self.pasX