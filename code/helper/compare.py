from code.classes.grid import Grid
from code.helper.play import move
from code.algoritmes.breadth import informedbreadth
from code.algoritmes.dumbsolver import dumbsolver

def compare(size, bord):
    breadthscore = informedbreadth(size,bord)
    dumbscore = dumbsolver(size,bord)
    print('dumbsolver score for this bord is:' + ' ' + str(dumbscore))
    print('informedbreadthfirst score is' + ' ' + str(breadthscore))
