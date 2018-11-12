class Grid():
    def __init__(self):
        self.grid = self.load_grid()

    def load_grid(self):
        gridsize = 6
        grid = []
        row = []
        for i in range(gridsize):
            row.append([])
        for i in range(gridsize):
            grid.append(row)
        print(grid)
Main = Grid()
Main.load_grid()
