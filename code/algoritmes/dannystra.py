from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
from Random_solve import list

def dannystra(size,bord):
    """lijkt op hill climber algoritme"""
    grid = Grid(size,bord)
    cache = {}
    for elem in list():
        print(elem)
