from class_auto import Auto

# Deze class definieerd de grid en implementeerd de auto's
class Grid(object):

    def __init__(self,size):
        self.load_cars('autos.txt')
        self.size = size
        self.load_grid()
        self.add_cars()

    def load_grid(self):
        self.grid = [[0] * self.size for i in range(self.size)]

    def load_cars(self, filename):
        ''' docstring placeholder '''
        with open(filename, "r") as file_cars:
            self.all_cars = []
            for line in file_cars:
                line = line.strip()
                if line.isdigit():
                    id = int(line.strip())
                    line = file_cars.readline()
                    direction = line.strip()
                    line = file_cars.readline().split()
                    position = [[xy for xy in coordinate.split(',')] for coordinate in line]
                    line = file_cars.readline()
                    type = line.strip()
                    auto = Auto(id, direction, position, type)
                    self.all_cars.append(auto)

    def add_cars(self):
        for car in self.all_cars:
            for len in car.position:
                    cor_1 = int(len[0])
                    cor_2 = int(len[1])
                    self.grid[cor_1][cor_2] = car.id

    def update(self):
        self.load_grid()
        foself.add_cars()
