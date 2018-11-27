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
    cache[grid] = grid
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        travel = caches[grid]
        for i in range(0,range(0,len(possible_moves))):
            move(grid,[possible_moves[randommove][i],possible_moves[randommove][i],possiblemoves[randommove][i]])
        lastgrid = grid
        grid.grid = grid.update()
        if (len(cache[lastgrid]) + 1) < len(cache.get(grid)):
                visited = cache[lastgrid]
                visited.append(grid)
                cache[grid] = visited














"""
 """
