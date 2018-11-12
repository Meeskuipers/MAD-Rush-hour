from Grid6x6 import *
from cars6x6 import *
from freecoordinates import *
import random

movelist1 = ['up','down']
movelist2 = ['left','right']

#the empty cache used to evade loops and the set of possible moves
cache = []
possiblemoves = []

#calculates possible moves
def calculatemoves(grid,allcars):
    cache.append(grid)
    freelist = freefunction(grid, allcars)

    for i in allcars:
        if i[0][0] == i[1][0]:
            trymoveright = i.pop(0)
            trymoveright[0][1] = trymoveright[0][1] + 1
            if trymoveright in freelist:
                possiblemoves.append([i,'right'])
            trymoveleft = i.pop(1)
            trymoveleft[0][1] = trymoveleft[0][1] - 1
            if trymoveleft in freelist:
                possiblemoves.append([i,'left'])
        if i[0][1] == i[1][1]:
            trymovedown = i.pop(0)
            trymovedown[0][0] = trymovedown[0][0] + 1
            if trymovedown in freelist:
                possiblemoves.append([i,'down'])
            trymoveup = i.pop(0)
            trymoveup[0][0] = trymoveup[0][0] - 1
            if trymoveup in freelist:
                possiblemoves.append([i,'up'])
        return freelist


def move(grid, car):
    newpos = []
    if move == 'left':
        for i in range(len(car)):
            newpos.append(car[i-1][1] -1)
    elif move == 'right':
        for i in range(len(car)):
            newpos.append(car[i-1][1] +1)
    elif move == 'up':
        for i in range(len(car)):
            newpos.append(car[i-1][0] -1)
    elif move == 'down':
        for i in range(len(car)):
            newpos.append(car[i-1][0] +1)



def solve(grid, allcars):
    print('*calculating rushour*')
    print("i'LL BE BACK")
    cache.append(grid)
    counter = 0
    while True:
        possiblemoves = calculatemoves(grid,allcars)
        randomint2 = random.randint(0,len(possiblemoves))
        chosenmove = possiblemoves[randomint2]
        move(chosenmove[0],chosenmove[2])
        counter += 1
        if if car2hor == [[3,5],[3,6]]:
            print('you did it!')
            print('it took you' + counter + 'moves')
            break

solve(grid, allcars)
