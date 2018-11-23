from class_auto import Auto
from grid import Grid
from possiblemoves import *
from types import *
from random import *

def play(size):
    ''' docstring placeholder '''
    counter = 0
    print("Heee let's play!!!")
    playgrid = Grid(size)
    while not won():
        command = input("> ").upper().split(',')
        move(command)
        playgrid.update()
    print('it took you' + str(counter) + 'moves to win')


#def won():
    #universeel optionneel if wincar op laatste positie in row


def move(command):
    ''' docstring placeholder '''
    if len(command) != 2:
        print("huh")
        return(False)
    car = int(command[0])
    direction = command[1]
    return(self.all_cars[car-1].move_car(direction))


# def play(self):
#     print("Heee let's play!!!")
#     #Deze for loop print de grid op een elegante manier.
#     for row in self.grid:
#         for number in row:
#             print("", end=" ")
#             print(number, end=" ")
#         print()
#         #Door deze while loop blijft de grid uitgeprint worden nadat er een move is gedaan
#         #Hij stopt pas als de 'won' functie true returnt
#     while not self.won():
#         command = input("> ").upper().split(',')
#         self.move(command)
#         self.grid = self.load_grid()
#         for car in self.all_cars:
#             Grid(self.grid, car.id, car.position)
#         for row in self.grid:
#             for number in row:
#                 print("", end=" ")
#                 print(number, end=" ")
#             print()
#     print("You won!!!")
