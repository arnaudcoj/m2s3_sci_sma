from Observer import *

class View(Observer):
    """docstring for View"""
    def __init__(self):
        super(View, self).__init__()

    def onReceive(self, signal, emitter):
        if signal == "modelUpdated":
            emitter.environment.printASCII()
