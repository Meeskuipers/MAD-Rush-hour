from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move


def dumbsolver(size,bord):
    ''' docstring placeholder '''
    grid = Grid(size,bord)
    counter = 0
    answer = []
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0,len(possible_moves)-1)
        move(grid,[possible_moves[randommove][0],possible_moves[randommove][1],possible_moves[randommove][2]])
        answer.append(grid)
        grid.update()
        counter += 1
        if counter == 2000:
            dumbsolver(size,bord)
    if counter < 1999:
        return counter
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
