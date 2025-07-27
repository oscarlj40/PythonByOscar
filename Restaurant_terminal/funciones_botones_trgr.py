from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def total(texto_comida, texto_bebida, texto_postres, var_costo_comida, var_costo_bebida, var_costo_postres, var_subtotal, var_impuestos, var_total):
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo(texto_recibo, texto_comida, lista_comida, texto_bebida, lista_bebida, texto_postres, lista_postres, var_costo_comida, var_costo_bebida, var_costo_postres, var_subtotal, var_impuestos, var_total):
    texto_recibo.delete(1.0, END)
    num_recibo = f'N#  -  {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = fecha.strftime('%d/%m/%Y - %H:%M')
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END, '\n' + f'*' * 55 + '\n')
    texto_recibo.insert(END, '\nItems\t\tCant.\t\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 55 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comida[x]}\t\t{comida.get()}\t\t'
                                     f'$ {round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebida[x]}\t\t{bebida.get()}\t\t'
                                     f'$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t\t'
                                     f'$ {round(int(postres.get()) * precios_postres[x], 2)}\n')
        x += 1
    texto_recibo.insert(END, f'-' * 55 + '\n')
    texto_recibo.insert(END, f' Costo de la Comidas: \t\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebidas: \t\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 55 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impiestos: \t\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 55 + '\n')
    texto_recibo.insert(END, f'Lo esperamos pronto')





def guardar(texto_recibo):
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode= "w", defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo a sido guardado')


def resetear(texto_recibo, cuadro_comida, cuadro_bebida, cuadro_postres, variable_comida, variable_bebida, variable_postres, texto_comida, texto_bebida, texto_postres, var_costo_comida, var_costo_bebida, var_costo_postres, var_subtotal, var_impuestos, var_total):

    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postres:
        v.set(0)


    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')



