class Auto(object):
    def __init__(self, id, direction, position, type):
        self.id = id
        self.direction = direction
        self.position = position
        self.type =  type

    def move_car(self, direction):
        if direction == 'LEFT':
            if self.direction == "VERTICAAL":
                return False
            else:
                position = [[elem[0],int(elem[1])-1] for elem in self.position]
                print(position)
                return True
        elif direction == 'RIGHT':
            if self.direction == "VERTICAAL":
                return False
            else:
                position = [[elem[0],int(elem[1])+1] for elem in self.position]
                return True

        elif direction == 'UP':
            if self.direction == "HORIZONTAAL":
                return False
            else:
                position = [[int(elem[0])-1,elem[1]] for elem in self.position]
                return True

        elif direction == 'DOWN':
            if self.direction == "HORIZONTAAL":
                return False
            else:
                position = [[int(elem[0])+1,elem[1]] for elem in self.position]
                return True
        else:
            return False

    def __str__(self):
        return f"{self.id}\n{self.position}\n{self.direction}{self.type}\n"
