
#de class auto definieert autos binnen onze grid. iedere auto heeft een id nummer,
#direction, positie en een type
class Auto(object):
    def __init__(self, id, direction, position, type):
        self.id = id
        self.direction = direction
        self.position = position
        self.type =  type

#move_car is redelijk self explanatory. move_car geeft de gespecificeerde auto
#een andere positie afhankelijk van de gespecificeerde command.
    def move_car(self, direction, grid):
        #beweegt de auto naar links
        if direction == 'LEFT':
            self.position = [[elem[0],int(elem[1])-1] for elem in self.position]

        #beweegt de auto naar rechts
        elif direction == 'RIGHT':
            self.position = [[elem[0],int(elem[1])+1] for elem in self.position]

        #beweegt de auto naar boven
        elif direction == 'UP':
            self.position = [[int(elem[0])-1,elem[1]] for elem in self.position]

        #beweegt de auto naar beneden
        elif direction == 'DOWN':
            self.position = [[int(elem[0])+1,elem[1]] for elem in self.position]
            
    def __str__(self):
        return f"{self.id}\n{self.position}\n{self.direction}{self.type}\n"
