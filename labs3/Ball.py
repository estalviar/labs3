from config import *


class Ball:
    def __init__(self, canvas):
        self.x = WIDTH_WINDOW / 2
        self.y = HEIGHT_WINDOW / 2
        self.oval = canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE,
                           fill='#404040', outline='#ffffff')
        self.delta = (HEIGHT_WINDOW - HEIGHT_WINDOW / 2) / 200
        self.h = 30
        self.a = 0
        self.direction = 'down'
        self.f = 0

    def fall(self, canvas):
        if self.f == 1:
            self.a += self.delta
            self.y += self.a
            if self.y + SPACE_SIZE >= HEIGHT_WINDOW:
                self.y = HEIGHT_WINDOW - 30
        elif self.direction == 'down':
            self.a += self.delta
            self.y += self.a
        elif self.direction == 'up':
            self.a -= self.delta
            if self.a > 0:
                self.y -= self.a

        if self.y + SPACE_SIZE >= HEIGHT_WINDOW and self.direction != 'up':
            self.y = HEIGHT_WINDOW - 30
            self.direction = 'up'
        elif self.a <= 0 and self.direction != 'down':
            self.direction = 'down'
            self.h += 30
            self.a = 0
            p = (HEIGHT_WINDOW - HEIGHT_WINDOW / 2 + self.h)
            self.delta = p / 200
            if self.h >= HEIGHT_WINDOW - HEIGHT_WINDOW / 2:
                self.f = 1
        canvas.coords(self.oval, self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE)
