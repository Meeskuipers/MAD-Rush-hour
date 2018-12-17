import tkinter as tk
import time
from code.classes.class_auto import Auto
from code.classes.grid import Grid


def begin(answer, size):
    """
    Begin is de main functie voor het tekenen van de grids. Deze functie heeft
    twee argumenten: een lijst met de volgorde van alle grids en een integer
    voor het bepalen van de groote van het boord.

    Begin visualiseert met behulp van tKinter de borden. Hierbij wordt een grid
    omgezet naar een overzichtelijke visualisatieselfself.

    Deze functie wordt aangeropen door play_2.
    """
    if len(answer) < 50:
        rest = 0.5
    elif len(answer) < 150:
        rest = 0.25
    else:
        rest = 0.1
    back_ground = background(size)
    canvas = back_ground[0]
    exp = back_ground[1]
    for grid in answer:
        cars = updatecars(grid)
        draw(cars, canvas, size, exp, rest)


def background(size):
    """
    In de background functie wordt de achtergrond van het geopende zwart
    tKinter tablat zwart gemaakt.

    De functie vraagt om één argument: een interger die de groote van het boord
    aangeeft.

    De functie wordt aangeropen door begin.

    De backgrond functie returned een tKinter canvas die in de draw functie
    wordt gebruikt.
    """
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
    """
    In de updatecars functie wordt voor elke grid een dictionary gemaakt.
    Hierbij zijn de keys de car.id en de values de coordinaten van de auto.
    Deze grid coordinaten zijn nodig voor het bepalen van de coordinaten van
    het tKinter tablat.

    De functie updatecars vraagt om één argument: een lijst die de locatie
    van alle auto's bevat.

    De functie wordt aangeroepen door begin. Hierna returned het een dictionary
    waarin alle coordinaten van de auto's staan. Deze dictionary wordt hierna
    gebruikt door de draw functie.
    """
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


def draw(cars, canvas, size, exp, rest):
    """
    De wraw functie zet de coordinaten van de auto's om in coordinaten op het
    tKinter tablat. Hierbij wordt eerst een lege grid gevisualiseerd, waarnaar
    elke auto zijn plek op het boord krijgt.

    De functie draw vraag om vijf argumenten:
        1) De locatie van alle auto's
        2) Een canvas om op te visualiseren
        3) De groote van het boord
        4) De expansie van de vierkantjes (afhankelijk van de size)
        5) Een int die bepaald hoe snel de grids achter elkaar gespeeld worden.

    De draw functie maakt vierkante witte vlakken op het canvas. Dit zijn
    de lege vakjes. Daarna wordt de dictionary gebruikt om elke auto op de
    goede locatie te tekenen.
    """
    colours = ["#D2691E", "#FF7F50", "#696969", "#DAA520", "#008000",
               "#4B0082", "#800080", "#008080", "#0033cc", "#ff33cc"]

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
    # De sleep functie is ervoor dat de grids niet te snel achter elkaar worden
    # afgespeeld.
    time.sleep(rest)
    canvas.delete("all")
