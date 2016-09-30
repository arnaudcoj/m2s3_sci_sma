from Agent import *
from Observable import *
from Defender import *
from Winner import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener
        self.avatarNotifier = AvatarNotifier(environment)
        self.nbDefenders = 0
        self.dead = False

        self.tick = 0

    def decide(self):
        speedAvatar = self.environment.data["speedAvatar"]
        if (self.tick % speedAvatar) == 0:
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

    def eat(self):
        coords = self.findNextCell()
        if coords :
            nextCellAgent = self.environment.grid[coords[0]][coords[1]]
            if nextCellAgent and type(nextCellAgent) == Defender and not nextCellAgent.isDead() :
                self.nbDefenders += 1
                nextCellAgent.die(self.nbDefenders)
            elif nextCellAgent and type(nextCellAgent) == Winner and not nextCellAgent.isDead() :
                raise NotImplementedError("end of the game, to be implemented")

    def die(self):
        self.environment.killAgent(self)
        self.dead = True

    def isDead(self):
        return self.dead

    def update(self):
        if not self.isDead() :
            speedAvatar = self.environment.data["speedAvatar"]
            if (self.tick % speedAvatar) == 0:
                self.eat()
                self.move()
                self.computeDijkstraMatrix()
            self.tick += 1

    def computeDijkstraMatrix(self):
        width = self.environment.getNbCol()
        height = self.environment.getNbRow()
        grid = self.environment.grid
        cpt = 1

        matrix = []
        for i in range(width):
            matrix.append([None] * height)
        matrix[self.posX][self.posY] = 0

        fringe = self.environment.getVonNeumannNeighbors(self.posX,self.posY)

        while fringe:
            nextFringe = []
            for cell in fringe:
                x = cell[0]
                y = cell[1]
                if grid[x][y] == None and matrix[x][y] == None:
                    matrix[x][y] = cpt
                    nextFringe.extend(self.environment.getVonNeumannNeighbors(x,y))
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
