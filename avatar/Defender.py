from Agent import *
from Winner import *

class Defender(Agent):
	"""docstring for Wall."""
	def __init__(self, environment, posX, posY, name):
		super(Defender, self).__init__(environment, posX, posY, name)
		self.color = "Blue"
		self.life = self.environment.data["defenderLife"]
		self.dead = False

	def decide(self):
		pass

	def die(self, nbDefenders):
		if nbDefenders == self.environment.data["nbDefenders"] :
			self.createWinner()
		self.breed()
		self.environment.killAgent(self)
		self.dead = True

	def breed(self):
		freeCells = self.environment.getFreeCells()
		random.shuffle(freeCells)
		position = freeCells.pop()
		newDefender = Defender(self.environment, position[0], position[1], None)
		self.environment.addAgent(newDefender, position[0], position[1])

	def createWinner(self):
		freeCells = self.environment.getFreeCells()
		random.shuffle(freeCells)
		position = freeCells.pop()
		winner = Winner(self.environment, position[0], position[1], None)
		self.environment.addAgent(winner, position[0], position[1])

	def starve(self):
		self.life -= 1
		if self.life < 0:
			self.die(-1)

	def update(self):
		self.starve()

	def isDead(self):
		return self.dead
