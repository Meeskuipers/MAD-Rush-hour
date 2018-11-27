from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *
from play import *


def informed(size):
    grid = Grid(size)
    counter = 0
    cache = {}
    cache[grid] = [grid]
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        travel = caches[grid]

        for i in range(0,range(0,len(possible_moves))):
            move(grid,[possible_moves[i][0],possible_moves[i][1],possiblemoves[i][2]])
            lastgrid = grid
            grid.grid = grid.update()

            if (len(cache[lastgrid]) + 1) < len(cache.get(grid)):
                visited = cache[lastgrid]
                visited.append(grid)
                cache[grid] = visited

            if possible_moves[i][1] == 'LEFT':
                move(grid,[possible_moves[i][0],'RIGHT',possiblemoves[i][2]])

            if possible_moves[i][1] == 'RIGHT':
                move(grid,[possible_moves[i][0],'LEFT',possiblemoves[i][2]])

            if possible_moves[i][1] == 'UP':
                move(grid,[possible_moves[i][0],'DOWN',possiblemoves[i][2]])

            if possible_moves[i][1] == 'DOWN':
                move(grid,[possible_moves[i][0],'UP',possiblemoves[i][2]])



    print(len(cache[grid]))















"""
 """
