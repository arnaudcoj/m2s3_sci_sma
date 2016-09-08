class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, color):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.color = color

        self.pasY = 1
        self.pasX = 1

    def update():
    	decide()
    	move()

    def decide():
    	next_cell = environment.grid[posY + pasY][posX + pasX]
    	if next_cell.isOccupied :
            new_pasY = next_cell.agent.pasY
    		new_pasX = next_cell.agent.pasX

    		next_cell.agent.pasY = self.pasY
            next_cell.agent.pasX = self.pasX

    		self.pasY = new_pasY
            self.pasX = new_pasX

    def move():
    	self.posY += self.pasY
        self.posX += self.pasX