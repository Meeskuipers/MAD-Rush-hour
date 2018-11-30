from algoritmes.dumbsolver import dumbsolver
from play import play

def main():
    ''' docstring placeholder
    '''
    bordlist = ['boards/game_1.txt','boards/game_2.txt','boards/game_3.txt','boards/game_4.txt','boards/game_5.txt','boards/game_6.txt']
    choice = input('type play or dumbsolve or informed    ')
    gridsize = input('what size would you like your board? (6)')
    nummer = input('bord 1,2,3,4,5 of 6?')
    nummer = int(nummer) - 1
    bord = bordlist[nummer]
    if choice == 'play':
        play(int(gridsize),bord)
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize),bord)
    else:
        print('Thats is not a valid input')
        main()

main()
