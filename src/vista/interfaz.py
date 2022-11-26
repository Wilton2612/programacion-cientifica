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
    root.title("Modelo Pc")
    root.resizable(1,1)
    center(root,1000, 600)
    return root

root = crearVentana()
 
"""Creación de Frames"""

"""Frame 0,0"""
frame1 = tk.Frame(root)
frame1.grid(pady=5, row=0, column=0)
#frame1.config(bg="red")
frame1.config(width="500",height="300")
tk.Label(frame1, text ="Modelo").place(x=0,y=0)

"""Gráfica"""
fig = plt.Figure(figsize=(4, 2), dpi=100)
t = np.arange(0,10, 0.01)
fig.add_subplot(111).plot(t, np.tan(t))     # subplot(filas, columnas, item)
plt.close()

plt.style.use('seaborn-darkgrid')
cvs = FigureCanvasTkAgg(fig, master=frame1)
cvs.draw()
barra_navegacion = NavigationToolbar2Tk(cvs, frame1)
barra_navegacion.update()
cvs.get_tk_widget().pack(padx=0, pady=0, expand=True)



"""Frame 0,1"""
frame2 = tk.Frame(root)
frame2.grid(pady=5, row=0, column=1)
#frame2.config(bg="yellow")
frame2.config(width="500",height="300")
tk.Label(frame2, text ="Imagen").place(x=0,y=0)
modelo = tk.PhotoImage(file="modelo.png")
tk.Label(frame2, image =modelo).grid(row=0,column=0)
buttonClose = tk.Button(frame2,text = "Quit",font=("bold"), 
                   command = close_window, background="red")
buttonClose.grid(row=0,column=1)

"""Frame 1,0"""
frame3 = tk.Frame(root)
frame3.grid(pady=5, row=1, column=0, columnspan=2)
#frame3.config(bg="purple")
frame3.config(width="1000",height="300",relief="groove",bd=10)
tk.Label(frame3, text ="Opciones Modelo").place(x=0,y=0)

"""
Sub Frame Metodos, Variables y Parametros
"""
frame31 = tk.Frame(master=frame3)
frame31.place(x=0,y=20)
#frame31.config(bg="green")
frame31.config(width="500",height="300")
tk.Label(frame31, text ="Metodo de Solución:",font=(18)).grid(pady=25, padx=10, row=0, column=0)

#Checkbuttons
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

