from math import ceil


def win(grid, size):
    """
    Deze functie checked of een bord opgelost isself.

    De functie vraagt om twee argumenten: een grid en het formaat van deze
    grid.

    Deze functie wordt aangeroepen vanuit de algoritmes om te checken of de
    winnende move gemaakt is."""
    victoryx = ceil(size / 2) - 1
    victoryy = size - 1
    if grid.grid[victoryx][victoryy] == 6:
        return False
    else:
        return True
