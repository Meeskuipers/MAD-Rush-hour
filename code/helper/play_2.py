from code.classes.class_auto import Auto
from code.classes.grid import Grid
from types import *
from random import *
from code.helper.draw_2 import begin
import copy


def play_2(size, bord, list):
    """
    De play_2 functie wordt gebruikt om van een lijst van moves om te zetten
    naar een lijst van grids. Deze lijst is nodig voor het tekenen in draw_2.
    """
    counter = 0
    playgrid = Grid(size, bord)
    check = copy.deepcopy(playgrid.grid)
    answer = []
    answer.append(playgrid.grid)
    for i in list:
        move(playgrid, i)
        playgrid.update()
        if playgrid.grid == check:  # Deel van hill climb algoritme
            counter = 0
            answer = []
        answer.append(playgrid.grid)
        counter = counter + 1
    print('it took you ' + str(counter) + ' moves to win')
    begin(answer, size)


def move(grid, command):
    """
    De move functie update de positie van de auto.
    """
    car = int(command[0])
    direction = command[1]
    times = command[2]
    grid.all_cars[car-1].move_car(direction, times)


def printgrid(grid):
    """
    De printgrid functie zorgt ervoor dat de grid op een goede manier geprint
    worden.
    """
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()
