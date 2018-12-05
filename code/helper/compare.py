from code.classes.grid import Grid
from code.helper.play import move
from code.algoritmes.breadth import informedbreadth
from code.algoritmes.dumbsolver import dumbsolver
import matplotlib.pyplot as plt
import numpy as np

def compare(size, bord):
    bool = True
    breadthscore = informedbreadth(size,bord)
    while bool:
        dumbscore = dumbsolver(size,bord)
        if dumbscore:
            bool = False

    print('')
    print('dumbsolver score for this bord is:' + ' ' + str(dumbscore))
    print('informedbreadthfirst score is' + ' ' + str(breadthscore))
    algoritmes = ('dumb', 'breadth')
    waardes = [dumbscore, breadthscore]
    y = np.arange(len(algoritmes))
    plt.bar(y,waardes)
    plt.xticks(y,algoritmes)
    plt.show()
