from classes.class_auto import Auto
from classes.grid import Grid
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move



def axelstra(size,bord):
    grid = Grid(size)
    cache = {}
    






def updatecars(grid):
    for car in self.all_cars:
        id = car.id
        newposition = []
        for i in range(0,len(grid)-1):
            for x in range(0,len(grid)-1):
                if grid[i][x] == car.id:
                    newposition.append([i,x])
        car.position = newposition
