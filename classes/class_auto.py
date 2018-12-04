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
    def move_car(self, direction, times):
        for i in range(0,int(times)):
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

    def calculatemove(self,freelist):

        movelist = []
        if self.direction == 'HORIZONTAAL':
            # i = 1
            # while([int(self.position[0][0]),int(self.position[0][1])-i] in freelist):
            #     movelist.append([self.id,'LEFT',i])
            #     i += 1
            if [int(self.position[0][0]),int(self.position[0][1])-1] in freelist:
                movelist.append([self.id,'LEFT',1])

                if [int(self.position[0][0]),int(self.position[0][1])-2] in freelist:
                    movelist.append([self.id,'LEFT',2])

                    if [int(self.position[0][0]),int(self.position[0][1])-3] in freelist:
                        movelist.append([self.id,'LEFT',3])

                        if [int(self.position[0][0]),int(self.position[0][1])-4] in freelist:
                            movelist.append([self.id,'LEFT',4])
            # i = 1
            # while([int(self.position[0][0]),int(self.position[-1][1])+i] in freelist):
            #     movelist.append([self.id,'RIGHT',i])
            #     i += 1
            if [int(self.position[0][0]),int(self.position[-1][1])+1] in freelist:
                movelist.append([self.id,'RIGHT',1])

                if [int(self.position[0][0]),int(self.position[-1][1])+2] in freelist:
                    movelist.append([self.id,'RIGHT',2])

                    if [int(self.position[0][0]),int(self.position[-1][1])+3] in freelist:
                        movelist.append([self.id,'RIGHT',3])

                        if [int(self.position[0][0]),int(self.position[-1][1])+4] in freelist:
                            movelist.append([self.id,'RIGHT',4])

        elif self.direction == 'VERTICAAL':
            # i = 1
            # while([int(self.position[0][0])-i,int(self.position[0][1])] in freelist):
            #     movelist.append([self.id,'UP',i])
            #     i += 1
            if [int(self.position[0][0])-1,int(self.position[0][1])] in freelist:
                movelist.append([self.id,'UP',1])

                if [int(self.position[0][0])-2,int(self.position[0][1])] in freelist:
                    movelist.append([self.id,'UP',2])

                    if [int(self.position[0][0])-3,int(self.position[0][1])] in freelist:
                        movelist.append([self.id,'UP',3])

                        if [int(self.position[0][0])-4,int(self.position[0][1])] in freelist:
                            movelist.append([self.id,'UP',4])
            # i = 1
            # while([int(self.position[-1][0])+i,int(self.position[0][1])] in freelist):
            #     movelist.append([self.id,'DOWN',i])
            #     i += 1
            if [int(self.position[-1][0])+1,int(self.position[0][1])] in freelist:
                movelist.append([self.id,'DOWN',1])

                if [int(self.position[-1][0])+2,int(self.position[0][1])] in freelist:
                    movelist.append([self.id,'DOWN',2])

                    if [int(self.position[-1][0])+3,int(self.position[0][1])] in freelist:
                        movelist.append([self.id,'DOWN',3])

                        if [int(self.position[-1][0])+4,int(self.position[0][1])] in freelist:
                            movelist.append([self.id,'DOWN',4])
        return movelist

    def __str__(self):
        return f"{self.id}\n{self.position}\n{self.direction}{self.type}\n"
