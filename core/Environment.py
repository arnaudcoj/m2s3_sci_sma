class Environment(object):
    """docstring for Environment"""
    def __init__(self, gridSizeX, gridSizeY, torus):
        super(Environment, self).__init__()
        self.initGrid(gridSizeX, gridSizeY, torus)

    def initGrid(self, gridSizeX, gridSizeY, torus):
        self.grid = []
        for i in range(gridSizeX):
            self.grid.append([None] * gridSizeY)

    def setInCell(self, x, y, obj):
        self.grid[x][y] = obj

    def getFreeCells(self):
        freeCells = []
        for i in range(self.getNbCol()):
            for j in range(self.getNbRow()):
                if self.grid[i][j] == None:
                    freeCells.append((i,j))
        return freeCells

    def getNbRow(self):
        return len(self.grid[0])

    def getNbCol(self):
        return len(self.grid)

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