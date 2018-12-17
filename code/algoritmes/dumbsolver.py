from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
from code.helper.play_2 import play_2
from code.helper.checkwin import win


def dumbsolver(size, bord):
    ''' De functie dumbsolver vraagt om twee argumenten: een integer
        die de bord groote aangeeft en een string die aangeeft welk bord
        opgelost moet worden.

        dumbsolver lost de borden op door steeds een willekeurige move te doen.
        Nadat er 800 moves zijn gedaan gaat dumbsolver het opnieuw proberen om
        zo een degelijke oplossing te vinden. 800 moves is gekozen als bound
        zodat er bijna altijd een antwoord gevonden wordt, terwijl de uitkomst
        niet absurd hoog is.

        Dumbsolver wordt aangeroepen vanuit main.py als gevolg van user
        input

        Dumbsolver returned een lijst met gedane zetten om bij de final state
        te komen.'''
    grid = Grid(size, bord)
    counter = 0
    answer = []
    while win(grid, size):
        possible_moves = []
        possible_moves = possiblemoves(grid)
        randommove = randint(0, len(possible_moves)-1)
        move(grid, [possible_moves[randommove][0],
                    possible_moves[randommove][1],
                    possible_moves[randommove][2]])
        answer.append([possible_moves[randommove][0],
                       possible_moves[randommove][1],
                       possible_moves[randommove][2]])
        grid.update()
        counter += 1

        if counter == 2000:
            return dumbsolver(size,bord)
    if counter < 1999:
        print("it took "+ " " +str(counter)+ " " + " moves to win (for the computer, you're an idiot who chose solve)")
        play_2(size,bord,answer)

        if counter == 800:
            return dumbsolver(size, bord)
    if counter < 800:
        print("it took " + " " + str(counter) + " " + "moves to win")
        return answer


def show_grid(grid):
    '''Deze functie heeft als argument een class grid en print deze
       uit op een manier die voor mensen leesbaar is in de console'''
    for i in grid:
        for x in i:
            print("  ", end='')
            print(x, end='')
        print("")
    print("")
