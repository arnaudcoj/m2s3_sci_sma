import json

import Environment

class Main(object):
    """docstring for Main"""
    def __init__(self, fileName):
        super(Main, self).__init__()
        self.load_properties_from_json(fileName)
        self.createEnvironment()
        self.populate()
        self.createSMA()

    def load_properties_from_json(self, fileName):
        dataFile = open(fileName, 'r')
        try:
            self.data = json.loads(dataFile.read())
        finally:
            dataFile.close()
            print("Properties from", fileName, "successfully loaded.")

    def createEnvironment(self):
        gridSizeX = self.data["gridSizeX"]
        gridSizeY = self.data["gridSizeY"]
        torus = self.data["torus"]

        self.environment = Environment(gridSizeX, gridSizeY, torus)

    def createSMA(self):
        environment = self.data["environment"]
        delay = self.data["delay"]
        scheduling = self.data["scheduling"]
        nbTicks = self.data["nbTicks"]
        trace = self.data["trace"]
        nbParticles = self.data["nbParticles"]
        seed = self.data["seed"]

        self.SMA = SMA(environment, delay, scheduling, nbTicks, trace, nbParticles, seed)

def main():
    main = Main("properties.json")

if __name__ == '__main__':
    main()
