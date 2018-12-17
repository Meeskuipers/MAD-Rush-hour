from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from code.helper.play import move
from code.helper.checkwin import win
from code.helper.play_2 import play_2
from code.algoritmes.dumbsolver import dumbsolver
import copy


def dannystra(size, bord):
    """Dit is een versie van een hill climb algoritme.

        De functie dannystra vraagt om twee argumenten: een integer
        die de bord groote aangeeft en een string die aangeeft welk bord
        opgelost moet worden.

        Het neemt een oplossing uit dumbsolve en probeert hier een betere oplossing
        van te maken.

        De functie breadth wordt aangeroepen vanuit main.py afhankelijk
        van user input.

        dannystra returned een lijst met moves tot de winnende node een geeft deze
        door aan de draw functie."""
    grid = Grid(size, bord)
    list1 = dumbsolver(size, bord)
    last_list = remove_duplicates(list1)
    counter = 0
    new_list = remove_duplicates(hillclimber(last_list, size, bord, counter))

    while len(new_list) != len(last_list):
        print(len(last_list))
        print(len(new_list))
        last_list = copy.deepcopy(new_list)
        new_list = remove_duplicates(
            hillclimber(new_list, size, bord, counter = 0))
    # in play_2 wordt gecheckt of de begingrid opnieuw tegengekomen is
    return new_list
    play_2(size, bord, new_list)


def remove_duplicates(list):
    """
    De functie remove_duplicates vraagt om een argument: een lijst met move
    dat tot een antwoord leidt.

    remove_duplicates haalt alle opeenvolgende moves van dezelfde auto uit de
    lijst. Dit wordt gedaan door twee opeenvolgende moves te vergelijken op
    dezelfde auto-id en deze moves dan samen te voegen.

    Er wordt dan een nieuwe lijst van moves dat tot een antwoord leidt.
    """
    newlist = [[0, 0, 0]]
    for move in list:
        if move[:2] == newlist[-1][:2]:
            newmove = move[:2] + [move[2]+newlist[-1][2]]
            newlist = newlist[:-1]
            newlist.append(newmove)
        elif move[0] == newlist[-1][0]:
            if move[2] > newlist[-1][2]:
                newmove = move[:2] + [move[2]-newlist[-1][2]]
                newlist = newlist[:-1]
                newlist.append(newmove)
            elif move[2] < newlist[-1][2]:
                newmove = newlist[-1][:2] + [newlist[-1][2]-move[2]]
                newlist = newlist[:-1]
                newlist.append(newmove)
            elif move[2] == newlist[-1][2]:
                newlist = newlist[:-1]
        else:
            newlist.append(move)
    return(newlist[1:])


def hillclimber(list, size, bord, counter):
    """
    De functie hillclimber vraagt om 4 argumenten: een lijst van moves dat tot
    een antwoord leidt, de grootte van het bord, een string die aangeeft welk
    bord opgelost moet worden en een teller.

    Hillclimber swapt twee moves in de lijst met elkaar om en checkt of dit tot
    een antwoord leidt.

    Echter zoekt deze versie van hillclimber slechts door de eerste 200 moves.
    Dit is om de tijd in te korten.

    Hillclimber returnt een lijst van dezelfde lengte, maar in een andere
    volgorde.
    """

    grid = Grid(size, bord)
    hc_list = solver(list, size, grid, counter)
    answer1 = []
    if counter < len(hc_list)-1:
        if len(hc_list) > 200:
            max = 199
            # Deze magicnumbers houden de timecomplexity in toom.
            # Dit betekent echter dat alleen de eerste 200 elementen van de
            # lijst worden doorzocht.
        else:
            max = len(hc_list)-2
        if counter == max:
            return hc_list
        else:
            counter += 1
            return hillclimber(hc_list, size, bord, counter)
    else:
        counter = 0
        return hillclimber(hc_list, size, bord, counter)


def solver(list, size, grid, counter):
    """
    De functie solver vraagt om vier argumenten: een lijst van moves dat tot
    een antwoord leidt, de grootte van het bord, een string die aangeeft welk
    bord opgelost moet worden en een teller.

    De functie checkt of de gegeven list uit de functie hillclimber
    leidt tot een oplossing. Zo niet, dan maakt het de omgedraaide moves dat
    in hillclimber gedaan was ongedaan.

    Het returned deze list afhankelijk van de check (on)aangepast.
    """
    answer = []
    a = copy.deepcopy(list[counter])
    b = copy.deepcopy(list[counter+1])
    list[counter] = b
    list[counter+1] = a
    for i in list:
        if i not in possiblemoves(grid):
            list[counter] = a
            list[counter+1] = b
            return(list)
        move(grid, i)
        grid.update()
        answer.append(i)
        if not win(grid, size):
            return(answer)
    list[counter] = a
    list[counter+1] = b
    return(list)
