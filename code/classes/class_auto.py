class Auto(object):
    def __init__(self, id, direction, position, type):
        self.id = id
        self.direction = direction
        self.position = position
        self.type = type

    def move_car(self, direction, times):
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
