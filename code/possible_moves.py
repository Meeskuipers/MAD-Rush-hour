from class_auto import Auto
from grid import Grid
from types import *
from random import *

def possiblemoves(self):
      moveList = []
      freelist = self.freelist()
      for i in self.all_cars:
          movesCar = self.calculatemove(i,freelist)
          for x in movesCar:
              moveList.append(x)
      return moveList

  def calculatemove(self, car,freelist):
      movelist = []
      if car.direction == 'HORIZONTAAL':

          if [int(car.position[0][0]),int(car.position[0][1])-1] in freelist:
              movelist.append([car.id,'LEFT'])

          if [int(car.position[0][0]),int(car.position[-1][1])+1] in freelist:
              movelist.append([car.id,'RIGHT'])

      elif car.direction == 'VERTICAAL':

          if [int(car.position[0][0])-1,int(car.position[0][1])] in freelist:
              movelist.append([car.id,'UP'])

          if [int(car.position[-1][0])+1,int(car.position[0][1])] in freelist:
              movelist.append([car.id,'DOWN'])

      return movelist

  def freelist(self):
      freelist = []
      ycounter = 0
      for row in self.grid:
          xcounter = 0
          for x in row:
              if x == 0:
                  freelist.append([ycounter,xcounter])
              xcounter += 1
          ycounter += 1
      return freelist
