from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from code.helper.play import move
from code.helper.random_oplossing import list
from code.helper.checkwin import win
from random import *
import copy

#Doe ipv last_move de laatste item van newlist bekijken
#Kijk of weghalen van een move nogsteeds zorgt voor een antwoord
#check altijd of de weg van de rode auto vrij is
#
def dannystra(size,bord):
    """lijkt op hill climber algoritme"""
    grid = Grid(size,bord)
    answer = remove_duplicates()
    new = hillclimber(answer, size, bord)
    answer = new
    return(answer)


def remove_duplicates():
    newlist = [[0,0,0]]
    for move in list():
        if move[:2] == newlist[-1][:2]:
            newmove = move[:2] + [move[2]+newlist[-1][2]]
            newlist = newlist[:-1]
            newlist.append(newmove)
        elif move[0] == newlist[-1][0]:
            if move[2] > newlist[-1][2]:
                newmove = move[:2] + [move[2]-newlist[-1][2]]
                newlist = newlist[:-1]
                newlist.append(newmove)
            elif move[2] < newlist[-1][2]:
                newmove = newlist[-1][:2] + [newlist[-1][2]-move[2]]
                newlist = newlist[:-1]
                newlist.append(newmove)
            elif move[2] == newlist[-1][2]:
                newlist = newlist[:-1]
        else:
            newlist.append(move)
        # print(newlist)
    return(newlist[1:])

def hillclimber(list, size, bord):
    for i in range(len(list)-1):
        grid = Grid(size, bord)
        a = copy.deepcopy(list[i])
        b = copy.deepcopy(list[i+1])
        list[i] = b
        list[i+1] = a
        bool = solver(list, size, grid)
        if not bool:
            list[i] = a
            list[i+1] = b
        elif counter == 10:
            return bool
        else:
            hillclimber(bool, size, bord)

    return(list)

def solver(list, size, grid):
    ''' docstring placeholder '''
    answer = []
    for i in list:
        if i not in possiblemoves(grid):
            return False
        move(grid, i)
        grid.update()
        answer.append(i)
        if not win(grid, size):
            return(answer)
    return False
