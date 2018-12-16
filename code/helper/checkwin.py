from math import ceil


def win(grid, size):
    victoryx = ceil(size / 2) - 1
    victoryy = size - 1
    if grid.grid[victoryx][victoryy] == 6:
        return False
    else:
        return True
