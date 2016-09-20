import time
import random
from Observable import *

class SMA(Observable):
    """docstring for SMA."""
    def __init__(self, environment, scheduling, nbTicks, trace):
        super(SMA, self).__init__()
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.environment = environment
        self.tick = 1

    def hasFinished(self):
        return self.nbTicks and self.tick > self.nbTicks

    def run(self):
        if not self.hasFinished() :
            if self.trace :
                print("Tick", self.tick , "on", self.nbTicks)
            agentlist = list(self.environment.agentlist)
            if self.scheduling == "random":
                random.shuffle(agentlist)
            for agent in agentlist:
                if not agent.isDead():
                    agent.decide()
                    agent.update()
            if self.trace:
                print("NbFishes", self.environment.nbFishes)
                print("NbSharks", self.environment.nbSharks)

            #print(self.tick, self.environment.nbFishes, self.environment.nbSharks, self.environment.nbFishes / self.environment.nbSharks, sep=",")

            self.emitSignal("modelUpdated")
            self.tick += 1
