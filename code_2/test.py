# from class_auto import Auto
# from grid import Grid
# from possiblemoves import *
# from types import *
# from random import *
# import sys
# sys.path.insert(0, 'C:\\Users\\Mees Kuipers\\Documents\\minor programmeren\\code_2\\algoritme')
# import dumbsolver

def main():
    ''' docstring placeholder
    '''
    # print(sys.path)
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
