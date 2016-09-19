from Agent import *

class Fish(Agent):
    def __init__(self, environment, posX, posY, name, data):
        super(Fish, self).__init__(environment, posX, posY, name, data)
        self.breedTime = data["fishBreedTime"]
        self.color = "Green"

    def decide(self):
        pass

    def move(self):
        raise NotImplementedError("Fish.move needs to be implemented")

    def breed(self):
        raise NotImplementedError("Fish.breed needs to be implemented")

    def update(self):
        #self.move()
        #self.breed()
        pass
