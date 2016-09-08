import time
from Observable import *

class SMA(Observable):
    """docstring for SMA."""
    def __init__(self, window, environment, agentlist, delay, scheduling, nbTicks, trace):
        super(SMA, self).__init__()
        self.window = window
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.environment = environment
        self.agentlist = agentlist

    def run(self):
        #self.environment.printASCII()
        self.window.update_idletasks()
        self.window.update()
        for tick in range(1, self.nbTicks + 1):
            if self.trace: print("Tick", tick, "on", self.nbTicks)
            for agent in self.agentlist:
                agent.decide()
                agent.update()
                if self.trace: print("agent", agent)
                self.emitSignal("modelUpdated")
                self.window.update_idletasks()
                self.window.update()
            time.sleep(self.delay / 1000.0)
        self.window.mainloop()