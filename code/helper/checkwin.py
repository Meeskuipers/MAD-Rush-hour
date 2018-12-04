from math import ceil

def win(grid, size):
    if grid[2][5] == 6:
        return True
    else:
        return False
    # victoryx = ceil(size/2) -1
    # victoryy = size - 1
    # if grid[victoryx][victoryy] == 6:
    #     return True
    # else:
    #     return False
