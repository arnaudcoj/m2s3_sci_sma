import time
import random
from Observable import *

class SMA(Observable):
    """docstring for SMA."""
    def __init__(self, environment, data):
        super(SMA, self).__init__()
        self.environment = environment
        self.data = data
        self.tick = 1

    def hasFinished(self):
        nbTicks = self.data["nbTicks"]
        return nbTicks and self.tick > nbTicks

    def run(self):
        pause = self.data["pause"]
        scheduling = self.data["scheduling"]
        trace = self.data["trace"]
        if not self.hasFinished() and not pause :
            agentlist = list(self.environment.agentlist)
            if scheduling == "random":
                random.shuffle(agentlist)
            for agent in agentlist:
                if not agent.isDead():
                    agent.decide()
                    agent.update()

            self.emitSignal("modelUpdated")
            self.tick += 1
