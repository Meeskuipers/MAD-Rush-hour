import tkinter as tk
import time

def draw(cars):
    window = tk.Tk()

    canvas = tk.Canvas(window, bg="black", height=2+(95*6),width=2+(95*6))
    canvas.pack()

    for i in range(6):
        for x in range(6):
            canvas.create_rectangle(5+(i*95),5+(x*95),95+(i*95),95+(x*95), outline="white", fill="white")

    for car in cars:
        canvas.create_rectangle(5+(int(car.position[0][1])*95),5+(int(car.position[0][0])*95),95+(int(car.position[-1][1])*95), 95+(int(car.position[-1][0])*95), outline=car.colour, fill=car.colour)

    canvas.mainloop()
