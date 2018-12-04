from code.classes.class_auto import Auto
from code.classes.grid import Grid
from types import *
from random import *
from code.helper.draw import draw



def play(size,bord):
    ''' docstring placeholder '''
    counter = 0
    print("Heee let's play!!!")
    playgrid = Grid(size,bord)
    answer = []
    while not playgrid.won():
        printgrid(playgrid)
        command = input("> ").upper().split(',')
        answer.append(playgrid.grid)
        print(answer)
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
