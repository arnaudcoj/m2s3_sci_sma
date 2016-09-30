import random

class MapGenerator():
	def __init__(self, environment):
		self.environment = environment
		self.width = self.environment.getNbCol()
		self.height = self.environment.getNbRow()
		self.birthLimit = self.environment.data["birthLimit"]
		self.deathLimit = self.environment.data["deathLimit"]
		self.chanceToStartAlive = self.environment.data["chanceToStartAlive"]
		self.numberOfSteps = self.environment.data["numberOfSteps"]

		self.nbCave = 0
		self.caves = []

	def generateMap(self):
		#Create a new map
		self.cellMap = []
		for i in range(self.width):
			self.cellMap.append([None] * self.height)

		#Set up the map with random values
		self.cellMap = self.initialiseMap(self.cellMap)

		#And now run the simulation for a set number of steps
		for i in range(self.numberOfSteps):
			self.cellMap = self.doSimulationStep(self.cellMap)

		self.epurate()
 
	def initialiseMap(self, map):
		for x in range(self.width):
			for y in range(self.height):
				if (random.random() < self.chanceToStartAlive):
					map[x][y] = 1

		return map

	def doSimulationStep(self, oldMap):
		newMap = []
		for i in range(self.width):
			newMap.append([None] * self.height)

		#Loop over each row and column of the map
		for x in range(len(oldMap)):
			for y in range(len(oldMap[0])):
				nbs = self.countAliveNeighbours(oldMap, x, y)

				#The new value is based on our simulation rules
				#First, if a cell is alive but has too few neighbours, kill it.
				if (oldMap[x][y]):
					if (nbs < self.deathLimit):
						newMap[x][y] = 0
					else:
						newMap[x][y] = 1

				#Otherwise, if the cell is dead now, check if it has the right number of neighbours to be 'born'
				else:
					if (nbs > self.birthLimit):
						newMap[x][y] = 1
					else:
						newMap[x][y] = 0

		return newMap

	#Returns the number of cells in a ring around (x,y) that are alive.
	def countAliveNeighbours(self, map, x, y):
		count = 0

		for i in range(-1, 2):
			for j in range(-1, 2):
				neighbour_x = x + i
				neighbour_y = y + j

				#If we're looking at the middle point
				if (i == 0 and j == 0):
					#Do nothing, we don't want to add ourselves in!
					pass

				#In case the index we're looking at it off the edge of the map
				elif (neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(map) or neighbour_y >= len(map[0])):
					count = count + 1

				#Otherwise, a normal check of the neighbour
				elif (map[neighbour_x][neighbour_y]):
					count = count + 1

		return count

	def epurate(self):
		emptyCell = self.findEmptyCell()
		while emptyCell :
			self.nbCave += 1
			self.caves.append(0)
			self.floodfill(emptyCell[0], emptyCell[1], 0, self.nbCave + 1)
			emptyCell = self.findEmptyCell()
		
		print(self.nbCave)
		for x in range(self.nbCave):
			print(self.caves[x])

		biggestCave = 0
		for x in range(self.nbCave):
			if self.caves[x] > self.caves[biggestCave] :
				biggestCave = x

		print(biggestCave)
		for x in range(self.width):
			for y in range(self.height):
				if self.cellMap[x][y] != biggestCave + 2 :
					self.cellMap[x][y] = 1

	def findEmptyCell(self):
		for x in range(self.width):
			for y in range(self.height):
				if self.cellMap[x][y] == 0 :
					return (x,y)
		return None

	def floodfill(self, x, y, oldNb, newNb):
		if self.cellMap[x][y] != oldNb : # the base case
			return
		
		self.cellMap[x][y] = newNb
		self.caves[self.nbCave - 1] += 1

		if x < self.width -1 :
			self.floodfill(x + 1, y, oldNb, newNb) # right

		if x > 0 :
			self.floodfill(x - 1, y, oldNb, newNb) # left

		if y < self.height - 1 :
			self.floodfill(x, y + 1, oldNb, newNb) # down

		if y > 0 :
			self.floodfill(x, y - 1, oldNb, newNb) # up