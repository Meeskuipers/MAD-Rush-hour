from code.classes.grid import Grid
from code.helper.play import move
from code.algoritmes.breadth import breadth
from code.algoritmes.dumbsolver import dumbsolver
from code.algoritmes.dannystra import dannystra
import matplotlib.pyplot as plt
import numpy as np


def compare(size, bord):
    '''Deze functie vergelijkt de scores van het informed breadth first
       algoritme met de dumbsolver en de hillclimber over de dumbsolverself.

       De functie neemt twee argumenten: een gridsize en een bord.

       Deze functie wordt aangeroepen vanuit main.py door user input'''
    bool = True
    breadthscore = breadth(size, bord)
    while bool:
        dumbscore = dumbsolver(size, bord)
        if dumbscore:
            bool = False
    dannyscore = dannystra(size, bord)

    print('')
    print('dumbsolver score for this bord is:' + ' ' + str(len(dumbscore)))
    print('informedbreadthfirst score is' + ' ' + str(len(breadthscore)))
    print('hilclimber over dumboslver is' + ' ' + str(len(dannyscore)))
    algoritmes = ('dumb', 'danny', 'breadth')
    waardes = [len(dumbscore), len(dannyscore), len(breadthscore)]
    y = np.arange(len(algoritmes))
    plt.bar(y, waardes)
    plt.xticks(y, algoritmes)
    plt.show()
