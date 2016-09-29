from Agent import *
from Observable import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener
        self.avatarNotifier = AvatarNotifier(environment)

    def decide(self):
        lastDirectionPressed = self.keyListener.lastDirectionPressed
        self.pasX = 0
        self.pasY = 0
        if lastDirectionPressed == 'Up':
            self.pasY -= 1
        elif lastDirectionPressed == 'Down':
            self.pasY += 1
        if lastDirectionPressed == 'Left':
            self.pasX -= 1
        elif lastDirectionPressed == 'Right':
            self.pasX += 1

    def update(self):
        self.move()
        self.computeDijkstraMatrix()

    def computeDijkstraMatrix(self):
        width = self.environment.getNbCol()
        height = self.environment.getNbRow()
        grid = self.environment.grid
        cpt = 1

        matrix = []
        for i in range(width):
            matrix.append([None] * height)
        matrix[self.posX][self.posY] = 0

        fringe = self.environment.getMooreNeighbors(self.posX,self.posY)

        while fringe:
            nextFringe = []
            for cell in fringe:
                x = cell[0]
                y = cell[1]
                if grid[x][y] == None and matrix[x][y] == None:
                    matrix[x][y] = cpt
                    nextFringe.extend(self.environment.getMooreNeighbors(x,y))
            cpt += 1
            fringe = nextFringe

        self.avatarNotifier.updateDijkstraMatrix(matrix)

class AvatarNotifier(Observable):
    """docstring for AvatarNotifier."""
    def __init__(self, environment):
        super(AvatarNotifier, self).__init__()
        self.environment = environment

    def updateDijkstraMatrix(self, matrix):
        self.dijkstraMatrix = matrix
        self.emitSignal("avatarUpdated")
