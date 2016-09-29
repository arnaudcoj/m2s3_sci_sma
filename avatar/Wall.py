from Agent import *

class Wall(Agent):
    """docstring for Wall."""
    def __init__(self, environment, posX, posY, name):
        super(Wall, self).__init__(environment, posX, posY, name)
        self.color = "Brown"

    def decide(self):
        pass

    def update(self):
        pass
