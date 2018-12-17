from code.classes.class_auto import Auto
from code.classes.grid import Grid
from types import *
from random import *
from code.helper.draw_2 import begin
import copy


def play_2(size, bord, list):
    """
    De fucntie play_2 vraag om drie argumenten:
        1) Een interger die de groote van het boor aangeeft
        2) Een string die aangeeft welk boord opgelost moet worden
        3) Een lijst van moves die een oplossing geven.
    De play_2 functie wordt gebruikt om van een lijst van moves om te zetten
    naar een lijst van grids. Deze lijst is nodig voor het tekenen in draw_2.

    Deze functie wordt aangeroepen door breadth en dannystra. De groote van de
    list die als argument wordt gegeven hangt af van de oplossing die de
    algoritmes krijgen.
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
    De functie move krijgt twee argumenten: een lijst met lijsten waarin de
    locatie van alle auto's staan en een command die aangeeft welke auto waar
    heen gaat.

    De functie wordt aangeroepen door play_2.

    De coordinaten van de auto's worden aangepast in de Class auto.
    """
    car = int(command[0])
    direction = command[1]
    times = command[2]
    grid.all_cars[car-1].move_car(direction, times)


def printgrid(grid):
    """
    De functie printgrid vraag om één argument: een lijst met lijsten waarin
    intergers staan.

    De printgrid functie zorgt ervoor dat de grid op een goede manier geprint
    worden.
    """
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()
