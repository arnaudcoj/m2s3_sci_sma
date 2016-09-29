import random

class MapGenerator():
	def __init__(self):
		self.width = 20
		self.height = 10
		self.birthLimit = 4
		self.deathLimit = 3
		self.chanceToStartAlive = 0.45
		self.numberOfSteps = 2

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
 
	def initialiseMap(self, map):
		for x in range(self.width):
			for y in range(self.height):
				if (random.random() < self.chanceToStartAlive):
					map[x][y] = True

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
						newMap[x][y] = False
					else:
						newMap[x][y] = True

				#Otherwise, if the cell is dead now, check if it has the right number of neighbours to be 'born'
				else:
					if (nbs > self.birthLimit):
						newMap[x][y] = True
					else:
						newMap[x][y] = False

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

	def printASCII(self):
		#First Line
		print("+", end="")
		for i in range(self.width):
			print("-+", end="")

		#Intermediate Lines
		for j in range(self.height):
			print("\n|", end="")
			for i in range(self.width):
				if self.cellMap[i][j] == True:
					print("1", end="")
				else:
					print("0", end="")
				print("|", end="")
			print("\n+", end="")
			for i in range(self.width):
				print("-+", end="")

		#End
		print("")

mapGenerator = MapGenerator()
mapGenerator.generateMap()
mapGenerator.printASCII()