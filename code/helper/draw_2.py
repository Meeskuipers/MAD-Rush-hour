import tkinter as tk
import time
from code.classes.class_auto import Auto
from code.classes.grid import Grid

def begin(answer, size):
    colours = ["#D2691E", "#FF7F50", "#696969", "#DAA520", "#008000", "#4B0082", "#800080", "#008080", "#0033cc", "#ff33cc"]
    canvas = background(size)
    for grid in answer:
        cars = updatecars(grid)
        draw(cars, colours, canvas,size)
    done(canvas)

def background(size):
    size = size
    width = 2+(95*size)
    height = 2+(95*size)

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

def draw(cars, colours, canvas,size):
    canvas.create_rectangle(0,0,95+95*size,95+95*size, outline="black", fill="black")
    for i in range(size):
        for x in range(size):
            canvas.create_rectangle(5+(i*95),5+(x*95),95+(i*95),95+(x*95), outline="white", fill="white")

    for car in cars:
        if car == 6:
            colour = "red"
        else:
            colour = colours[(car%len(colours))]
        canvas.create_rectangle(5+(int(cars[car][0][1])*95),5+(int(cars[car][0][0])*95),95+(int(cars[car][-1][1])*95), 95+(int(cars[car][-1][0])*95), outline=colour, fill=colour)

    canvas.update()
    time.sleep(0.5)

def done(canvas):
    canvas.mainloop()
