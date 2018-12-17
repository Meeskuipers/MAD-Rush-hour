from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.checkwin import win
from types import *
from random import *
from code.helper.draw_2 import begin


def play(size, bord):
    """
    De play functie zorgt ervoor dat Rush-Hour zelf gespeeld kan worden.
    Hierbij wordt een command gevraagd (car.id, (RIGHT, LEFT, UP, DOWN),
    hoeveel plekken).

    Wanneer de rode auto (auto nummer 6) helemaal recht is gekomen wordt het
    gegeven pad uitgetekent in draw.
    """
    counter = 0
    print("Heee let's play!!!")
    playgrid = Grid(size, bord)
    answer = []
    answer.append(playgrid.grid)
    while win(playgrid, size):
        printgrid(playgrid)
        command = input("> ").upper().split(',')
        move(playgrid, command)
        playgrid.update()
        answer.append(playgrid.grid)
        counter = counter + 1
    printgrid(playgrid)
    begin(answer, size)
    print('it took you ' + str(counter) + ' moves to win')


def move(grid, command):
    """
    De move functie update de positie van de auto.
    """
    if len(command) != 3:
        return(False)
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
