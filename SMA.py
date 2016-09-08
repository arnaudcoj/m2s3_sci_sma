import time

class SMA(object):
    """docstring for SMA."""
    def __init__(self, environment, delay, scheduling, nbTicks, trace, nbParticles, seed):
        super(SMA, self).__init__()
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.environment = environment

        self.populate(nbParticles, seed)


    def populate(self, nbParticles, seed):
        self.agentlist = []
        print(nbParticles, "particles have been created and placed on the grid with the seed :", seed)

    def run(self):
        for tick in range(1, self.nbTicks + 1):
            for agent in self.agentlist:
                #agent.decide()
                if self.trace: print("agent")
            if self.trace: print("Tick", tick, "on", self.nbTicks)
            time.sleep(self.delay / 1000.0)
