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
            movelist.append([car.id,'LEFT',1])

            if [int(car.position[0][0]),int(car.position[0][1])-2] in freelist:
                movelist.append([car.id,'LEFT',2])

                if [int(car.position[0][0]),int(car.position[0][1])-3] in freelist:
                    movelist.append([car.id,'LEFT',3])

                    if [int(car.position[0][0]),int(car.position[0][1])-4] in freelist:
                        movelist.append([car.id,'LEFT',4])

        if [int(car.position[0][0]),int(car.position[-1][1])+1] in freelist:
            movelist.append([car.id,'RIGHT',1])

            if [int(car.position[0][0]),int(car.position[-1][1])+2] in freelist:
                movelist.append([car.id,'RIGHT',2])

                if [int(car.position[0][0]),int(car.position[-1][1])+3] in freelist:
                    movelist.append([car.id,'RIGHT',3])

                    if [int(car.position[0][0]),int(car.position[-1][1])+4] in freelist:
                        movelist.append([car.id,'RIGHT',4])

    elif car.direction == 'VERTICAAL':

        if [int(car.position[0][0])-1,int(car.position[0][1])] in freelist:
            movelist.append([car.id,'UP',1])

            if [int(car.position[0][0])-2,int(car.position[0][1])] in freelist:
                movelist.append([car.id,'UP',2])

                    if [int(car.position[0][0])-3,int(car.position[0][1])] in freelist:
                        movelist.append([car.id,'UP',3])

                        if [int(car.position[0][0])-4,int(car.position[0][1])] in freelist:
                            movelist.append([car.id,'UP',4])

        if [int(car.position[-1][0])+1,int(car.position[0][1])] in freelist:
            movelist.append([car.id,'DOWN',1])

            if [int(car.position[-1][0])+2,int(car.position[0][1])] in freelist:
                movelist.append([car.id,'DOWN',2])

                if [int(car.position[-1][0])+3,int(car.position[0][1])] in freelist:
                    movelist.append([car.id,'DOWN',3])

                    if [int(car.position[-1][0])+4,int(car.position[0][1])] in freelist:
                        movelist.append([car.id,'DOWN',4])

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
