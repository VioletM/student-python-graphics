from tkinter import *

## Размеры холста:
W = 400  # ширина
H = 400  # высота

## Диаметр мячика:
D = 10

## Начальное положение мячика:
X_START = 650 / 2
Y_START = 500 / 2

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

##Функции отвечающая за меню
def menu():
    global pong_label,play_button,exit_button ,W,H
    c.delete("all")
    W = 400
    H = 400
    c.config(width=W, height=H)
    pong_label = Label(text="PONG", font="Arial 50", bg="black", fg="white")
    pong_label.place(x=W/2-100, y=50)
    play_button = Button(text="Play", font="Arial 30", bg="black", fg="white", width=4, height=1, command=START)
    play_button.place(x=W/2-50, y=150)
    exit_button = Button(text="Exit", font="Arial 30", bg="black", fg="white", width=4, height=1, command=EXIT)
    exit_button.place(x=W/2-50, y=250)
    c.create_rectangle(45,45,W-45,H-45, outline='white', width=8)
    
def START():
    global pong_label,play_button,exit_button 
    c.delete("all")
    pong_label.destroy()
    play_button.destroy()
    exit_button.destroy()
    game()
    
def EXIT():
    Win.destroy()
#Надпись победителю
def Winner():
    global ls, rs,W,H,left_score,right_score
    c.delete("all")
    ls.destroy()
    rs.destroy()
    if left_score>right_score:
        c.create_text(W/2, H/2, text="Победил первый игрок", fill='White', font=("Calibri", 40))
    else:
        c.create_text(W/2, H/2, text="Победил второй игрок", fill='White', font=("Calibri", 40))
    Win.after(3000, menu)

## Функции отвечающее за игровое поле
a = 30
b=130
def game():
    global left_racket,right_racket,ball,left_score,right_score,ls,rs,W,H
    W=650
    H=500
    c.config(width=W, height=H)
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
    
    ## Обработка нажатий клавиш:
    Win.bind('w', move_up_left_racket)
    Win.bind('s', move_down_left_racket)
    Win.bind('<Up>', move_up_right_racket)
    Win.bind('<Down>', move_down_right_racket)
    
    motion()
## Функции для движения ракеток:    
def move_up_left_racket(event):
    if c.coords(left_racket)[1] > b:
        c.move(left_racket, 0, -RACKET_SPEED)
            
def move_down_left_racket(event):
    if c.coords(left_racket)[3] < H - a:
        c.move(left_racket, 0, RACKET_SPEED)
            
def move_up_right_racket(event):
    if c.coords(right_racket)[1] > b:
        c.move(right_racket, 0, -RACKET_SPEED)


def move_down_right_racket(event):
    if c.coords(right_racket)[3] < H - a:
        c.move(right_racket, 0, RACKET_SPEED)


## Перемещение мячика в поле:
def motion():
    global dx, dy, left_score, right_score,ls,rs
    ## Отскок от ракеток:
    if c.coords(ball)[0] < c.coords(left_racket)[2] and c.coords(ball)[2] > c.coords(left_racket)[0] and c.coords(ball)[3] > c.coords(left_racket)[1] and c.coords(ball)[1] < c.coords(left_racket)[3]:
        dx = -dx
    if c.coords(ball)[2] > c.coords(right_racket)[0] and c.coords(ball)[0] < c.coords(right_racket)[2] and c.coords(ball)[3] > c.coords(right_racket)[1] and c.coords(ball)[1] < c.coords(right_racket)[3]:
        dx = -dx

    ## Возврат в центр:
    if c.coords(ball)[0] < a+5 :
        c.coords(ball, X_START - D / 2, Y_START - D / 2, X_START + D / 2, Y_START + D / 2)
        right_score+=1
        rs.config(text=right_score)
        if right_score==7:
            Winner()
    elif c.coords(ball)[2] > W - a-5:
        c.coords(ball, X_START - D / 2, Y_START - D / 2, X_START + D / 2, Y_START + D / 2)
        left_score+=1
        ls.config(text=left_score)
        if left_score==7:
            Winner()

    ## Отскок от верхней и нижней границ поля:
    if c.coords(ball)[1] < b or c.coords(ball)[3] > H - a:
        dy = -dy

    c.move(ball, dx, dy)
    Win.after(MS, motion)




menu()

Win.mainloop()