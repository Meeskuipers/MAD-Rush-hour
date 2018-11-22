class dumbsolver():
    def dumbsolver(self):
        counter = 0
        while not self.won():
            possiblemoves = []
            possiblemoves = self.possiblemoves()
            print(possiblemoves)
            print(self.all_cars[5].position)
            if ['6','RIGHT'] in possiblemoves and self.all_cars[5].position == [['2',3],['2',4]]:
                self.move(['6','RIGHT'])
            elif self.grid[2][4] == self.grid[2][5] and self.all_cars[5].position == [['2',2],['2',3]]:
                self.move(['6',"RIGHT"])
            elif self.grid[2][3] == self.grid[2][4] == self.grid[2][5] and self.all_cars[5].position == [['2',1],['2',2]]:
                self.move(['6',"RIGHT"])
            else:
                print(self.grid[2][(self.grid[2].index("6")+2):])
                randommove = randint(0,len(possiblemoves)-1)
                print([possiblemoves[randommove][0],possiblemoves[randommove][1]])
                self.move([possiblemoves[randommove][0],possiblemoves[randommove][1]])
            counter += 1
            self.grid = self.load_grid()
            for car in self.all_cars:
                Grid(self.grid, car.id, car.position)
            for row in self.grid:
                for number in row:
                    print("", end=" ")
                    print(number, end=" ")
                print()
        print("it took "+str(counter)+" moves to win (for the computer, you're an idiot who chose solve)")

    def possiblemoves(self):
        moveList = []
        freelist = self.freelist()
        for i in self.all_cars:
            movesCar = self.calculatemove(i,freelist)
            for x in movesCar:
                moveList.append(x)
        return moveList

    def calculatemove(self, car,freelist):
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

    def freelist(self):
        freelist = []
        ycounter = 0
        for row in self.grid:
            xcounter = 0
            for x in row:
                if x == 0:
                    freelist.append([ycounter,xcounter])
                xcounter += 1
            ycounter += 1
        return freelist
