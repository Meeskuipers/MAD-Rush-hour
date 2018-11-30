from algoritmes.dumbsolver import dumbsolver
from algoritmes.dannystra import dannystra
from algoritmes.axelstra import *
from algoritmes.breadth import *
from play import play

def main():
    ''' Main is called to start the program, it takes no arguments and will call other functions depending on input.
    '''
    bordlist = ['boards/game_1.txt','boards/game_2.txt','boards/game_3.txt','boards/game_4.txt','boards/game_5.txt','boards/game_6.txt','boards/test.txt']
    choice = input('type play or dumbsolve or informed    ')
    gridsize = input('what size would you like your board? (6)')
    nummer = input('bord 1,2,3,4,5 of 6?')
    nummer = int(nummer) - 1
    bord = bordlist[nummer]
    if choice == 'play':
        play(int(gridsize),bord)
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize),bord)
    elif choice == 'danny':
        dannystra(int(gridsize),bord)
    elif choice == 'informed':
        informed(int(gridsize),bord)
    elif choice == 'breadth':
        breadth(int(gridsize),bord)
    else:
        print('Thats is not a valid input')
        main()

main()
