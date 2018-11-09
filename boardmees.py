import turtle
from cars6x6_test import *

sc=turtle.Screen()
# Dit is voor de achtergrond kleur en de titel van het turtle bestand
sc.bgcolor("black")
sc.title("MAD Rush-hour")

# Turtle moet voor elk beweging aangeroepen worden dus heb het afgekort naar t
t=turtle.Turtle()
# Snelheid 0 is het snelst, maar zou eigenlijk sneller kunnen
t.speed(0)
t.pencolor("white")

# square tekent elke square
def square (size,color):
    t.color(color)
    t.begin_fill()
    # Turtle tekent elke zeide door elke rib apart te tekenen en dan met 90
    # graden te draaien. Daarna wordt het gevuld met de color.
    for x in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()
    # Plus één is gedaan zodat er een mooit witregel er tussen in komt.
    t.fd(size+1)

# row stuurt square net zo lang aan totdat de opgegeven size is gehaald.
def row (size, size_board, color):
    # Roept square net zo lang aan totdat de rij af is.
    for row_lenght in range(size_board):
        square(size, color)

def board (size, size_board, color):
    # pu haalt de pen van het papier zodat er niet getekent word
    t.pu()
    # verplaats weer terug naar het begin
    t.goto(-(size*4), (size*4))
    for board_lenght in range(size_board):
        row(size, size_board, color)
        t.bk(size*size_board + size_board)
        t.rt(90)
        t.fd(size+1)
        t.lt(90)
    #Sluit het programma pas als er geklikt word
    cars(size)

def cars (size, size_board):
    t.pu()
    t.goto(-(size*4), (size*-1))
    t.color("white")
    t.begin_fill()
    for i in range(4):
        t.fd(size*size_board)
        t.lt(90)
    t.end_fill()
    for car in allcars:
        cor_1 = car[0][0]
        cor_2 = car[1][0]
        if cor_1 == cor_2:
            print("Verticaal")
            t.pu()
            t.goto((size*cor_1), (size*(car[0][1]-1)))
            t.color("blue")
            t.begin_fill()
            if len(car) == 3:
                t.fd(size)
                t.lt(90)
                t.fd(size*2)
                t.lt(90)
                t.fd(size)
                t.lt(90)
                t.fd(size*3)
                t.lt(90)
                t.fd(size)
                t.lt(90)
                t.fd(size)
                t.rt(90)
            else:
                for i in range(2):
                    t.fd(size)
                    t.lt(90)
                    t.fd(size*2)
                    t.lt(90)
            t.end_fill()

        else:
            t.pu()
            t.goto((size*(cor_1)), (size*car[0][1]))
            t.color("yellow")
            t.begin_fill()
            for i in range(2):
                t.fd(size*len(car))
                t.lt(90)
                t.fd(size)
                t.lt(90)
            t.end_fill()
            print("Horizontaal")

    sc.exitonclick()

cars(50, 6)
