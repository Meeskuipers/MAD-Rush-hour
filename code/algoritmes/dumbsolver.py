from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import *
from types import *
from random import *
from play import *

def dumbsolver(size):
    ''' docstring placeholder '''
    grid = Grid(size)
    counter = 0
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0,len(possible_moves)-1)
        move(grid,[possible_moves[randommove][0],possible_moves[randommove][1],possible_moves[randommove][2]])
        counter += 1
        if counter == 2000:
            dumbsolver(size)
        grid.grid = grid.update()
        show_grid(grid.grid)
    if counter < 1999:
        print("it took "  +str(counter)+  "moves to win (for the computer, you are an idiot who chose solve)")

def won(grid):
    if grid[2][5] == 6:
        return True

def show_grid(grid):
    for i in grid:
        for x in i:
            print("  ", end='')
            print(x, end='')
        print("")
    print("")
