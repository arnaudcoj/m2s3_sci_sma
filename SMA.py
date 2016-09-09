import time
from Observable import *

class SMA(Observable):
    """docstring for SMA."""
    def __init__(self, environment, agentlist, delay, scheduling, nbTicks, trace):
        super(SMA, self).__init__()
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.environment = environment
        self.agentlist = agentlist

    def run(self):
        self.emitSignal("modelUpdated")
        for tick in range(1, self.nbTicks + 1):
            time.sleep(self.delay / 1000.0)
            if self.trace: print("Tick", tick, "on", self.nbTicks)
            for agent in self.agentlist:
                agent.decide()
                agent.update()
                if self.trace: print("agent", agent)
                self.emitSignal("modelUpdated")