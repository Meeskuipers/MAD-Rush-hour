from class_auto import Auto
from grid import Grid
from types import *
from random import *

class Main():
    def __init__(self):
        self.cars = self.load_cars("autos.txt")
        self.grid = self.load_grid()
        self.grid = self.add_cars()

    #Maakt de grid aan door middel van list comprehension.
    #Het vult de grid oorspronkelijk met nullen,
    #dit staat dan tevens voor een lege plek in de grid
    def load_grid(self):
        gridsize = 6
        self.grid = [[0] * gridsize for i in range(gridsize)]
        return(self.grid)

    #Deze functie zet de informatie van een txt bestand om naar werkbare python formats
    #Door middel van readline leest hij alle informatie uit de autos.txt bestand
    def load_cars(self, filename):
        with open(filename, "r") as file_cars:
            self.all_cars = []
            for line in file_cars:
                line = line.strip()
                if line.isdigit():
                    id = line.strip()
                    line = file_cars.readline()
                    direction = line.strip()
                    line = file_cars.readline().split()
                    position = [[xy for xy in coordinate.split(',')] for coordinate in line]
                    line = file_cars.readline()
                    type = line.strip()
                    auto = Auto(id, direction, position, type)
                    self.all_cars.append(auto)

    #Deze functie voegt de ingeladen auto's van hierboven toe aan de grid
    def add_cars(self):
        for car in self.all_cars:
            Grid(self.grid, car.id, car.position)
        return(self.grid)

    def won(self):
        if self.grid[2][5] == '6':
            return(True)

    def menu(self):
        choice = input("hi! if you would to play type play. if you're an idiot, type solve!").lower()
        if choice == 'play':
            self.play()
        elif choice == 'solve':
            self.dumbsolver()

    def play(self):
        print("Heee let's play!!!")
        #Deze for loop print de grid op een elegante manier.
        for row in self.grid:
            for number in row:
                print("", end=" ")
                print(number, end=" ")
            print()
            #Door deze while loop blijft de grid uitgeprint worden nadat er een move is gedaan
            #Hij stopt pas als de 'won' functie true returnt
        while not self.won():
            command = input("> ").upper().split(',')
            self.move(command)
            self.grid = self.load_grid()
            for car in self.all_cars:
                Grid(self.grid, car.id, car.position)
            for row in self.grid:
                for number in row:
                    print("", end=" ")
                    print(number, end=" ")
                print()
        print("You won!!!")
    #Deze functie wordt aangeroepen om een move te maken.
    #Een move heeft 2 inputs nodig: de direction en car_id
    def move(self, command):
        if len(command) != 2:
            print("huh")
            return(False)
        car = int(command[0])
        direction = command[1]
        return(self.all_cars[car-1].move_car(direction))

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

if __name__ == "__main__":
    main = Main()
    main.menu()
