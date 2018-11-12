from class_auto import Auto

class Main():
    def __init__(self):
        self.cars = self.load_cars("autos.txt")
        print('dit zou het moeten doen')
        self.grid = ''

    def run(self, grid, ):
        print('deze ook')

    def load_cars(self, filename):
        with open(filename, "r") as file_cars:
            self.all_cars = []
            for line in file_cars:
                line = line.strip()
                if line.isdigit():
                    id = line
                    line = file_cars.readline()
                    direction = line
                    line = file_cars.readline()
                    start_position = line
                    line = file_cars.readline()
                    type = line
                    auto = Auto(id, direction, start_position, type)
                    self.all_cars.append(auto)
                    print(auto)



Main = Main()
