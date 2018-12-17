from code.classes.grid import Grid
from code.helper.play import move
from code.algoritmes.breadth import informedbreadth
from code.algoritmes.dumbsolver import dumbsolver
import matplotlib.pyplot as plt
import numpy as np


def compare(size, bord):
    """
    De compare functie vergelijkt de lengte van de antwoorden van het
    breadthfirst algoritme en het random algoritme.

    Deze uitkomst wordt dan in een staafdiagram tegenover elkaar gezet
    """
    bool = True
    breadthscore = informedbreadth(size, bord)
    # Het kan zijn dat dumbsolver geen antwoord teruggeefd
    # Deze while loop is dus als check toegevoegd.
    while bool:
        dumbscore = dumbsolver(size, bord)
        if dumbscore:
            bool = False

    print('')
    print('dumbsolver score for this bord is:' + ' ' + str(dumbscore))
    print('informedbreadthfirst score is' + ' ' + str(breadthscore))
    algoritmes = ('dumb', 'breadth')
    waardes = [dumbscore, breadthscore]
    y = np.arange(len(algoritmes))
    plt.bar(y, waardes)
    plt.xticks(y, algoritmes)
    plt.show()
