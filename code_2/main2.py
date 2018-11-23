from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *


def main():
    ''' docstring placeholder
    '''
    gridsize = 6
    choice = input('type play or dumbsolve    ')
    if choice == 'play':
        play(int(gridsize))
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize))
    else:
        print('Thats is not a valid input')
        main()

main()
