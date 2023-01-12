from tkinter import *
from config import *
from Ball import Ball


def start_animation():
    ball.fall(canvas)
    window.after(SPEED_BALL, start_animation)


window = Tk()
window.title('Сложная анимация')
window.resizable(False, False)
window.geometry(f'{WIDTH_WINDOW}x{HEIGHT_WINDOW}')

canvas = Canvas(window, height=HEIGHT_WINDOW, width=WIDTH_WINDOW, bg=FIELD_COLOR)
canvas.pack()

ball = Ball(canvas)

window.after(SPEED_BALL, start_animation)
window.mainloop()
