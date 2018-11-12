class Auto(object):
    def __init__(self, id, direction, start_position, type):
        self.id = id
        self.direction = direction
        self.start_position = start_position
        self.type =  type

    def __str__(self):
        return f"{self.id}\n{self.start_position}\n{self.direction}{self.type}\n"
