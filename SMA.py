class SMA(object):
    """docstring for SMA."""
    def __init__(self, environment, delay, scheduling, nbTicks, trace, nbParticles, seed):
        super(SMA, self).__init__()
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.trace = trace

        self.environment = environment

    def populate(self, nbParticles, seed):
        pass

    def run(self):
        for tick in range(nbTicks):
            for agent in agentlist:
                #agent.decide()
                print("agent")
            print("Tick", tick, "on", nbTicks)
            sleep(delay)
