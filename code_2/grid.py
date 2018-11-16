# Deze class definieerd de grid en implementeerd de auto's
class Grid(object):
    def __init__(self, grid, car_id, car_start_position):
        self.grid = grid
        self.car = self.add_cars(car_start_position, car_id)
        self.car_id = car_id
        self.car_start_position = car_start_position

    def add_cars(self, car_start_position, car_id):
        for len in car_start_position:
            cor_1 = int(len[0])
            cor_2 = int(len[1])
            self.grid[cor_1][cor_2] = car_id



    def __str__(self):
        return(self.grid)
