from dumbsolver import dumbsolver
#from informed import informed
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
    elif choice == 'informed':
        informed(int(gridsize))
    else:
        print('Thats is not a valid input')
        main()

main()
