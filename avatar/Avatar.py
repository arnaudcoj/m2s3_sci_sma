from Agent import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener

    def decide(self):
        UDPressed = self.keyListener.UDPressed
        LRPressed = self.keyListener.LRPressed
        self.pasX = 0
        self.pasY = 0
        if UDPressed == 'Up':
            self.pasY -= 1
        elif UDPressed == 'Down':
            self.pasY += 1
        if LRPressed == 'Left':
            self.pasX -= 1
        elif LRPressed == 'Right':
            self.pasX += 1

    def update(self):
        self.move()
