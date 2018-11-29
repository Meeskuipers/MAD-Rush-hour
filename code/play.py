from classes.class_auto import Auto
from classes.grid import Grid
from types import *
from random import *
from draw import draw

def play(size):
    ''' docstring placeholder '''
    counter = 0
    print("Heee let's play!!!")
    playgrid = Grid(size)
    while not playgrid.won():
        printgrid(playgrid)
        command = input("> ").upper().split(',')
        move(playgrid,command)
        playgrid.update()
        counter = counter + 1
    printgrid(playgrid)
    print('it took you ' + str(counter) + ' moves to win')

def move(grid,command):
    ''' docstring placeholder '''
    if len(command) != 3:
        print("huh")
        return(False)
    car = int(command[0])
    direction = command[1]
    times = command[2]
    grid.all_cars[car-1].move_car(direction,times)


def printgrid(grid):
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()
