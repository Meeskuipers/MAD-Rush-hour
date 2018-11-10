from Grid6x6 import *
from cars6x6 import *
from move import *
from freecoordinates import *

#The main file where the code comes together

def run(grid,allcars):
    print('welcome to this scratch version of rush hour!')
    counter = 0
    while True:
        freecoords = freefunction(grid,allcars)
        print(allcars)
        print('select a car you want to move')
        cartomove = input('select a car you want to move:')
        print (freecoords)
        inputdirection = input('in wich direction would you like to move your car:')
        direction = str(inputdirection)

        if move(cartomove,direction) == False:
            print('invalid move or car. Select a car from the list and use directions up, down, left or right')

        else:
            move(cartomove,direction)

        if car2hor == [[3,5],[3,6]]:
            print('you did it!')
            break
        counter += 1

run(grid,allcars)
