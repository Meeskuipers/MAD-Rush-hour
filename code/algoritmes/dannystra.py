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
    newlist = []
    last_move = [0,0,0]
    #print(grid.grid)
    for move in list():
        if move[:2] == last_move[:2]:
            newmove = move[:2] + [move[2]+last_move[2]]
            #print(move, last_move, newmove)
            newlist.append(newmove)
        elif move[0] == last_move[0]:
            if move[2] > last_move[2]:
                newmove = move[:2] + [move[2]-last_move[2]]
                newlist.append(newmove)
            elif move[2] < last_move[2]:
                newmove = last_move[:2] + [last_move[2]-move[2]]
                newlist.append(newmove)

        else:
            newlist.append(move)


        last_move = move

    # for i in range(len(w_list)):
    #     #print(w_list[i][2])
    #     if w_list[i][:2] == w_list[i+1][:2]:
    #         times = w_list[i][2] + w_list[i+1][2]
    #         w_list[i][2] = int(times)
    #         del(w_list[i+1])
    #         print(w_list[i])
    #     elif w_list[i][0] == w_list[i+1][0]:
    #         times = w_list[i][2] - w_list[i+1][2]
            #print(times)
    #nog toevoegen als weg voor winnercar vrij is --> doen
