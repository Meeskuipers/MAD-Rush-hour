from math import ceil


def win(grid, size):
    """
    Dit is de algemene win conditie voor het spel rush hour.
    Het wordt in elk algoritme aangeroepen om te controleren of
    de teruggegeven grid een final state is.
    """
    victoryx = ceil(size / 2) - 1
    victoryy = size - 1
    if grid.grid[victoryx][victoryy] == 6:
        return False
    else:
        return True
