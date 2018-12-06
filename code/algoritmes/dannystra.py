from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from code.helper.play import move
from code.helper.random_oplossing import list
from code.helper.checkwin import win
from code.helper.play_2 import play_2
from code.algoritmes.dumbsolver import dumbsolver
from random import *
import copy

#gebruik remove_duplicates als een check voor alles
def dannystra(size,bord):
    """
    Dit is een versie van een hill climb algoritme.
    Het neemt een oplossing uit dumbsolve en probeert hier een betere oplossing van te maken.
    Het heeft nodig als input een grootte en een bordconfiguratie
    Het geeft als output een betere oplossing van dumbsolve
    """
    grid = Grid(size,bord)
    list1 = dumbsolver(size, bord)
    last_list = remove_duplicates(list1)
    counter = 0
    new_list = remove_duplicates(hillclimber(last_list, size, bord, counter))

    while len(new_list) != len(last_list):
        print(len(last_list))
        print(len(new_list))
        last_list = copy.deepcopy(new_list)
        new_list = remove_duplicates(hillclimber(new_list, size, bord, counter))

    #in play wordt gecheckt of de begingrid opnieuw tegengekomen is
    play_2(size, bord, new_list)

def remove_duplicates(list):
    newlist = [[0,0,0]]
    for move in list:
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
    return(newlist[1:])

def hillclimber(list, size, bord, counter):
    grid = Grid(size, bord)
    hc_list = solver(list, size, grid, counter)
    answer1 = []
    if counter < len(hc_list)-1:
        if len(hc_list) > 400:
            max = 399
            #deze magicnumber houden de timecomplexity in toom
        else:
            max = len(hc_list)-2
        if counter == max:
            return hc_list
        else:
            counter += 1
            return hillclimber(hc_list, size, bord, counter)
    else:
        counter = 0
        return hillclimber(hc_list, size, bord, counter)


def solver(list, size, grid, counter):
    answer = []
    a = copy.deepcopy(list[counter])
    b = copy.deepcopy(list[counter+1])
    list[counter] = b
    list[counter+1] = a
    for i in list:
        if i not in possiblemoves(grid):
            list[counter] = a
            list[counter+1] = b
            return(list)
        move(grid, i)
        grid.update()
        answer.append(i)
        if not win(grid, size):
            return(answer)
    list[counter] = a
    list[counter+1] = b
    return(list)
