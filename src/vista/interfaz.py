import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.animation as animation
from matplotlib import style
from PIL import ImageTk ,Image

import numpy as np

from PIL import ImageTk ,Image

import os
import sys

"""Metodos Ventana"""

##Centrar
def center(root,ancho,alto):
    alto_ven = alto
    ancho_ven = ancho
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
    y_cor = int((alto_pantalla/2)-(alto_ven/2))
    root.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))

#Seleccion Metodo
def print_selection():
    if (var1.get() == 1) :
        print("K2")
    elif (var2.get() == 1):
        print("K4")
    elif (var3.get() == 1):
        print("E")
    elif (var4.get() == 1) :
        print("EA")
    elif (var5.get() == 1):
        print("EM")
    elif (var6.get() == 1):
        print("V")
    elif (var7.get() == 1):
        print("G")
    elif (var8.get() == 1):
        print("GN")

#Cerrar Ventana
def close_window():
    MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Retornar','Será retornado a la aplicación')

#Crear Ventana
def crearVentana():
    root = tk.Tk()
    root.title("Modelo Hodgkin-Huxley")
    root.resizable(1,1)
    root.config(bg='#F3EFE0')
    center(root,1400, 770)
    root.columnconfigure(0, weight=2)
    #root.columnconfigure(1, weight=2)
    root.rowconfigure(0,  weight=1)
    root.rowconfigure(1,  weight=4)
    root.rowconfigure(2,  weight=4)
    return root

root = crearVentana()
 
"""Creación de Frames"""

header = tk.Frame(root,  width=1500,  height=30)
header.grid(row=0, column=0, pady=0,padx=0)
#header.config(relief="groove",bd=5)

header.columnconfigure(0, weight=6)
header.columnconfigure(1, weight=1)

titulo = tk.Label(header, text ="Modelo de Hodgkin y Huxley",fg='black',font='arial 20')
titulo.grid(pady=0, padx=570, row=0, column=0)

buttonClose = tk.Button(header,borderwidth=1, relief="solid",text = "Quit",font='arial 10', command = close_window, background="gray")
buttonClose.grid(padx=0, pady=0,row=0,column=1)



"""Frame que contiene la gráfica e imagen"""
frame_arriba = tk.LabelFrame(root, borderwidth=1, relief="solid",  width=1500, height=350)
frame_arriba.grid(row=1, column=0, pady=0,padx=0)
frame_arriba.config(relief="groove",bd=5)

frame_arriba.columnconfigure(0, weight=4)
frame_arriba.columnconfigure(1, weight=4)
frame_arriba.columnconfigure(2, weight=1)

"""Frame 0,0"""
frame1 = tk.LabelFrame(frame_arriba, text='Gráfica')
frame1.grid(pady=5,padx=0, row=0, column=0)
#frame1.config(bg="red")
frame1.config(width="750",height="350")



"""Gráfica"""
fig = plt.Figure(figsize=(6.5, 3.2), dpi=100)
t = np.arange(0,10, 0.01)
fig.add_subplot(111).plot(t, np.tan(t))     # subplot(filas, columnas, item)
plt.close()

plt.style.use('seaborn-darkgrid')
cvs = FigureCanvasTkAgg(fig, master=frame1)
cvs.draw()
barra_navegacion = NavigationToolbar2Tk(cvs, frame1)
barra_navegacion.update()
cvs.get_tk_widget().pack(padx=0, pady=5, expand=True)


"""Frame 0,1 - Imagen"""
frame2 = tk.LabelFrame(frame_arriba, text='Imagen')
frame2.grid(padx=0, pady=5, row=0, column=1)
#frame2.config(bg="yellow")
frame2.config(width="750",height="350")
modelo = tk.PhotoImage(file="modelo.png")
tk.Label(frame2, image =modelo).grid(padx=150, pady=60,row=0,column=0)



"""Frame que métodos de solución, variables, etc"""
frame_abajo = tk.LabelFrame(root, text ="Opciones Modelo",  font='arial 15', borderwidth=1, relief="solid",  width=1500, height=350)
frame_abajo.grid( row=2, column=0, pady=0,padx=0)

frame_abajo.config(relief="groove",bd=5)
#tk.Label(frame_abajo, text ="Opciones Modelo").place(x=0,y=0)

frame_abajo.columnconfigure(0, weight=2)
frame_abajo.columnconfigure(1, weight=2)
frame_abajo.columnconfigure(2, weight=2)

