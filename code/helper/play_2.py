from code.classes.class_auto import Auto
from code.classes.grid import Grid
from types import *
from random import *
# from code.helper.draw import draw
from code.helper.draw_2 import begin
from code.helper.random_oplossing import list
# from code.algoritmes.dannystra import dannystra

def play_2(size,bord,list):
    ''' docstring placeholder '''
    counter = 0
    playgrid = Grid(size,bord)
    answer = []
    answer.append(playgrid.grid)
    for i in list:
        move(playgrid,i)
        playgrid.update()
        for grid in answer:
            if x == playgrid:
                print("huh")
                answer = []
        answer.append(playgrid.grid)
        counter = counter + 1
    begin(answer)
    print('it took you ' + str(counter) + ' moves to win')

def move(grid,command):
    ''' docstring placeholder '''
    if len(command) != 3:
        print("huh")
        return(False)
    car = int(command[0])
    direction = command[1]
    times = command[2]
    grid.all_cars[car-1].move_car(direction,times)


def printgrid(grid):
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()
