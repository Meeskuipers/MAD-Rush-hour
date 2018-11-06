import turtle

def board (x,y,width,color):

    turtle.penup()
    turtle.pencolor("grey")
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()

    for x in range(4):
        turtle.forward(40)
        turtle.left(90)

    turtle.end_fill()

board(30,30,30,"red")

turtle.exitonclick()
