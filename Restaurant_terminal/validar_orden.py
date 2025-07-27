from tkinter import *

def revisar_check(cuadroscomida, variablescomida, texto_comida):
    x = 0
    for c in cuadroscomida:
        if variablescomida[x].get() == 1:
            cuadroscomida[x].config(state=NORMAL)
            if cuadroscomida[x].get() == '0':
                cuadroscomida[x].delete(0, END)
            cuadroscomida[x].focus()
        else:
            cuadroscomida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1