from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
from code.helper.play_2 import play_2
from code.helper.checkwin import win


def dumbsolver(size, bord):
    ''' This function solves the bord by doing constantly doing random moves
        untill it either finds a solution or did 2000 moves. 2000 moves was
        chosen as the bound so that answers wouldnt be to long to work with and
        so that dumbsolver practically always finds an answerself.

        dumbsolver takes two arguments: an integer describing the bordsize and
        a string representing the bord to work with.

        dumbsolver is called from either main.py to solve the bord or from
        dannystra to give the hillclimber an initial solutionself.

        dumbsolver returns a list of moves to get to a victory state.'''
    grid = Grid(size, bord)
    counter = 0
    answer = []
    while win(grid, size):
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0, len(possible_moves)-1)
        move(grid, [possible_moves[randommove][0],
                    possible_moves[randommove][1],
                    possible_moves[randommove][2]])
        answer.append([possible_moves[randommove][0],
                       possible_moves[randommove][1],
                       possible_moves[randommove][2]])
        grid.update()
        counter += 1

        if counter == 2000:
            return dumbsolver(size, bord)
    print("it took " + " " + str(counter) + " " +
          " moves to win (for the computer, you're an idiot who chose solve)")
    return answer
