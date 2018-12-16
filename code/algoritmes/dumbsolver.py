from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
from code.helper.play_2 import play_2
from code.helper.checkwin import win


def dumbsolver(size,bord):
    ''' docstring placeholder '''
    grid = Grid(size,bord)
    counter = 0
    answer = []
    while win(grid,size):
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0,len(possible_moves)-1)
        move(grid,[possible_moves[randommove][0],possible_moves[randommove][1],possible_moves[randommove][2]])
        answer.append([possible_moves[randommove][0],possible_moves[randommove][1],possible_moves[randommove][2]])
        grid.update()
        counter += 1
        if counter == 2000:
            return dumbsolver(size,bord)
    if counter < 1999:
        print("it took "+ " " +str(counter)+ " " + " moves to win (for the computer, you're an idiot who chose solve)")
        play_2(size,bord,answer)
        return answer

def show_grid(grid):
    for i in grid:
        for x in i:
            print("  ", end='')
            print(x, end='')
        print("")
    print("")
