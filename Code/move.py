from cars6x6 import *
from Grid6x6 import *
from freecoordinates import *


def check_dir(car, dir):
    if car[0][0] == car[1][0]:
        if dir == 'up' or dir == 'down':
            return False
        else:
            return True
    elif car[0][0] != car[1][0]:
        if dir == 'up' or dir == 'down':
            return True
        else:
            return False
    else:
        return False

def check(move):
    size_board = grid[-1][-1]
    occupiedcoordinates = occupiedfuntion(allcars)
    if move in occupiedcoordinates:
        return(False)
    for xy in move:
        if xy > size_board or xy < 1:
            return(False)
    return(True)

def move(car, dir):
    dir = dir.lower()
    if dir == 'left':
        if not check_dir(car,dir) :
            print("No valid move")
            return False
        move = [elem[:-1] + [elem[1]-1] for elem in car]
        check_move = move[0]
        if check(check_move):
            print(move)
        else:
            print("No valid move")
            return False

    elif dir == 'right':

        if not check_dir(car,dir):
            print("No valid move")
            return False
        move = [elem[:-1] + [elem[1]+1] for elem in car]
        check_move = move[-1]
        if check(check_move):
            print(move)
        else:
            print("No valid move")
            return False

    elif dir == 'down':
<<<<<<< HEAD

        move = [[elem[0]-1] + elem[1:] for elem in car]
        check_dir = True
        check_dir = check_dir(car, dir)
        if check_dir == False:
=======
        if not check_dir(car,dir):
>>>>>>> 0bab9bbb48949179be13ff807ccb566636947907
            print("No valid move")
            return False
        move = [[elem[0]+1] + elem[1:] for elem in car]
        check_move = move[-1]

        if check(check_move):
            print(move)
        else:
            print("No valid move")
            return False

    elif dir == 'up':
<<<<<<< HEAD
        move = [[elem[0]+1] + elem[1:] for elem in car]

        check_dir = check_dir(car, dir)
        if check_dir == False:
=======
        if not check_dir(car,dir):
>>>>>>> 0bab9bbb48949179be13ff807ccb566636947907
            print("No valid move")
            return False
        move = [[elem[0]-1] + elem[1:] for elem in car]
<<<<<<< HEAD

=======
>>>>>>> 0bab9bbb48949179be13ff807ccb566636947907
        check_move = move[0]
        if check(check_move):
            print(move)
        else:
            print("No valid move")
            return False

    else:
        print('That is not a valid direction. Try: left, right, up or down')

move(car1ver,'down')
