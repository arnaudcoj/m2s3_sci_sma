class Agent(object):
    """docstring for Agent"""
    def __init__(self, environment, posX, posY, color):
        super(Agent, self).__init__()
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.color = color

        self.direction = (1,1)

    def update():
    	decide()
    	move()

    def decide():
    	next_cell = environment.grid[posY + direction.y][posX + direction.x]
    	if next_cell.isOccupied :
    		new_direction = next_cell.getAgent.getDirection()
    		next_cell.getAgent.setDirection(direction)
    		self.direction = new_direction

    def move():
    	self.posX += direction.x
    	self.posY += direction.y

