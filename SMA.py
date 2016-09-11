import time
import random
from Observable import *

class SMA(Observable):
    """docstring for SMA."""
    def __init__(self, environment, agentlist, scheduling, nbTicks, trace):
        super(SMA, self).__init__()
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.environment = environment
        self.agentlist = agentlist
        self.tick = 1

    def hasFinished(self):
        return self.nbTicks and self.tick > self.nbTicks

    def run(self):
        if not self.hasFinished() :
            if self.trace:
                print("Tick", self.tick , "on", self.nbTicks)
            agentlist = self.agentlist
            if self.scheduling == "random":
                random.shuffle(agentlist)
            for agent in agentlist:
                agent.decide()
                agent.update()
                self.emitSignal("modelUpdated")
            self.tick += 1
