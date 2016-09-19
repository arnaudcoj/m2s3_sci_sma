from Agent import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name, torus, trace):
        super(Shark, self).__init__(environment, posX, posY, name, torus, trace)

    def create(self):
        raise NotImplementedError("Agent.create needs to be implemented")

    def decide(self):
        raise NotImplementedError("Agent.decide needs to be implemented")
