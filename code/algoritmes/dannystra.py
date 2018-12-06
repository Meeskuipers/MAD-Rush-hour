from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from code.helper.play import move
from code.helper.random_oplossing import list
from code.helper.checkwin import win
from code.helper.draw_2 import begin
from code.algoritmes.dumbsolver import dumbsolver
from random import *
import copy

#Doe ipv last_move de laatste item van newlist bekijken
#Kijk of weghalen van een move nogsteeds zorgt voor een antwoord
#check altijd of de weg van de rode auto vrij is
#gaat alles door --> vernoemen
#gebruik remove_duplicates als een check voor alles
def dannystra(size,bord):
    """lijkt op hill climber algoritme"""
    grid = Grid(size,bord)
    list1 = list()
    last_list = remove_duplicates(list1) #gaat alles door --> vernoemen
    print(last_list)
    counter = 0
    new_list = remove_duplicates(hillclimber(last_list, size, bord, counter))

    while len(new_list) != len(last_list):
        print(len(last_list))
        print(len(new_list))
        last_list = copy.deepcopy(new_list)
        new_list = remove_duplicates(hillclimber(new_list, size, bord, counter))


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
    if len(hc_list) > 100:
        max = 99
    else:
        max = len(hc_list)-2
    if counter == max:
        return hc_list
    else:
        counter += 1
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
