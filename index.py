#create the pong game
#use tkinter
#use the turtle module

import turtle
import os
import tkinter as tk
import random



wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("gray")
wn.setup(width=800, height=600)
wn.tracer(0)


#score
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#Linea Division
division = turtle.Turtle()
division.color("Black")
division.goto(0, 400)
division.goto(0, -400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("paddle_a: 0      paddle_b: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    

def ajustar_velocidad():
    nueva_velocidad = int(velocidad_entry.get())
    ball.vel_x = nueva_velocidad
    ball.vel_y = nueva_velocidad

# Función para mostrar información del juego
def mostrar_informacion():
    informacion = "Juego de Ping Pong\n" \
                "Velocidad de la bola: {}\n" \
                "Presiona 'P' para pausar/reanudar el juego\n"\
                "Este juego ha sido desarrollado en python con casi 200 líneas de código, los colores, sonidos de los personajes se irán añadiendo con el paso del tiempo"
    info_label.configure(text=informacion)

# Función para detener/reanudar el juego
def detener_reanudar_juego():
    global pausa
    pausa = not pausa

# Función para actualizar la posición de la bola y dibujar en el lienzo
def actualizar_lienzo():
    if not pausa:
        canvas.delete("all")
        ball.mover()
        canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                ball.x + ball.radius, ball.y + ball.radius)
                
    ventana.after(16, actualizar_lienzo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Ping Pong")

# Crear el lienzo
canvas = tk.Canvas(ventana, width=72, height=150)
canvas.pack()


# Variables para pausa
pausa = False

# Crear el menú
menu_frame = tk.Frame(ventana)
menu_frame.pack()

velocidad_label = tk.Label(menu_frame, text="Velocidad de la bola:")
velocidad_label.grid(row=0, column=0)

velocidad_entry = tk.Entry(menu_frame)
velocidad_entry.grid(row=0, column=1)

ajustar_velocidad_btn = tk.Button(menu_frame, text="Ajustar velocidad", command=ajustar_velocidad)
ajustar_velocidad_btn.grid(row=1, column=0, columnspan=2)

info_label = tk.Label(menu_frame, text="")
info_label.grid(row=2, column=0, columnspan=2)

mostrar_info_btn = tk.Button(menu_frame, text="Mostrar información", command=mostrar_informacion)
mostrar_info_btn.grid(row=3, column=0, columnspan=2)

detener_reanudar_btn = tk.Button(menu_frame, text="Detener/Reanudar juego", command=detener_reanudar_juego)
detener_reanudar_btn.grid(row=4, column=0, columnspan=4)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down,"Down")

# Main Gme loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("paddle_a: {}      paddle_b: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("paddle_a: {}     paddle_b: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
    
    if ((ball.xcor() > 340 and ball.xcor() < 350)
        and (ball.ycor() < paddle_a.ycor() +50
            and ball.ycor() > paddle_b.ycor() -50)):
        ball.dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > -350)
        and (ball.ycor() < paddle_a.ycor() + 50
            and ball.ycor() > paddle_b.ycor() -50)):
        ball.dx *= -1


#---------------------------------------------------------------------#

