from tkinter import *

## Размеры холста:
W = 600  # ширина
H = 500  # высота

## Диаметр мячика:
D = 10

## Начальное положение мячика:
X_START = W / 2
Y_START = H / 2

## Ширина и высота ракеток:
RACKET_W = 10
RACKET_H = 100

## Скорость перемещения ракеток:
RACKET_SPEED = 10

## Скорость перемещения мячика:
dx = 2
dy = 2

## Через какое время будет происходить премещение мячика (в мс):
MS = 10

Win = Tk()
c = Canvas(Win, width=W, height=H, bg='black')
c.pack()

## Отрисовка поля:
a = 30
b=130
c.create_rectangle(a, b, W - a, H - a, outline='white')
c.create_line(W / 2, b, W / 2, H - a, fill='white', width=8, dash=(100, 10))
left_score=0
right_score=0
ls = Label(text=left_score, bg='black', fg='white', font=("Calibri", 64))
ls.place(x=W / 2-80, y=20)
rs = Label(text=right_score, bg='black', fg='white', font=("Calibri", 64))
rs.place(x=W / 2+30, y=20)

## Ракетки и мячик:
ball = c.create_rectangle(X_START - D / 2, Y_START - D / 2, X_START + D / 2, Y_START + D / 2, fill='red')
left_racket = c.create_rectangle(50, 150, 50 + RACKET_W, 150 + RACKET_H, fill='white')
right_racket = c.create_rectangle(W - 50, 150, W - 50 - RACKET_W, 150 + RACKET_H, fill='white')


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


## Перемещение мячика в поле:

def motion():
    global dx, dy, left_score, right_score
    ## Отскок от ракеток:
    is_inside_left_x = c.coords(ball)[0] < c.coords(left_racket)[2] and c.coords(ball)[2] > c.coords(left_racket)[0]
    is_inside_left_y = c.coords(ball)[3] > c.coords(left_racket)[1] and c.coords(ball)[1] < c.coords(left_racket)[3]
    if is_inside_left_x and is_inside_left_y:
        dx = -dx
    is_inside_right_x = c.coords(ball)[2] > c.coords(right_racket)[0] and c.coords(ball)[0] < c.coords(right_racket)[2]
    is_inside_right_y = c.coords(ball)[3] > c.coords(right_racket)[1] and c.coords(ball)[1] < c.coords(right_racket)[3]
    if is_inside_right_x and is_inside_right_y:
        dx = -dx

    ## Возврат в центр:
    if c.coords(ball)[0] < a :
        c.coords(ball, X_START - D / 2, Y_START - D / 2, X_START + D / 2, Y_START + D / 2)
        right_score+=1
        rs.config(text=right_score)
    elif c.coords(ball)[2] > W - a:
        c.coords(ball, X_START - D / 2, Y_START - D / 2, X_START + D / 2, Y_START + D / 2)
        left_score+=1
        ls.config(text=left_score) 

    ## Отскок от верхней и нижней границ поля:
    if c.coords(ball)[1] < b or c.coords(ball)[3] > H - a:
        dy = -dy

    c.move(ball, dx, dy)
    Win.after(MS, motion)


## Обработка нажатий клавиш:
Win.bind('w', move_up_left_racket)
Win.bind('s', move_down_left_racket)
Win.bind('<Up>', move_up_right_racket)
Win.bind('<Down>', move_down_right_racket)

motion()

Win.mainloop()
