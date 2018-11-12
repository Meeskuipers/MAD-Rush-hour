from Grid6x6 import *
from cars6x6 import *
from freecoordinates import *
import random


allcars = [car1ver, car2ver, car3ver, car4ver, car1hor, car2hor, car3hor, car4hor, car5hor]

#the empty cache used to evade loops and the set of possible moves



#calculates possible moves
def calculatemoves(grid, allcars):
    freegrid = freefunction(grid,allcars)
    movelist = []
    for i in allcars:
        #move left
        if i[0][0] == i[1][0]:
            testleft = [i[0][0] ,i[0][1] - 1]
            if testleft in freegrid:
                movelist.append([i,'left'])
            testright = [i[0][0],i[-1][1] +1]
            if testright in freegrid:
                movelist.append([i,'right'])
        if i[0][1] == i[1][1]:
            testdown = [i[-1][0] + 1,i[1][1]]
            if testdown in freegrid:
                movelist.append([i,'down'])
            testup = [i[0][0]-1,i[0][0]]
            if testup in freegrid:
                movelist.append([i,'up'])
    return movelist

def move(car, move):
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
    cache = []
    print('*calculating rushour*')
    print("i'LL BE BACK")
    counter = 0
    while True:
        freecoords = freefunction(grid,allcars)
        cache.append(freecoords)
        possiblemoves = calculatemoves(grid,allcars)
        if len(possiblemoves) == 0:
            print('i failed')
            break
        randomint = random.randint(0,len(possiblemoves)-1)
        chosenmove = possiblemoves[randomint]
        move(chosenmove[0],chosenmove[1])
        freecoords = freefunction(grid,allcars)

        #this does not work since it will loop around
        if freecoords in cache:
            if chosenmove[1] == 'left':
                move(chosenmove[0],'right')
            if chosenmove[1] == 'right':
                move(chosenmove[0],'left')
            if chosenmove[1] == 'up':
                move(chosenmove[0],'down')
            if chosenmove[1] == 'down':
                move(chosenmove[0],'up')
        counter += 1
        if car2hor == [[3,5],[3,6]]:
            print('it took')
            print(counter)
            print('moves to find john connor')
            break

print(car5hor)
move(car5hor,'left')
print(car5hor)
