from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *
from play import *


def dijkstra(size):
    grid = Grid(size)
    counter = 0
    cache = {}
    while not grid.won():
        
