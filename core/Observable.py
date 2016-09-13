from Observer import *

class Observable(object):
    """docstring for Observable"""
    def __init__(self):
        super(Observable, self).__init__()
        self.observers = []

    def addObserver(self, observer):
        if isinstance(observer, Observer):
            self.observers.append(observer)
        else:
            print("addObserver :", observer, "is not an observer")
            
    def emitSignal(self, signal):
        for observer in self.observers:
            observer.onReceive(signal, self)
