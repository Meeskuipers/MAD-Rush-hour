from code.classes.class_auto import Auto


class Grid(object):
    '''Deze class definieert een speelboord van het rush hour spel. Iedere
       instance van class Grid wordt gebouwd vanuit een size en een specifieke
       invulling die gedefinieerd wordt vanuit een text file'''
    def __init__(self, size, bord):
        self.load_cars(bord)
        self.size = size
        self.load_grid()
        self.add_cars()

    def load_grid(self):
        ''' Deze functie wordt aangeroepen als een grid aangemaakt wordt
            en bouwt de initiele structuur van de grid als nested lists'''
        self.grid = [[0] * self.size for i in range(self.size)]

    def load_cars(self, filename):
        ''' Deze functie voegt de autos toe aan de grid nadat load_grid is
            aangeroepen. Deze functie heeft als argument een filename die
            ingelezen wordt om de auto posities te bepalen.'''
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
        ''' Deze functie wordt aangeroepen vanuit load_cars om een specifieke
            auto toe te voegen aan de grid. De auto wordt toegevoegd door een
            vakje zonder auto (gerepresenteerd door de waarde 0) up te daten
            met de car ID'''
        for car in self.all_cars:
            for len in car.position:
                cor_1 = int(len[0])
                cor_2 = int(len[1])
                self.grid[cor_1][cor_2] = car.id
        # draw(self.all_cars)

    def update(self):
        '''Deze functie wordt aangeroepen vanuit algoritmes om het bord up te
           daten wanneer auto posities geupdate worden

           Deze functie returned de nieuwe grid nadat deze geupdate is.'''
        self.load_grid()
        self.add_cars()
        return(self.grid)

    def updatecars(self):
        '''Deze functie wordt aangeroepen vanuit algoritmes om de instances
           van alle autos te updaten afhankelijk van de nieuwe grid.'''
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
        '''Deze functie wordt aangeroepen vanuit possiblemoves en heeft een
           argument: freelist is een lijst met coördinaten in de grid zonder
           auto op dat coördinaat.

           Calculatemove returned een lijst met commands die gedaan kunnen
           op het huidige bord afhankelijk van de auto posities.

           calculatemove returned de mogelijke moves voor een specifieke auto
           '''
        movelist = []
        for car in self.all_cars:
            if car.direction == 'HORIZONTAAL':
                for i in range(self.size):
                    if ((int(car.position[0][1]) - (i + 1)) > -1):
                        if [int(car.position[0][0]),
                                int(car.position[0][1]) - (i + 1)] in free_list:
                                    movelist.append([car.id, 'LEFT', (i + 1)])
                        else:
                            break

                for i in range(self.size):
                    if [int(car.position[0][0]),
                            int(car.position[-1][1]) + (i + 1)] in free_list:
                                movelist.append([car.id, 'RIGHT', (i + 1)])
                    else:
                        break

            elif car.direction == 'VERTICAAL':
                for i in range(self.size):
                    if ((int(car.position[0][0]) - (i + 1)) > -1):
                        if [(int(car.position[0][0])) - (i + 1),
                                int(car.position[0][1])] in free_list:
                                    movelist.append([car.id, 'UP', (i + 1)])
                        else:
                            break

                for i in range(self.size):
                    if [(int(car.position[-1][0]) + (i+1)),
                            int(car.position[0][1])] in free_list:
                                movelist.append([car.id, 'DOWN', (i + 1)])
                    else:
                        break
        return movelist
