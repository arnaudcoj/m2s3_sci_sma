from Agent import *

class Shark(Agent):
    def __init__(self, environment, posX, posY, name, data):
        super(Shark, self).__init__(environment, posX, posY, name, data)
        self.breedTime = data["sharkBreedTime"]
        self.starveTime = data["sharkStarveTime"]
        self.color = "Pink"

    def decide(self):
        raise NotImplementedError("Shark.decide needs to be implemented")

    def starve(self):
        raise NotImplementedError("Shark.starve needs to be implemented")

    def eat(self):
        raise NotImplementedError("Shark.eat needs to be implemented")

    def move(self):
        raise NotImplementedError("Shark.move needs to be implemented")

    def breed(self):
        raise NotImplementedError("Shark.breed needs to be implemented")

    def update(self):
        self.starve()
        self.eat()
        self.move()
        self.breed()
