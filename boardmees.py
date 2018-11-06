import turtle

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
    # Sluit het programma pas als er geklikt word
    sc.exitonclick()


board(50, 8, "white")
