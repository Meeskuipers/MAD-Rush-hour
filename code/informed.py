from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *
from play import *
from dumbsolver import *

def informed(size):
    grid = Grid(size)
    cache = {}
    cache[grid] = [grid]
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)

        for i in range(0,len(possible_moves)):
            move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
            lastgrid = grid
            grid.grid = grid.update()

            if (len(cache[lastgrid]) + 1) < len(cache.get(grid)):
                visited = cache[lastgrid]
                visited.append(grid)
                cache[grid] = visited

            if possible_moves[i][1] == 'LEFT':
                move(grid,[possible_moves[i][0],'RIGHT',possible_moves[i][2]])

            if possible_moves[i][1] == 'RIGHT':
                move(grid,[possible_moves[i][0],'LEFT',possible_moves[i][2]])

            if possible_moves[i][1] == 'UP':
                move(grid,[possible_moves[i][0],'DOWN',possible_moves[i][2]])

            if possible_moves[i][1] == 'DOWN':
                move(grid,[possible_moves[i][0],'UP',possible_moves[i][2]])

        list_counter = min([len(i) for i in dict.values()])
        grid = list_counter[-1]
        updatecars(grid)

    for i in range(0,len(cache[grid])):
        show_grid(i)

informed(6)
