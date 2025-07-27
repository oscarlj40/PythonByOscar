from calculadora import *
from validar_orden import *
from funciones_botones_trgr import *


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# color de fondo de la ventana
aplicacion.configure(background='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Century Gothic', 58), bg='burlywood', width=20)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Century Gothic', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Century Gothic', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Century Gothic', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comida = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:

    # crear los check button
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(),
                         font=('Century Gothic', 16, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=lambda : revisar_check(cuadros_comida, variables_comida, texto_comida))
    comida.grid(row=contador,
                column=0,
                sticky=W,
                pady=6)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Century Gothic', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1,
                                  pady=6)

    contador += 1

# generar items bebida
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebidas in lista_bebidas:

    # crear los check button
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(),
                          font=('Century Gothic', 16, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_bebidas[contador],
                          command=lambda : revisar_check(cuadros_bebidas, variables_bebidas, texto_bebidas))
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W,
                 pady=6)

    # crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                     font=('Century Gothic', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                  column=1,
                                  pady=6)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:

    # crear los check button
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Century Gothic', 16, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=lambda : revisar_check(cuadros_postres, variables_postres, texto_postres))
    postres.grid(row=contador,
                 column=0,
                 sticky=W,
                 pady=6)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Century Gothic', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                  column=1,
                                   pady=6)

    contador += 1


# etiquetas de costos y campos de entrada
# variables
var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()
#comida
etiqueda_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueda_costo_comida.grid(row=0,
                           column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=50, pady=2)

# bebidas
etiqueda_costo_bebidas = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueda_costo_bebidas.grid(row=1, column=0)

texto_costo_bebidas = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row=1, column=1, pady=2)

# postres
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3)

# impuestos
etiqueta_impuesto = Label(panel_costos,
                              text='Impuesto',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3)

# total
etiqueda_total = Label(panel_costos,
                              text='Total',
                              font=('Century Gothic', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueda_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Century Gothic', 14, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, pady=2)


# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Century Gothic', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=10)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=lambda : total(texto_comida, texto_bebidas, texto_postres, var_costo_comida,
                                                 var_costo_bebidas, var_costo_postres, var_subtotal, var_impuesto,
                                                 var_total))

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Century Gothic', 12, 'bold'),
                    bd=1,
                    width=43,
                    height=15)
texto_recibo.grid(row=0,
                  column=0)

botones_creados[1].config(command=lambda : recibo(texto_recibo, texto_comida, lista_comida, texto_bebidas, lista_bebidas,
                                                  texto_postres, lista_postres, var_costo_comida, var_costo_bebidas,
                                                  var_costo_postres, var_subtotal, var_impuesto, var_total))
botones_creados[2].config(command=lambda : guardar(texto_recibo))
botones_creados[3].config(command=lambda : resetear(texto_recibo, cuadros_comida, cuadros_bebidas, cuadros_postres, variables_comida, variables_bebidas, variables_postres, texto_comida, texto_bebidas, texto_postres, var_costo_comida, var_costo_bebidas, var_costo_postres, var_subtotal, var_impuesto, var_total))

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Century Gothic', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', '=', 'CE', '0', '/']

botones_guardados = []

fila = 1
columnas = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton,
                   font=('Century Gothic', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columnas)

    if columnas == 3:
        fila += 1

    columnas += 1

    if columnas == 4:
        columnas = 0

botones_guardados[0].config(command=lambda : click_boton('7', visor_calculadora))
botones_guardados[1].config(command=lambda : click_boton('8', visor_calculadora))
botones_guardados[2].config(command=lambda : click_boton('9', visor_calculadora))
botones_guardados[3].config(command=lambda : click_boton('+', visor_calculadora))
botones_guardados[4].config(command=lambda : click_boton('4', visor_calculadora))
botones_guardados[5].config(command=lambda : click_boton('5', visor_calculadora))
botones_guardados[6].config(command=lambda : click_boton('6', visor_calculadora))
botones_guardados[7].config(command=lambda : click_boton('-', visor_calculadora))
botones_guardados[8].config(command=lambda : click_boton('1', visor_calculadora))
botones_guardados[9].config(command=lambda : click_boton('2', visor_calculadora))
botones_guardados[10].config(command=lambda : click_boton('3', visor_calculadora))
botones_guardados[11].config(command=lambda : click_boton('*', visor_calculadora))
botones_guardados[12].config(command=lambda : resultado(visor_calculadora))
botones_guardados[13].config(command=lambda : borrar(visor_calculadora))
botones_guardados[14].config(command=lambda : click_boton('0', visor_calculadora))
botones_guardados[15].config(command=lambda : click_boton('/', visor_calculadora))





# evitar que la pantalla se cierre
aplicacion.mainloop()
