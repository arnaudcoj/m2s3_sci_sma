class Environment(object):
    """docstring for Environment"""
    def __init__(self, gridSizeX, gridSizeY, torus):
        super(Environment, self).__init__()
        self.init_grid(gridSizeX, gridSizeY, torus)

    def init_grid(self, gridSizeX, gridSizeY, torus):
        self.grid = []
        for j in range(gridSizeY):
            self.grid.append([None] * gridSizeX)
        print("The grid of size", gridSizeX, gridSizeY, "has successfully been created.")
