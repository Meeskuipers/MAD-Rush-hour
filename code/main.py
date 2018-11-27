<<<<<<< HEAD
from dumbsolver import dumbsolver
#from informed import informed
=======
from algoritmes.dumbsolver import dumbsolver
>>>>>>> 35bcb0ca61521535395ddea277e61f078f5cb9cc
from play import play

def main():
    ''' docstring placeholder
    '''
    gridsize = 6
    choice = input('type play or dumbsolve or informed    ')
    if choice == 'play':
        play(int(gridsize))
    elif choice == 'dumbsolve':
        dumbsolver(int(gridsize))
    else:
        print('Thats is not a valid input')
        main()

main()
