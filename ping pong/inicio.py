import tkinter
import tkinter as tk
import subprocess

#------------------Ventana------------------#

ventana = tkinter.Tk()
ventana.title("Ping Pong")
ventana.geometry("500x500")

#------------------Botón-----------------#

def jugar():
    subprocess.Popen(["python", './index.py'])
boton = tk.Button(ventana, text = "Jugar", command=jugar)
boton.pack()
boton.place(x= 300, y= 100, width=150, height=75)

def info():
    subprocess.Popen(["python", './opciones.py'])
boton = tk.Button(ventana, text = "Opciones", command=info)
boton.pack()
boton.place(x= 100, y=100, width=150, height=75)


ventana.mainloop()