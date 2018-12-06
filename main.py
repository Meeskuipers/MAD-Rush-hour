from code.algoritmes.dumbsolver import dumbsolver
from code.algoritmes.dannystra import dannystra
from code.algoritmes.breadth import *
from code.helper.play import play
from code.helper.play_2 import play_2
from code.helper.draw_2 import begin
#from code.helper.compare import compare

def main():
    ''' Main is called to start the program, it takes no arguments and will call other functions depending on input.
    '''
    bordlist = ['data/game_1.txt','data/game_2.txt','data/game_3.txt','data/game_4.txt','data/game_5.txt','data/game_6.txt','data/test.txt']
    choice = input('type play, dumbsolve or informed    ')
    gridsize = input('what size would you like your board? (6)')
    nummer = input('bord 1,2,3,4,5 of 6?')
    bord = bordlist[int(nummer) - 1]
    if choice == 'play':
        play(int(gridsize), bord)
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize), bord)
    elif choice == 'danny':
        dannystra(int(gridsize), bord)
    elif choice == 'informed':
        informedbreadth(int(gridsize),bord)
    elif choice == 'bord':
        play_2(int(gridsize),bord)
        informedbreadth(int(gridsize), bord)
    elif choice == 'draw':
        begin()
    elif choice == 'compare':
        compare(int(gridsize), bord)
    else:
        print('Thats is not a valid input')
        main()

main()
