from Agent import *
from Observer import *
from Avatar import *

class Hunter(Agent):
	"""docstring for Hunter."""
	def __init__(self, environment, posX, posY, name):
		super(Hunter, self).__init__(environment, posX, posY, name)
		self.avatarFollower = AvatarFollower()
		self.color = "Red"

	def decide(self):
		targetX = self.posX
		targetY = self.posY
		matrix = self.avatarFollower.dijkstraMatrix

		if self.avatarFollower.dijkstraMatrix != None :
			for cell in self.environment.getMooreNeighbors(self.posX, self.posY):
				x = cell[0]
				y = cell[1]

				if matrix[x][y] == 0:
					nextCellAgent = self.environment.grid[coords[x]][coords[y]]
					if nextCellAgent and type(nextCellAgent) == Avatar and not nextCellAgent.isDead() :
						nextCellAgent.die()
						raise NotImplementedError("end of the game, to be implemented")

				if matrix[targetX][targetY] == None or (matrix[x][y] != None and matrix[x][y] < matrix[targetX][targetY]):
					targetX = x
					targetY = y

		self.pasX = targetX - self.posX
		self.pasY = targetY - self.posY

	def update(self):
		self.move()

class AvatarFollower(Observer):
	"""docstring for AvatarFollower."""
	def __init__(self):
		super(AvatarFollower, self).__init__()
		self.dijkstraMatrix = None
		self.signalFunc = {"avatarUpdated":self.onAvatarUpdated}

	def onAvatarUpdated(self, avatar):
		self.dijkstraMatrix = avatar.dijkstraMatrix
