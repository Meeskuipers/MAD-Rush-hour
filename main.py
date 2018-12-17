from code.algoritmes.dumbsolver import dumbsolver
from code.algoritmes.dannystra import dannystra
from code.algoritmes.breadth import breadth
from code.helper.play import play
from code.helper.play_2 import play_2
from code.helper.draw_2 import begin


def main():
    '''
    Main wordt aangeroepen om het programma te starten.
    Het heeft geen argumenten en het roept andere functies aan,
    aan de hand van de gegeven gebruikers input.
    '''
    bordlist = ['data/game_1.txt', 'data/game_2.txt', 'data/game_3.txt',
                'data/game_4.txt', 'data/game_5.txt', 'data/game_6.txt',
                'data/game_7.txt']
    choice = input('type play, hillclimber, dumbsolve, breadth, compare of test' + " ")
    if choice != 'test':
        nummer = int(input('bord 1, 2, 3, 4, 5, 6 of 7?'))
        if nummer <= 3:
            gridsize = 6
        elif 4 <= nummer <= 6:
            gridsize = 9
        else:
            gridsize = 12
        bord = bordlist[int(nummer) - 1]
        if choice == 'play':
            play(int(gridsize), bord)
        elif choice == 'dumbsolve':
            dumbsolver(int(gridsize), bord)
        elif choice == 'hillclimber':
            dannystra(int(gridsize), bord)
        elif choice == 'compare':
            compare(int(gridsize), bord)
        elif choice == 'breadth':
            breadth(int(gridsize), bord)
        else:
            print('Dat is geen goede input, probeer het opnieuw')
            main()
    elif choice == 'test':
        gridsize = 6
        bord = 'data/game_2.txt'
        breadth(int(gridsize), bord)


main()
