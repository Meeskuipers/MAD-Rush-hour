import tkinter as tk
import time
from code.classes.class_auto import Auto
from code.classes.grid import Grid


def begin(answer, size):
    colours = ["#D2691E", "#FF7F50", "#696969", "#DAA520", "#008000",
                    "#4B0082", "#800080", "#008080", "#0033cc", "#ff33cc"]
    back_ground = background(size)
    canvas = back_ground[0]
    exp = back_ground[1]
    for grid in answer:
        cars = updatecars(grid)
        draw(cars, colours, canvas, size, exp)
    done(canvas)


def background(size):
    size = size
    if size == 6:
        exp = 95
    elif size == 9:
        exp = 75
    else:
        exp = 60
    width = 2 + (exp * size)
    height = 2 + (exp * size)

    window = tk.Tk()

    canvas = tk.Canvas(window, bg="black", height=height, width=width)
    canvas.pack()
    return([canvas, exp])


def updatecars(bord):
    cardict = {}
    rowcounter = 0
    for row in bord:
        icounter = 0
        for i in row:
            if i:
                if not cardict.get(i, 0):
                    cardict[i] = [[rowcounter, icounter]]
                else:
                    cardict[i].append([rowcounter, icounter])
            icounter += 1
        rowcounter += 1
    return cardict


def draw(cars, colours, canvas, size, exp):
    canvas.create_rectangle(0, 0,
                            exp + exp * size,
                            exp + exp * size,
                            outline="black", fill="black")
    for i in range(size):
        for x in range(size):
            canvas.create_rectangle(5 + (i * exp),
                                    5 + (x * exp),
                                    exp + (i * exp),
                                    exp + (x * exp),
                                    outline="white", fill="white")

    for car in cars:
        if car == 6:
            colour = "red"
        else:
            colour = colours[(car % len(colours))]
        canvas.create_rectangle(5 + (int(cars[car][0][1]) * exp),
                                5 + (int(cars[car][0][0]) * exp),
                                exp + (int(cars[car][-1][1]) * exp),
                                exp + (int(cars[car][-1][0]) * exp),
                                outline=colour, fill=colour)

    canvas.update()
    canvas.delete("all")
    time.sleep(0.1)


def done(canvas):
    canvas.mainloop()
