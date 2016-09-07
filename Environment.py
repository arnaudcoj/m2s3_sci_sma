class Environment(object):
    """docstring for Environment"""
    def __init__(self, gridSizeX, gridSizeY):
        super(Environment, self).__init__()
        self.init_grid(gridSizeX, gridSizeY)

    def init_grid(self, gridSizeX, gridSizeY):
        self.grid = []
        for j in range(gridSizeY):
            self.grid.append([None] * gridSizeX)
        print("The grid of size", gridSizeX, gridSizeY, "has successfully been created.")
