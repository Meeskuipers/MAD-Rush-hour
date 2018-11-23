from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *
from play import *

def dumbsolver(size):
    grid = Grid(size)
    counter = 0
    while not won(grid):
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0,len(possible_moves)-1)
        move(grid,[possible_moves[randommove][0],possible_moves[randommove][1]])
        counter += 1
        grid.grid = grid.load_grid()

    print("it took "+ " " +str(counter)+ " " + " moves to win (for the computer, you're an idiot who chose solve)")
