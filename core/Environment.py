class Environment(object):
    """docstring for Environment"""
    def __init__(self, data, agentlist, walllist):
        super(Environment, self).__init__()
        self.data = data
        self.torus = data["torus"]
        self.agentlist = agentlist
        self.walllist = walllist
        self.initGrid()

    def initGrid(self):
        self.grid = []
        for i in range(self.data["gridSizeX"]):
            self.grid.append([None] * self.data["gridSizeY"])

    def setInCell(self, x, y, obj):
        self.grid[x][y] = obj

    def getFreeCells(self):
        freeCells = []
        for i in range(self.getNbCol()):
            for j in range(self.getNbRow()):
                if self.grid[i][j] == None:
                    freeCells.append((i,j))
        return freeCells

    def getMooreNeighbors(self, x, y):
        width = self.getNbCol()
        height = self.getNbRow()
        neighbors = []
        steps = [(0,1), (1,0), (0,-1), (-1,0)]
        torus = self.torus
        grid = self.grid

        for step in steps:
            nextCellX = x + step[0]
            nextCellY = y + step[1]
            neighbor = (nextCellX, nextCellY)

            if (nextCellY < 0) or (nextCellY >= height) or (nextCellX < 0) or (nextCellX >= width) :
                #the environment is toric
                if torus :
                    if nextCellY < 0 :
                        nextCellY = height - 1
                    elif nextCellY >= height :
                        nextCellY = 0

                    if nextCellX < 0 :
                        nextCellX = width - 1
                    elif nextCellX >= width :
                        nextCellX = 0
                    neighbor = (nextCellX, nextCellY)
                else:
                    neighbor = None

            if neighbor != None:
                neighbors.append(neighbor)
        return neighbors


    def getNbRow(self):
        return len(self.grid[0])

    def getNbCol(self):
        return len(self.grid)

    def killAgent(self, agent):
        self.setInCell(agent.posX, agent.posY, None)
        if agent in self.agentlist: #dont know why, we'll see this later
            self.agentlist.remove(agent)

    def addAgent(self, agent, posX, posY):
        self.setInCell(posX, posY, agent)
        self.agentlist.append(agent)

    def printASCII(self):
        #First Line
        print("+", end="")
        for i in range(self.getNbCol()):
            print("-+", end="")

        #Intermediate Lines
        for j in range(self.getNbRow()):
            print("\n|", end="")
            for i in range(self.getNbCol()):
                if self.grid[i][j] != None:
                    print(self.grid[i][j].name, end="")
                else:
                    print(" ", end="")
                print("|", end="")
            print("\n+", end="")
            for i in range(self.getNbCol()):
                print("-+", end="")

        #End
        print("")
