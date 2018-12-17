from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.checkwin import win
from types import *
from random import *
from code.helper.draw_2 import begin


def play(size, bord):
    """
    Deze functie laat de user zelf een bord oplossen. De user moet typt een
    commande in de vorm {carID, richting, hoeveelheid stapjes} E.G.: 6,left,2.

    Play vraagt om twee argumenten: een integer die de size van het bord
    beschrijft en een string die aangeeft welk bord opgelost moet worden.

    Play wordt aangeroepen vanuit main.py afhankelijk van user input.
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
    Deze functie past de positie van een instance van de class auto aanself.

    move heeft twee argumenten: een instance van de class grid en een commando
    dat uit user input wordt gehaald.

    move wordt aangeroepen door alle algoritmes en door play.
    """
    if len(command) != 3:
        return(False)
    car = int(command[0])
    direction = command[1]
    times = command[2]
    grid.all_cars[car-1].move_car(direction, times)


def printgrid(grid):
    """
    De printgrid functie zorgt ervoor dat de grid op een leesbare manier naar
    de console wordt geprint.

    printgrid heeft maar een argument: een instance van grid om te printen.

    printgrid wordt gecalled vanuit play om de user te kunnen laten spelen.
    """
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()
