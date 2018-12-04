from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move


def dumbsolver(size,bord):
    ''' docstring placeholder '''
    grid = Grid(size,bord)
    counter = 0
    #answer = []
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0,len(possible_moves)-1)
        move(grid,[possible_moves[randommove][0],possible_moves[randommove][1],possible_moves[randommove][2]])
        #answer.append(possible_moves[randommove])
        counter += 1
        if counter == 2000:
            dumbsolver(size,bord)
    if counter < 1999:
        # with open(Random_solve.txt) as f:
        #     print(answer, file=f)
        print("it took "+ " " +str(counter)+ " " + " moves to win (for the computer, you're an idiot who chose solve)")

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
