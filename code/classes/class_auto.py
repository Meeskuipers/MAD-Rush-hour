class Auto(object):
    ''' Deze Class definieert de auto's op het rush hour bord. Auto's hebben
        een ID, een richting, een positie en een type.'''
    def __init__(self, id, direction, position, type):
        self.id = id
        self.direction = direction
        self.position = position
        self.type = type

    def move_car(self, direction, times):
        ''' Deze functie heeft twee argumenten: de richting waarin een Auto
            bewogen moet worden en hoeveel stappen de auto moet maken.

            Deze functie wordt aangeroepen vanuit de move functie om de positie
            van een specifieke auto to wijzigen.'''
        for i in range(0, int(times)):

            if direction == 'LEFT':
                self.position = [[elem[0],
                                  int(elem[1])-1] for elem in self.position]

            elif direction == 'RIGHT':
                self.position = [[elem[0],
                                  int(elem[1])+1] for elem in self.position]

            elif direction == 'UP':
                self.position = [[int(elem[0])-1,
                                  elem[1]] for elem in self.position]

            elif direction == 'DOWN':
                self.position = [[int(elem[0])+1,
                                  elem[1]] for elem in self.position]

    def __str__(self):
        return f"{self.id}\n{self.position}\n{self.direction}{self.type}\n"
