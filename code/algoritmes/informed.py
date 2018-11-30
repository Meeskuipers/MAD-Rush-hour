from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
import copy

def informed(size,bord):
    grid = Grid(size)
    cache = {}
    copiedgrid = copy.deepcopy(grid)
    print(grid)
    print(copiedgrid)
    cache[copiedgrid] = [grid.grid]
    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)

        for i in range(0,len(possible_moves)):
            move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
            lastgrid = copy.deepcopy(grid)
            grid.grid = grid.update()
            if grid in cache.keys():
                print('grid zit in keys')
                s
                if (len(cache[lastgrid]) + 1) < len(cache[grid]):
                    print('past grid aan')
                    visited = cache[lastgrid]
                    visited.append(grid.grid)
                    cache[grid] = visited

                if possible_moves[i][1] == 'LEFT':
                    move(grid,[possible_moves[i][0],'RIGHT',possible_moves[i][2]])

                if possible_moves[i][1] == 'RIGHT':
                    move(grid,[possible_moves[i][0],'LEFT',possible_moves[i][2]])

                if possible_moves[i][1] == 'UP':
                    move(grid,[possible_moves[i][0],'DOWN',possible_moves[i][2]])

                if possible_moves[i][1] == 'DOWN':
                    move(grid,[possible_moves[i][0],'UP',possible_moves[i][2]])

        length = min([len(i) for i in cache.values()])
        shortest_path = []

        for i in cache.values():
            if len(i) == length:
                shortest_path = i

        grid.grid = shortest_path[-1]
        grid.updatecars()
        grid.update()

    printgrid(grid)



informed(6,'boards/game_1.txt')
