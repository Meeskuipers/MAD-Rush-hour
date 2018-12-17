from copy import deepcopy
from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import *
from code.helper.checkwin import win
from math import ceil
from code.helper.draw_2 import begin
from code.helper.play_2 import play_2


def breadth(size, bord):
    ''' De functie breadth vraagt om twee argumenten: een integer
        die de bord groote aangeeft en een string die aangeeft welk bord
        opgelost moet worden.

        Breadth lost het gegeven bord op zoals een breadth first algoritme
        dat zou doen, maar verkent geen dubbele nodes.

        De functie breadth wordt aangeroepen vanuit main.py afhankelijk
        van user input.

        Wanneer breadth een antwoord vind wordt er gevraagd om user input
        waarna breadth een functie aanroept die de gedane zetten
        visualiseert.

        breadth returned een lijst met moves tot de winnende node voor de draw
        en voor de compare functie'''

    grid = Grid(size, bord)
    possible_moves = []
    startgrid = deepcopy(grid.grid)
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid
    explored = {}
    explored[str(grid.grid)] = []

    while bool:
        counter += 1
        print(counter)
        gridlist = []

        for i in borddict.keys():
            grid.grid = borddict[i]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for x in (possible_moves):
                move(grid, x)
                grid.grid = grid.update()
                if str(grid.grid) not in explored.keys():
                    gridlist.append(deepcopy(grid.grid))
                    path = []
                    path = deepcopy(explored[i])
                    path.append(deepcopy(x))
                    explored[str(grid.grid)] = deepcopy(path)
                movecarback(grid, x)
                grid.update()

        for y in gridlist:
            grid.grid = y
            grid.updatecars()
            borddict[str(y)] = y
            if not win(grid, size):
                bool = False
                input('awaiting orders sir')
                play_2(size, bord, explored[str(y)])
                return explored[str(y)]
                break

    print('it took' + " " + str(counter) + " " + "moves to win")


def movecarback(grid, command):
    ''' movecarback vraagt om twee argumenten: de grid waar mee gewerkt wordt
        en het een string van het commando welke auto verplaatst moet worden.

        movecarback verplaatst de auto in de tegenovergestelde riching van het
        gegeven commando.

        movecarback wordt aangeroepen vanuit breadth '''
    if command[1] == 'LEFT':
        move(grid, [command[0], 'RIGHT', command[2]])

    if command[1] == 'RIGHT':
        move(grid, [command[0], 'LEFT', command[2]])

    if command[1] == 'UP':
        move(grid, [command[0], 'DOWN', command[2]])

    if command[1] == 'DOWN':
        move(grid, [command[0], 'UP', command[2]])
