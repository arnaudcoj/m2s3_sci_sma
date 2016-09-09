import time
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

    def run(self):
        self.emitSignal("modelUpdated")
        if self.tick <= self.nbTicks :
            if self.trace: print("Tick", self.tick , "on", self.nbTicks)
            for agent in self.agentlist:
                agent.decide()
                agent.update()
                if self.trace: print("agent", agent)
                self.emitSignal("modelUpdated")
            self.tick += 1
