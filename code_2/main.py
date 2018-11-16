from class_auto import Auto
from grid import Grid
from types import *

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
            move = self.move(command)
            if not move:
                print("Invalid move")
            else:
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
        return(self.all_cars[car-1].move_car(direction, self.grid))


if __name__ == "__main__":
    main = Main()
    main.play()
