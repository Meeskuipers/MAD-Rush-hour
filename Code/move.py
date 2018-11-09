from cars6x6 import *
from Grid6x6 import *
from freecoordinates import *


#calculates the possible moves given a car x
#def calculatemove(x)
#    freelist
    #first the direction of the car is calculated.
#    horver = []
#    test1 = [x[0]]
#    test2 = [x[1]]
#    if test1[0] = test2[0]:
#        #horver with value 1 is a horizontal facing car
#        horver = [1]
        #horver with a value 2 is a vertical facing car
#    else:
#        horver = [2]
#    carlength = len(x)
#    if test1[1] -1 in freelist

def move(car, dir):
    dir = dir.lower()

    if dir == 'left':
        move = [elem[:-1] + [elem[1]-1] for elem in car]
        print(move)

    elif dir == 'right':
        move = [elem[:-1] + [elem[1]+1] for elem in car]
        if move in freecoordinates:
            return(move)
        else:
            print('That is not a valid move')

    elif dir == 'down':
        move = [[elem[0]+1] + elem[1:] for elem in car]
        return(move)

    elif dir == 'up':
        move = [[elem[0]-1] + elem[1:] for elem in car]
        return(move)

    else:
        print('That is not a valid direction. Try: left, right, up or down')

move(car4hor, 'left')
