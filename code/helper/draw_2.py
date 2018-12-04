import tkinter as tk
import time
from code.classes.class_auto import Auto
from code.classes.grid import Grid

def begin():
    colours = ["#D2691E", "#FF7F50", "#696969", "#DAA520", "#008000", "red", "#4B0082", "#800080", "#008080"]
    answer =[[[0, 1, 1, 2, 2, 2], [0, 3, 3, 4, 5, 5], [6, 6, 7, 4, 0, 8], [9, 9, 7, 10, 10, 8], [11, 0, 12, 0, 13, 13], [11, 0, 12, 0, 0, 0]], [[1, 1, 0, 2, 2, 2], [0, 3, 3, 4, 5, 5], [6, 6, 7, 4, 0, 8], [9, 9, 7, 10, 10, 8], [11, 0, 12, 0, 13, 13], [11, 0, 12, 0, 0, 0]], [[1, 1, 0, 2, 2, 2], [3, 3, 0, 4, 5, 5], [6, 6, 7, 4, 0, 8], [9, 9, 7, 10, 10, 8], [11, 0, 12, 0, 13, 13], [11, 0, 12, 0, 0, 0]], [[1, 1, 0, 2, 2, 2], [3, 3, 0, 4, 5, 5], [6, 6, 7, 4, 0, 8], [9, 9, 7, 10, 10, 8], [11, 0, 12, 13, 13, 0], [11, 0, 12, 0, 0, 0]], [[1, 1, 0, 2, 2, 2], [3, 3, 0, 4, 5, 5], [6, 6, 7, 4, 0, 0], [9, 9, 7, 10, 10, 0], [11, 0, 12, 13, 13, 8], [11, 0, 12, 0, 0, 8]], [[1, 1, 7, 2, 2, 2], [3, 3, 7, 4, 5, 5], [6, 6, 0, 4, 0, 0], [9, 9, 0, 10, 10, 0], [11, 0, 12, 13, 13, 8], [11, 0, 12, 0, 0, 8]], [[1, 1, 7, 2, 2, 2], [3, 3, 7, 4, 5, 5], [6, 6, 0, 4, 0, 0], [9, 9, 0, 0, 10, 10], [11, 0, 12, 13, 13, 8], [11, 0, 12, 0, 0, 8]]]
    canvas = background()
    for grid in answer:
        cars = updatecars(grid)
        draw(cars, colours, canvas)
    done(canvas)

def background():
    size = 6
    width = 2+(95*size)
    height = 2+(95*6)

    window = tk.Tk()

    canvas = tk.Canvas(window, bg="black", height=height,width=width)
    canvas.pack()
    return(canvas)

def updatecars(bord):
    cardict = {}
    rowcounter = 0
    for row in bord:
        icounter = 0
        for i in row:
            if i :
                if not cardict.get(i, 0):
                    cardict[i] = [[rowcounter,icounter]]
                else:
                    cardict[i].append([rowcounter,icounter])
            icounter += 1
        rowcounter += 1
    return cardict

def draw(cars, colours, canvas):
    canvas.create_rectangle(0,0,95+95*6,95+95*6, outline="black", fill="black")
    for i in range(6):
        for x in range(6):
            canvas.create_rectangle(5+(i*95),5+(x*95),95+(i*95),95+(x*95), outline="white", fill="white")

    for car in cars:
        canvas.create_rectangle(5+(int(cars[car][0][1])*95),5+(int(cars[car][0][0])*95),95+(int(cars[car][-1][1])*95), 95+(int(cars[car][-1][0])*95), outline=colours[(car%len(colours))], fill=colours[(car%len(colours))])

    canvas.update()
    time.sleep(1)

def done(canvas):
    canvas.mainloop()
