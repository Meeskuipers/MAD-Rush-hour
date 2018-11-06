import turtle

sc=turtle.Screen()
sc.bgcolor("black")
sc.title("MAD Rush-hour")

t=turtle.Turtle()
t.speed(0)
t.pencolor("white")

def square (size,color):
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()
    t.fd(size+1)

def row (bool, size, size_board, color_1, color_2):
    for row_lenght in range(size_board):
        if bool is True:
            square(size, color_1)
            bool = False
        else:
            square(size, color_2)
            bool = True

def board (size, size_board, color_1, color_2):
    t.pu()
    t.goto(-(size*4), (size*4))
    counter = 0
    for board_lenght in range(size_board):
        if counter % 2 == 0:
            row(True, size, size_board, color_1, color_2)
            counter += 1
        else:
            row(False, size, size_board, color_1, color_2)
            counter +=1

        t.bk(size*size_board + size_board)
        t.rt(90)
        t.fd(size+1)
        t.lt(90)
    sc.exitonclick()


board(50, 8, "white", "white")
