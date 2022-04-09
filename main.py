import tkinter as tk
import time
from random import *
import keyboard

x = 20
y = 20
apl = 240
score = 0


def applecheck():
    global score
    if x == apl and y == apl:
        score += 1
        Score.config(text='Score: ' + str(score) + ' 000')

        applespawn()


def applespawn():
    global apl
    apl = randint(0, 45) * 10
    if (apl % 20) != 0:
        apl += 10
    canvas.coords(apple, apl, apl, apl + 20, apl + 20)
    if x == apl and y == apl:
        applespawn()


def bordercheck():
    global x, y
    if x <= 0:
        x = 480
    elif x >= 480:
        x = 0
    if y <= 0:
        y = 480
    elif y >= 480:
        y = 0


def keypressedd(event):
    global x
    x += 20
    canvas.coords(block, x, y, x-(score+1)*20, y+20)
    applecheck()
    bordercheck()


def keypresseda(event):
    bordercheck()
    global x
    x -= 20
    canvas.coords(block, x, y, x+(score+1)*20, y+20)
    applecheck()



def keypresseds(event):
    global y
    y += 20
    canvas.coords(block, x, y, x+20, y-(score+1)*20)
    applecheck()
    bordercheck()


def keypressedw(event):
    global y
    y -= 20
    canvas.coords(block, x, y, x+20, y+(score+1)*20)
    applecheck()
    bordercheck()


window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("500x530")
canvas = tk.Canvas()
Score = tk.Label(text='Score: ' + str(score), font="Arial 14")
Score.pack(side="bottom")
border = canvas.create_rectangle(2, 2, 497, 497, fill="gray22", outline="blue")
block = canvas.create_rectangle(x, y, x+20, y+20, fill="White", outline="Black")
apple = canvas.create_oval(apl, apl, apl + 20, apl + 20, fill="red", outline="black")
window.bind("d", keypressedd)
window.bind("a", keypresseda)
window.bind("s", keypresseds)
window.bind("w", keypressedw)
canvas.pack(fill="both", expand=1)
window.mainloop()