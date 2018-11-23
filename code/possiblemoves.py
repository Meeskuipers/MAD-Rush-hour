from grid import *



def possiblemoves(grid):
    moveList = []
    free_list = freelist(grid)
    for i in grid.all_cars:
        movesCar = calculatemove(i,free_list)
        for x in movesCar:
            moveList.append(x)
    return moveList


def calculatemove(car,freelist):
    movelist = []
    if car.direction == 'HORIZONTAAL':

        if [int(car.position[0][0]),int(car.position[0][1])-1] in freelist:
            movelist.append([car.id,'LEFT'])

        if [int(car.position[0][0]),int(car.position[-1][1])+1] in freelist:
            movelist.append([car.id,'RIGHT'])

    elif car.direction == 'VERTICAAL':

        if [int(car.position[0][0])-1,int(car.position[0][1])] in freelist:
            movelist.append([car.id,'UP'])

        if [int(car.position[-1][0])+1,int(car.position[0][1])] in freelist:
            movelist.append([car.id,'DOWN'])

    return movelist

def freelist(grid):
    freelist = []
    ycounter = 0
    for row in grid.grid:
        xcounter = 0
        for x in row:
            if x == 0:
                freelist.append([ycounter,xcounter])
            xcounter += 1
        ycounter += 1
    return freelist
