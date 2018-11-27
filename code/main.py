from dumbsolver import dumbsolver
from dijkstra import dijkstra
from play import play

def main():
    ''' docstring placeholder
    '''
    gridsize = 6
    choice = input('type play or dumbsolve    ')
    if choice == 'play':
        play(int(gridsize))
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize))
    elif choice == 'dijkstra':
        dijkstra(int(gridsize))
    else:
        print('Thats is not a valid input')
        main()

main()
