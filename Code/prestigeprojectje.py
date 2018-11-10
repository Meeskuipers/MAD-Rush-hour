from Grid6x6 import *
from cars6x6 import *
from freecoordinates import *
import random


allcars = [car1ver, car2ver, car3ver, car4ver, car1hor, car2hor, car3hor, car4hor, car5hor]

#the empty cache used to evade loops and the set of possible moves
cache = []
possiblemoves = []

#calculates possible moves
def calculatemoves(grid,allcars):
    freelist = freefunction(grid, allcars)

    for i in allcars:
        if i[0][0] == i[1][0]:
            trymoveright = i
            trymoveright.pop(0)
            updatevariable = trymoveright[0][1]
            trymoveright[0][1] = updatevariable + 1
            if trymoveright in freelist:
                possiblemoves.append([i,'right'])

            trymoveleft = i
            trymoveleft.pop(1)
            updatevariable = trymoveleft[0][1]
            trymoveleft[0][1] = updatevariable - 1
            if trymoveleft in freelist:
                possiblemoves.append([i,'left'])

        if i[0][1] == i[1][1]:
            trymovedown = i
            trymovedown.pop(0)
            updatevariable = trymovedown[0][0]
            trymovedown.append(updatevariable+1)

            if trymovedown in freelist:
                possiblemoves.append([i,'down'])

            trymoveup = i
            trymoveup.pop(1)
            updatevariable = trymoveup[0][0]
            trymoveup[0][0] = updatevariable - 1
            if trymoveup in freelist:
                possiblemoves.append([i,'up'])
        return possiblemoves


def move(grid, car):
    newpos = []
    if move == 'left':
        for i in range(0,len(car)-1):
            newpos.append(car[i-1][1] -1)
        car = newpos
    elif move == 'right':
        for i in range(0,len(car)-1):
            newpos.append(car[i-1][1] +1)
            car = newpos
    elif move == 'up':
        for i in range(0,len(car)-1):
            newpos.append(car[i-1][0] -1)
            car = newpos
    elif move == 'down':
        for i in range(0,len(car)-1):
            newpos.append(car[i-1][0] +1)
            car = newpos



def solve(grid, allcars):
    print('*calculating rushour*')
    print("i'LL BE BACK")
    cache.append(grid)
    counter = 0
    while True:
        possiblemoves = calculatemoves(grid,allcars)
        randomint = random.randint(0,len(possiblemoves)-1)
        chosenmove = possiblemoves[randomint]
        move(chosenmove[0],chosenmove[1])
        counter += 1
        if car2hor == [[3,5],[3,6]]:
            print('you did it!')
            print('it took you' + counter + 'moves')
            break

print(calculatemoves(grid,allcars))
