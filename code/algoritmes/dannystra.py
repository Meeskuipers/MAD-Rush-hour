from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
from Random_solve import list
import copy


def dannystra(size,bord):
    """lijkt op hill climber algoritme"""
    grid = Grid(size,bord)
    cache = {}
    previous_elem = [0,0,0]
    for elem in list():
        if elem[0] == previous_elem[0]:
            if elem[1] == previous_elem[1]:
                times = elem[2] + previous_elem[2]
                #print(times)
            elif elem[2] > previous_elem[2]:
                times = elem[2] - previous_elem[2]
                print(times)

        previous_elem = copy.deepcopy(elem)
