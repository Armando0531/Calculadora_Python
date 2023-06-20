'''
Created on 20 jun 2023

@author: arman
'''
from tkinter import *
import math

ventana = Tk()
ventana.title("Calculadora")

i = 0

# Entrada
pantalla = Entry(ventana, font=("Calibri 20"))
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Funciones
def click_boton(valor):
    global i
    pantalla.insert(i, valor)
    i += 1

def borrar():
    pantalla.delete(0, END)
    i = 0

def borrar_ultimo():
    texto_actual = pantalla.get()
    nuevo_texto = texto_actual[:-1]
    pantalla.delete(0, END)
    pantalla.insert(0, nuevo_texto)

def hacer_operacion():
    ecuacion = pantalla.get()
    resultado = eval(ecuacion)
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)
    i = 0

def calcular_raiz_cuadrada():
    numero = float(pantalla.get())
    resultado = math.sqrt(numero)
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)

def calcular_cuadrado():
    numero = float(pantalla.get())
    resultado = numero ** 2
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)

def calcular_fraccion():
    numero = float(pantalla.get())
    if numero != 0:
        resultado = 1 / numero
        pantalla.delete(0, END)
        pantalla.insert(0, resultado)
    else:
        pantalla.delete(0, END)
        pantalla.insert(0, "Error")

def agregar_porcentaje():
    ecuacion = pantalla.get()
    try:
        resultado = eval(ecuacion) / 100
        pantalla.delete(0, END)
        pantalla.insert(END, str(resultado))
    except:
        pantalla.delete(0, END)
        pantalla.insert(END, "Error")

# Botones
boton_porcentaje = Button(ventana, text="%", width=5, height=2, command=lambda: agregar_porcentaje())
boton_raiz_cuadrada = Button(ventana, text="√", width=5, height=2, command=lambda: calcular_raiz_cuadrada())
boton_cuadrado = Button(ventana, text="x²", width=5, height=2, command=lambda: calcular_cuadrado())
boton_fraccion = Button(ventana, text="1/x", width=5, height=2, command=lambda: calcular_fraccion())

boton_CE = Button(ventana, text="CE", width=5, height=2, command=lambda: borrar())
boton_C = Button(ventana, text="C", width=5, height=2, command=lambda: borrar())
boton_borrar_ultimo = Button(ventana, text="←", width=5, height=2, command=lambda: borrar_ultimo())
boton_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"))
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"))
boton_sum = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
boton_rest = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: hacer_operacion())

boton_1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
boton_2 = Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2))
boton_3 = Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3))
boton_4 = Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4))
boton_5 = Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5))
boton_6 = Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6))
boton_7 = Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7))
boton_8 = Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8))
boton_9 = Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9))
boton_0 = Button(ventana, text="0", width=13, height=2, command=lambda: click_boton(0))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))

# Colocar botones en la ventana
boton_porcentaje.grid(row=1, column=0, padx=5, pady=5)
boton_raiz_cuadrada.grid(row=1, column=1, padx=5, pady=5)
boton_cuadrado.grid(row=1, column=2, padx=5, pady=5)
boton_fraccion.grid(row=1, column=3, padx=5, pady=5)

boton_CE.grid(row=2, column=0, padx=5, pady=5)
boton_C.grid(row=2, column=1, padx=5, pady=5)
boton_borrar_ultimo.grid(row=2, column=2, padx=5, pady=5)
boton_div.grid(row=2, column=3, padx=5, pady=5)

boton_7.grid(row=3, column=0, padx=5, pady=5)
boton_8.grid(row=3, column=1, padx=5, pady=5)
boton_9.grid(row=3, column=2, padx=5, pady=5)
boton_mult.grid(row=3, column=3, padx=5, pady=5)

boton_4.grid(row=4, column=0, padx=5, pady=5)
boton_5.grid(row=4, column=1, padx=5, pady=5)
boton_6.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton_1.grid(row=5, column=0, padx=5, pady=5)
boton_2.grid(row=5, column=1, padx=5, pady=5)
boton_3.grid(row=5, column=2, padx=5, pady=5)
boton_sum.grid(row=5, column=3, padx=5, pady=5)

boton_0.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=6, column=2, padx=5, pady=5)
boton_igual.grid(row=6, column=3, padx=5, pady=5)

ventana.mainloop()







