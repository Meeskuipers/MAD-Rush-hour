def informedbreadth(size,bord):
    ''' Informedbreadth takes two arguments: size and bord. size is an integer
        defining the gridsize. bord is a string pointing to the according bord
        in data. informedbreadth works like a breadth first search algoritm
        without exploring previously visited nodes to reduce the space complexity
        '''
    grid = Grid(size, bord)
    possible_moves = []
    counter = 0
    bool = True
    borddict = {}
    borddict[str(deepcopy(grid.grid))] = []
    explored = {}
    explored[str(deepcopy(grid.grid))] = [deepcopy(grid.grid)]

    while bool:
        counter += 1
        children = []
        print(counter)
        print('lengte explored: {}'.format(len(explored)))
        #loops over each child
        for x in borddict.keys():
            grid.grid = explored[x][-1]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for i in range(len(possible_moves)):
                xpath = explored.get(x)
                move(grid,[possible_moves[i][0],possible_moves[i][1],
                possible_moves[i][2]])
                grid.grid = grid.update()

                if not str(grid.grid) in explored.keys():
                    xpath.append(deepcopy(grid.grid))
                    explored[str(grid.grid)] = xpath
                    movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                    children.append(deepcopy(grid.grid))

                else:
                    #movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                grid.grid = grid.update()

        borddict = {}
        for y in children:
            borddict[str(y)] = []


        for z in borddict.keys():
            if size == 6 and explored[z][-1][2][5] == 6:
                bool = False
            elif size == 9 and explored[z][-1][4][8] == 15:
                bool = False

    print('it took' + " " + str(counter) + " " + "moves to win")
    return counter
