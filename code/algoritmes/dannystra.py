from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from code.helper.play import move
from code.helper.random_oplossing import list
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
    hillclimber(answer)

def remove_duplicates():
    newlist = [[0,0,0]]
    for move in list():
        if move[:2] == newlist[-1][:2]:
            newmove = move[:2] + [move[2]+newlist[-1][2]]
            newlist.pop()
            newlist.append(newmove)
        elif move[0] == newlist[-1][0]:
            if move[2] > newlist[-1][2]:
                newmove = move[:2] + [move[2]-newlist[-1][2]]
            elif move[2] < newlist[-1][2]:
                newmove = newlist[-1][:2] + [newlist[-1][2]-move[2]]
            newlist.pop()
            newlist.append(newmove)
        else:
            newlist.append(move)
        # print(newlist)
    return(newlist[1:])

def hillclimber(list):
    print(list)
    for i in range(len(list)-1):
        a = copy.deepcopy(list[i])
        b = copy.deepcopy(list[i+1])
        list[i] = b
        list[i+1] = a
    print(list)
