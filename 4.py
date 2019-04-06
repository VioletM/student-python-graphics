from tkinter import *

## Размеры холста:
W = 600  # ширина
H = 400  # высота

## Диаметр мячика:
D = 10

## Начальное положение мячика:
X_START = 150
Y_START = 100

## Скорость перемещения ракеток:
RACKET_SPEED = 10

Win=Tk()
c = Canvas(Win, width=W, height=H, bg='black')
c.pack()

## Отрисовка поля:
a = 30
c.create_rectangle(a, a, W - a, H - a, outline='white')
c.create_line(W / 2, a, W / 2, H - a, fill='white', width=8, dash=(100, 10))

## Ракетки и мячик:
ball = c.create_rectangle(X_START, Y_START, X_START + D, Y_START + D, fill='red')
left_racket = c.create_line(50, 150, 50, 200, fill='white', width=10)
right_racket = c.create_line(W - 50, 150, W - 50, 200, fill='white', width=10)

## Функции для движения ракеток:
def move_up_left_racket(event):
    if c.coords(left_racket)[1] > a:
        c.move(left_racket, 0, -RACKET_SPEED)
    
def move_down_left_racket(event):
    if c.coords(left_racket)[3] < H - a:
        c.move(left_racket, 0, RACKET_SPEED)
    
def move_up_right_racket(event):
    if c.coords(right_racket)[1] > a:
        c.move(right_racket, 0, -RACKET_SPEED)
    
def move_down_right_racket(event):
    if c.coords(right_racket)[3] < H - a:
        c.move(right_racket, 0, RACKET_SPEED)
## Функции для движения мячика.
speed_x=5
speed_y=5
def motion_ball():
    global speed_x, speed_y
    if c.coords(ball)[0]<30 or c.coords(ball)[2]>570:
        speed_x=-speed_x
    elif c.coords(ball)[1]<30 or c.coords(ball)[3]>370:
        speed_y=-speed_y
    c.move(ball, speed_x, speed_y)
    Win.after(100, motion_ball)
## Обработка нажатий клавиш:
Win.bind('w', move_up_left_racket)
Win.bind('s', move_down_left_racket)
Win.bind('<Up>', move_up_right_racket)
Win.bind('<Down>', move_down_right_racket)
motion_ball()
Win.mainloop()