"""
Sub Frame Metodos
"""

frame31 = tk.Frame(master=frame_abajo)
frame31.grid( row=0, column=0, pady=0,padx=0)
#frame31.config(bg="green")
frame31.config(width="500",height="300")
tk.Label(frame31, text ="Metodo de Solución:",font=(16)).grid(pady=25, padx=100, row=0, column=0)

#Checkbuttons
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

c1 = tk.Checkbutton(frame31, text='Ruggen-Kutta 2', font='arial 14',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.grid(pady=5,padx=100, row=1, column=0,sticky="w")
c2 = tk.Checkbutton(frame31, text='Ruggen-Kutta 4', font='arial 14',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.grid(pady=5, padx=100, row=2, column=0,sticky="w")
c3 = tk.Checkbutton(frame31, text='Euler Adelante',font='arial 14',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.grid(pady=5, padx=100, row=3, column=0,sticky="w")
c4 = tk.Checkbutton(frame31, text='Euler Modificado',font='arial 14',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.grid(pady=5, padx=100, row=4, column=0,sticky="w")
c5 = tk.Checkbutton(frame31, text='Euler Atras', font='arial 14',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.grid(pady=5, padx=100, row=5, column=0,sticky="w")



"""
Variables y Parametros
"""
frame32 = tk.Frame(master=frame_abajo)
frame32.grid( row=0, column=1, pady=0,padx=0)
#frame31.config(bg="green")
frame32.config(width="500",height="300")

tk.Label(frame32, text ="Variables",font=(18)).grid(pady=5,padx=0, row=0, column=3,columnspan=2)

#Checkbuttons
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()

c6 = tk.Checkbutton(frame32, text='V(t)',font='arial 11',variable=var6, onvalue=1, offvalue=0, command=print_selection)
c6.grid(pady=5, padx=0, row=1, column=1,sticky="e",columnspan=2)
c7 = tk.Checkbutton(frame32, text='Gk(t)',font='arial 11',variable=var7, onvalue=1, offvalue=0, command=print_selection)
c7.grid(pady=5, padx=0,row=1, column=3, columnspan=2)
c8 = tk.Checkbutton(frame32, text='GNa(t)',font='arial 11',variable=var8, onvalue=1, offvalue=0, command=print_selection)
c8.grid(pady=5, padx=0,row=1, column=5)


"""Parámetros"""

#Entrys
cuadro1 = tk.Entry(frame32,width=8)
cuadro2 = tk.Entry(frame32,width=8)
cuadro3 = tk.Entry(frame32,width=8)
cuadro4 = tk.Entry(frame32,width=8)
cuadro5 = tk.Entry(frame32,width=8)

tk.Label(frame32, text ="Parámetros",font=(16)).grid(pady=15,padx=100, row=2, column=3,columnspan=2)

tk.Label(frame32, text ="EK",font=(16)).grid(pady=5,padx=0, row=3, column=1)
cuadro1.grid(pady=5,padx=0, row=3, column=2)
tk.Label(frame32, text ="mV",font=(16)).grid(pady=5,padx=0, row=3, column=3)

tk.Label(frame32, text ="ENa",font=(16)).grid(pady=5,padx=0, row=4, column=1)
cuadro2.grid(pady=5,padx=0, row=4, column=2)
tk.Label(frame32, text ="mV",font=(16)).grid(pady=5,padx=0, row=4, column=3)

tk.Label(frame32, text ="El",font=(16)).grid(pady=5,padx=0, row=5, column=1)
cuadro3.grid(pady=5,padx=0, row=5, column=2)
tk.Label(frame32, text ="mv",font=(16)).grid(pady=5,padx=0, row=5, column=3)

tk.Label(frame32, text ="Gk",font=(16)).grid(pady=5,padx=0, row=3, column=4)
cuadro4.grid(pady=5,padx=0, row=3, column=5)
tk.Label(frame32, text ="mS/cm3",font=(16)).grid(pady=5,padx=0, row=3, column=6)

tk.Label(frame32, text ="GNa",font=(16)).grid(pady=5,padx=0, row=4, column=4)
cuadro5.grid(pady=5,padx=0, row=4, column=5)
tk.Label(frame32, text ="mS/cm3",font=(16)).grid(pady=5,padx=0, row=4, column=6)




"""
Frame Tiempos y Botones
"""
frame33 = tk.Frame(master=frame_abajo )
frame33.grid( row=0, column=2, pady=0,padx=0)
#frame32.config(bg="orange")
frame33.config(width="500",height="300")

frame33.rowconfigure(0,  weight=4)
frame33.rowconfigure(1,  weight=4)
frame33.rowconfigure(2,  weight=1)

frame321 = tk.Frame(master=frame33 )
frame321.grid( row=0, column=0, pady=5,padx=100)
#frame321.config(bg="pink")
frame321.config(width="500",height="100")

#Entrys
cuadro6 = tk.Entry(frame321,width=8)
cuadro7 = tk.Entry(frame321,width=8)
cuadro8 = tk.Entry(frame321,width=8)
cuadro9 = tk.Entry(frame321,width=8)

tk.Label(frame321, text ="Tiempo de Simulación:",font='arial 12').grid(pady=0,padx=0, row=0, column=0,sticky="w")
cuadro6.grid(pady=0,padx=0, row=0, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=0, column=2)

tk.Label(frame321, text ="Tiempo de Inicio de Estimulación",font='arial 12').grid(pady=0,padx=0, row=1, column=0,sticky="w")
cuadro7.grid(pady=0,padx=0, row=1, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=1, column=2)

tk.Label(frame321, text ="Tiempo de fin de Estimulación",font='arial 12').grid(pady=0,padx=0, row=2, column=0,sticky="w")
cuadro8.grid(pady=0,padx=0, row=2, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=2, column=2)

tk.Label(frame321, text ="Valor de Estimulación",font='arial 12').grid(pady=0,padx=0, row=3, column=0,sticky="w")
cuadro9.grid(pady=0,padx=0, row=3, column=1)
tk.Label(frame321, text ="ma",font=(18)).grid(pady=0,padx=0, row=3, column=2)


#TABLA
frame322 = tk.Frame(master=frame33, borderwidth=1, relief="solid")
frame322.grid( row=1, column=0, pady=5,padx=100)
#frame322.config(bg="brown")
frame322.config(width="500",height="100")

tk.Label(frame322, text ="T inicial (ms)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=0,sticky="w")
tk.Label(frame322, text ="T final (ms)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=1,sticky="w")
tk.Label(frame322, text ="Estimulación (mA)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=2,sticky="w")

tk.Label(frame322, text ="0").grid(pady=2,padx=0, row=1, column=0,sticky="w")
tk.Label(frame322, text ="200").grid(pady=2,padx=0, row=1, column=1,sticky="w")
tk.Label(frame322, text ="0").grid(pady=2,padx=0, row=1, column=2,sticky="w")

tk.Label(frame322, text ="200").grid(pady=2,padx=0, row=2, column=0,sticky="w")
tk.Label(frame322, text ="300").grid(pady=2,padx=0, row=2, column=1,sticky="w")
tk.Label(frame322, text ="14").grid(pady=2,padx=0, row=2, column=2,sticky="w")

tk.Label(frame322, text ="300").grid(pady=2,padx=0, row=3, column=0,sticky="w")
tk.Label(frame322, text ="900").grid(pady=2,padx=0, row=3, column=1,sticky="w")
tk.Label(frame322, text ="0").grid(pady=2,padx=0, row=3, column=2,sticky="w")



#BOTONES DE SIMULAR, CARGAR, IMPORTAR, EXPORTAR
frame323 = tk.Frame(master=frame33)
frame323.grid( row=2, column=0, pady=5,padx=100)
#frame322.config(bg="brown")
frame323.config(width="500",height="100")


frame323.columnconfigure(0,  weight=2)
frame323.columnconfigure(1,  weight=2)
frame323.columnconfigure(2,  weight=2)


#Buttons
button1 = tk.Button(frame323, text="Cargar", font=7, bg='gray')
button2 = tk.Button(frame323, text="Simular", font=7, bg='gray')
button3 = tk.Button(frame323, text="Importar", font=7, bg='gray')
button4 = tk.Button(frame323, text="Exportar", font=7, bg='gray')

button1.grid(pady=0,padx=0, row=0, column=0,sticky="e")
button2.grid(pady=0,padx=0, row=0, column=1,sticky="e")
button3.grid(pady=0,padx=0, row=0, column=2,sticky="e")
button4.grid(pady=0,padx=0, row=0, column=3,sticky="e")


root.mainloop()
