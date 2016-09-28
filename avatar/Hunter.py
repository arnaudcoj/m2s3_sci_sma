from Agent import *
from Observer import *

class Hunter(Avatar):
    """docstring for Hunter."""
    def __init__(self, environment, posX, posY, name):
        super(Hunter, self).__init__(environment, posX, posY, name)
        self.avatarFollower = AvatarFollower()

    def decide(self):
        if self.avatarFollower.dijkstraMatrix != None :
            pass #choisir meilleure case
            #si score de meilleure case = 0, ou si player dessus, fin du jeu

    def update(self):
        pass #move

    class AvatarFollower(Observer):
        """docstring for AvatarFollower."""
        def __init__(self):
            super(AvatarFollower, self).__init__()
            self.dijkstraMatrix = None
            self.signalFunc = {"avatarUpdated":onAvatarUpdated}

        def onAvatarUpdated(self, avatar):
            self.dijkstraMatrix = avatar.dijkstraMatrix
