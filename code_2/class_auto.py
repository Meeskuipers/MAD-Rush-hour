class Auto(object):
    def __init__(self, id, start_position, direction, type):
        id = id
        start_position = start_position
        direction = direction
        type =  type

    def __str__(self):
        return f"{self.id}{self.start_position}{self.direction}{self.type}\n"
