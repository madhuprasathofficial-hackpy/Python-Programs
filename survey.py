import tkinter as tk
import random

window = tk.Tk()

canvas = tk.Canvas(window, width=700, height=500, bg="darkgreen")
canvas.pack()

player = canvas.create_rectangle(320,220,380,280, fill="blue")

zombies = []

score = 0