c1 = tk.Checkbutton(frame31, text='Ruggen-Kutta 2',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.grid(pady=5,padx=20, row=1, column=0,sticky="w")
c2 = tk.Checkbutton(frame31, text='Ruggen-Kutta 4',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.grid(pady=5, padx=20, row=2, column=0,sticky="w")
c3 = tk.Checkbutton(frame31, text='Euler Adelante',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.grid(pady=5, padx=20, row=3, column=0,sticky="w")
c4 = tk.Checkbutton(frame31, text='Euler Modificado',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.grid(pady=5, padx=20, row=4, column=0,sticky="w")
c5 = tk.Checkbutton(frame31, text='Euler Atras',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.grid(pady=5, padx=20, row=5, column=0,sticky="w")

"""Variables"""
tk.Label(frame31, text ="Variables",font=(18)).grid(pady=5,padx=0, row=0, column=3,columnspan=2)

#Checkbuttons
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()

c6 = tk.Checkbutton(frame31, text='V(t)',variable=var6, onvalue=1, offvalue=0, command=print_selection)
c6.grid(pady=5, padx=0, row=1, column=1,sticky="e",columnspan=2)
c7 = tk.Checkbutton(frame31, text='Gk(t)',variable=var7, onvalue=1, offvalue=0, command=print_selection)
c7.grid(pady=5, padx=0,row=1, column=3, columnspan=2)
c8 = tk.Checkbutton(frame31, text='GNa(t)',variable=var8, onvalue=1, offvalue=0, command=print_selection)
c8.grid(pady=5, padx=0,row=1, column=5)

"""Parámetros"""

#Entrys
cuadro1 = tk.Entry(frame31,width=8)
cuadro2 = tk.Entry(frame31,width=8)
cuadro3 = tk.Entry(frame31,width=8)
cuadro4 = tk.Entry(frame31,width=8)
cuadro5 = tk.Entry(frame31,width=8)

tk.Label(frame31, text ="Parámetros",font=(18)).grid(pady=15,padx=0, row=2, column=3,columnspan=2)

tk.Label(frame31, text ="EK",font=(18)).grid(pady=5,padx=0, row=3, column=1)
cuadro1.grid(pady=5,padx=0, row=3, column=2)
tk.Label(frame31, text ="mV",font=(18)).grid(pady=5,padx=0, row=3, column=3)

tk.Label(frame31, text ="ENa",font=(18)).grid(pady=5,padx=0, row=4, column=1)
cuadro2.grid(pady=5,padx=0, row=4, column=2)
tk.Label(frame31, text ="mV",font=(18)).grid(pady=5,padx=0, row=4, column=3)

tk.Label(frame31, text ="El",font=(18)).grid(pady=5,padx=0, row=5, column=1)
cuadro3.grid(pady=5,padx=0, row=5, column=2)
tk.Label(frame31, text ="mv",font=(18)).grid(pady=5,padx=0, row=5, column=3)

tk.Label(frame31, text ="Gk",font=(18)).grid(pady=5,padx=0, row=3, column=4)
cuadro4.grid(pady=5,padx=0, row=3, column=5)
tk.Label(frame31, text ="mS/cm3",font=(18)).grid(pady=5,padx=0, row=3, column=6)

tk.Label(frame31, text ="GNa",font=(18)).grid(pady=5,padx=0, row=4, column=4)
cuadro5.grid(pady=5,padx=0, row=4, column=5)
tk.Label(frame31, text ="mS/cm3",font=(18)).grid(pady=5,padx=0, row=4, column=6)



"""
Frame Tiempos y Botones

"""
frame32 = tk.Frame(master=frame3)
frame32.place(x=500,y=20)
#frame32.config(bg="orange")
frame32.config(width="500",height="300")

frame321 = tk.Frame(master=frame32)
frame321.place(x=0,y=0)
#frame321.config(bg="pink")
frame321.config(width="500",height="125")

frame322 = tk.Frame(master=frame32)
frame322.place(x=130,y=160)
#frame322.config(bg="brown")
frame322.config(width="400",height="135")


#Entrys
cuadro6 = tk.Entry(frame321,width=8)
cuadro7 = tk.Entry(frame321,width=8)
cuadro8 = tk.Entry(frame321,width=8)
cuadro9 = tk.Entry(frame321,width=8)

#Buttons
button1 = tk.Button(frame321, text="Cargar")
button2 = tk.Button(frame321, text="Simular", font=18)
button3 = tk.Button(frame321, text="Importar", font=18)
button4 = tk.Button(frame321, text="Exportar", font=18)


tk.Label(frame321, text ="Tiempo de Simulación:",font=(18)).grid(pady=0,padx=0, row=0, column=0,sticky="w")
cuadro6.grid(pady=0,padx=0, row=0, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=0, column=2)

tk.Label(frame321, text ="Tiempo de Inicio de Estimulación",font=(18)).grid(pady=0,padx=0, row=1, column=0,sticky="w")
cuadro7.grid(pady=0,padx=0, row=1, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=1, column=2)

tk.Label(frame321, text ="Tiempo de fin de Estimulación",font=(18)).grid(pady=0,padx=0, row=2, column=0,sticky="w")
cuadro8.grid(pady=0,padx=0, row=2, column=1)
tk.Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=2, column=2)

tk.Label(frame321, text ="Valor de Estimulación",font=(18)).grid(pady=0,padx=0, row=3, column=0,sticky="w")
cuadro9.grid(pady=0,padx=0, row=3, column=1)
tk.Label(frame321, text ="ma",font=(18)).grid(pady=0,padx=0, row=3, column=2)

button1.grid(pady=0,padx=0, row=4, column=0,sticky="e")
button2.grid(pady=0,padx=60, row=0, column=3,sticky="e")
button3.grid(pady=2,padx=40, row=2, column=3,sticky="e")
button4.grid(pady=2,padx=40, row=3, column=3,sticky="e")

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

root.mainloop()









"""
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.animation as animation
from matplotlib import style

import numpy as np

from PIL import ImageTk ,Image

import os
import sys
sys.path.insert(1, os.getcwd())

class Principal:


    def __init__(self):
        self.window = tk.Tk()
                
        self.window.title('Diferentes funciones - Programación Científica')
        self.center(1100, 700)
       # self.window.geometry('1000x700')
        self.window.config(bg='#69DADB')
        self.window.resizable(1,1)

        self.window.columnconfigure(0, weight=2)

       
          
        #Sección de la gráfica e imagen
        self.panel  = tk.Frame(self.window, borderwidth=1, relief="solid", height=400, width=1100)
        self.panel.grid(row=0, column=0, pady=10)
        



        #Gráfica
        fig = plt.Figure(figsize=(4, 2), dpi=100)
        t = np.arange(0,10, 0.01)
        fig.add_subplot(111).plot(t, np.tan(t))     # subplot(filas, columnas, item)
       
        #fig.suptitle(opcion.get())

        plt.close()
        plt.style.use('seaborn-darkgrid')
        self.cvs = FigureCanvasTkAgg(fig, master=self.panel)
        self.cvs.draw()
        barra_navegacion = NavigationToolbar2Tk(self.cvs, self.panel)
        barra_navegacion.update()
        self.cvs.get_tk_widget().pack(padx=80, pady=70, expand=True)
            



        #Sección variables 
        self.botones = tk.Frame(self.window, borderwidth=1, relief="solid",height=320, width=1100)
        #,height=100, width=500
        self.botones.grid(row=1, column=0, pady=20)

        self.window.mainloop()

    def grafica():
        fig = plt.Figure(figsize=(4, 2), dpi=100)
        t = np.arange(0,10, 0.01)
        fig.add_subplot(111).plot(t, fun(t))     # subplot(filas, columnas, item)
        fig.suptitle(opcion.get())

        plt.close()
        plt.style.use('seaborn-darkgrid')
        Plot = FigureCanvasTkAgg(fig, master=self.panel)
        Plot.draw()

        toolbar = NavigationToolbar2Tk(Plot, window)
        toolbar.update()
        Plot.get_tk_widget().place(x=350,y=50)





    def center(self, ancho, alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_pantalla = self.window.winfo_screenwidth()
        alto_pantalla = self.window.winfo_screenheight()
        x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
        y_cor = int((alto_pantalla/2)-(alto_ven/2))
        self.window.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))

if __name__  == '__main__':
    Principal()


        
      """