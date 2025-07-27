from tkinter import *

operador = ''

def click_boton(numero, visor_calculadora):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar(visor_calculadora):
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def resultado(visor_calculadora):
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ''



