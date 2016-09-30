from Agent import *

class Winner(Agent):
	"""docstring for Wall."""
	def __init__(self, environment, posX, posY, name):
		super(Winner, self).__init__(environment, posX, posY, name)
		self.color = "Yellow"
		self.dead = False

	def decide(self):
		pass

	def update(self):
		pass
	 
	def isDead(self):
		return self.dead