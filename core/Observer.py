class Observer(object):
    """docstring for Observer"""
    def __init__(self):
        super(Observer, self).__init__()
        self.signalFunc = None

    def onReceive(self, signal, emitter):
        if self.signalFunc != None:
            self.signalFunc[signal](emitter)
