from code.classes.class_auto import Auto


class Grid(object):

    def __init__(self, size, bord):
        self.load_cars(bord)
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
                    position = [[xy for xy in coordinate.split(',')]
                                for coordinate in line]
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
        # draw(self.all_cars)

    def update(self):
        self.load_grid()
        self.add_cars()
        return(self.grid)

    def won(self):
        if self.grid[2][5] == 6:
            return True

    def updatecars(self):
        cardict = {}
        rowcounter = 0
        for row in self.grid:
            icounter = 0
            for i in row:

                if not cardict.get(i, 0):
                    cardict[i] = [[rowcounter, icounter]]
                else:
                    cardict[i].append([rowcounter, icounter])
                icounter += 1
            rowcounter += 1

        for key in cardict.keys():
            for car in self.all_cars:
                if key == car.id:
                    car.position = cardict[key]

    def calculatemove(self, free_list):
        movelist = []
        for car in self.all_cars:
            if car.direction == 'HORIZONTAAL':
                for i in range(self.size):
                    if ((int(car.position[0][1])-(i+1)) > -1):
                        if [int(car.position[0][0]),
                            int(car.position[0][1])-(i+1)] in free_list:
                                movelist.append([car.id,'LEFT',(i+1)])
                        else:
                            break

                for i in range(self.size):
                    if [int(car.position[0][0]),
                        int(car.position[-1][1])+(i+1)] in free_list:
                            movelist.append([car.id,'RIGHT',(i+1)])
                    else:
                        break


            elif car.direction == 'VERTICAAL':
                for i in range(self.size):
                    if ((int(car.position[0][0])-(i+1)) > -1):
                        if [(int(car.position[0][0]))-(i+1),
                             int(car.position[0][1])] in free_list:
                                movelist.append([car.id, 'UP',(i+1)])
                        else:
                            break

                for i in range(self.size):
                    if [(int(car.position[-1][0])+(i+1)),
                          int(car.position[0][1])] in free_list:
                            movelist.append([car.id, 'DOWN',(i+1)])
                    else:
                        break
        return movelist
