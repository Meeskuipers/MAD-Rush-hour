from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
from code.helper.random_oplossing import list
import copy


def dannystra(size,bord):
    """lijkt op hill climber algoritme"""
    grid = Grid(size,bord)
    cache = {}
    previous_elem = [0,0,0]
    for elem in list()[:10]:
        if elem[:2] == previous_elem[:2]:
            times = elem[2] + previous_elem[2]

        elif elem[0] == previous_elem[0]:
            times = elem[2] - previous_elem[2]

    #nog toevoegen als weg voor winnercar vrij is --> doen
        previous_elem = copy.deepcopy(elem)
