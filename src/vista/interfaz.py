##
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.animation as animation
from matplotlib import style
from PIL import ImageTk ,Image
from funciones2 import elegir
from tkinter import *
import numpy as np
import scipy.optimize as opt

from PIL import ImageTk ,Image

import os
import sys



class Ventana:


    #Crear Ventana  
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modelo Hodgkin-Huxley")
        self.root.resizable(1,1)
        self.root.config(bg='#F3EFE0')
        self.center(1400, 770)
        self.root.columnconfigure(0, weight=2)
        #root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0,  weight=1)
        self.root.rowconfigure(1,  weight=4)
        self.root.rowconfigure(2,  weight=4)

        """Creación de Frames"""

        header = Frame(self.root,  width=1500,  height=30)
        header.grid(row=0, column=0, pady=0,padx=0)
        #header.config(relief="groove",bd=5)

        header.columnconfigure(0, weight=6)
        header.columnconfigure(1, weight=1)

        titulo = Label(header, text ="Modelo de Hodgkin y Huxley",fg='black',font='arial 20')
        titulo.grid(pady=0, padx=570, row=0, column=0)

        buttonClose = Button(header,borderwidth=1, relief="solid",text = "Quit",font='arial 10', command = self.close_window, background="gray")
        buttonClose.grid(padx=0, pady=0,row=0,column=1)



        """Frame que contiene la gráfica e imagen"""
        self.frame_arriba = LabelFrame(self.root, borderwidth=1, relief="solid",  width=1500, height=350)
        self.frame_arriba.grid(row=1, column=0, pady=0,padx=0)
        self.frame_arriba.config(relief="groove",bd=5)

        self.frame_arriba.columnconfigure(0, weight=4)
        self.frame_arriba.columnconfigure(1, weight=4)
        self.frame_arriba.columnconfigure(2, weight=1)

        """Frame 0,0"""
        self.frame1 = LabelFrame(self.frame_arriba, text='Gráfica')
        self.frame1.grid(pady=5,padx=0, row=0, column=0)
        #frame1.config(bg="red")
        self.frame1.config(width="750",height="350")



        """Gráfica"""
        self.fig = plt.Figure(figsize=(6.5, 3.2), dpi=100)
        self.t =  np.arange(0,10, 0.01)
        self.y = 2*self.t**2
        self.fig.add_subplot(111).plot(self.t,self.y )     # subplot(filas, columnas, item)
        plt.close()

        plt.style.use('seaborn-darkgrid')
        self.cvs = FigureCanvasTkAgg(self.fig, master=self.frame1)
        self.cvs.draw()
        self.barra_navegacion = NavigationToolbar2Tk(self.cvs, self.frame1)
        self.barra_navegacion.update()
        self.cvs.get_tk_widget().pack(padx=0, pady=5, expand=True)


        """Frame 0,1 - Imagen"""
        frame2 = LabelFrame(self.frame_arriba, text='Imagen')
        frame2.grid(padx=0, pady=5, row=0, column=1)
        #frame2.config(bg="yellow")
        frame2.config(width="750",height="350")
        modelo = PhotoImage(file="modelo.png")
        tk.Label(frame2, image =modelo).grid(padx=150, pady=60,row=0,column=0)



        """Frame que métodos de solución, variables, etc"""
        frame_abajo = LabelFrame(self.root, text ="Opciones Modelo",  font='arial 15', borderwidth=1, relief="solid",  width=1500, height=350)
        frame_abajo.grid( row=2, column=0, pady=0,padx=0)

        frame_abajo.config(relief="groove",bd=5)
        #tk.Label(frame_abajo, text ="Opciones Modelo").place(x=0,y=0)

        frame_abajo.columnconfigure(0, weight=2)
        frame_abajo.columnconfigure(1, weight=2)
        frame_abajo.columnconfigure(2, weight=2)

        """
        Sub Frame Metodos
        """

        frame31 = Frame(master=frame_abajo)
        frame31.grid( row=0, column=0, pady=0,padx=0)
        #frame31.config(bg="green")
        frame31.config(width="500",height="300")
        tk.Label(frame31, text ="Metodo de Solución:",font=(16)).grid(pady=25, padx=100, row=0, column=0)

        #Elección del método
        self.opcion = IntVar()

        c1 = tk.Radiobutton(frame31, text='Ruggen-Kutta 2', font='arial 14',value=1,variable=self.opcion)
        c1.grid(pady=5,padx=100, row=1, column=0,sticky="w")
        c2 = tk.Radiobutton(frame31, text='Ruggen-Kutta 4', font='arial 14',value=2,variable=self.opcion)
        c2.grid(pady=5, padx=100, row=2, column=0,sticky="w")
        c3 = tk.Radiobutton(frame31, text='Euler Adelante',font='arial 14',value=3, variable=self.opcion)
        c3.grid(pady=5, padx=100, row=3, column=0,sticky="w")
        c4 = tk.Radiobutton(frame31, text='Euler Modificado',font='arial 14',value=4,variable=self.opcion)
        c4.grid(pady=5, padx=100, row=4, column=0,sticky="w")
        c5 = tk.Radiobutton(frame31, text='Euler Atras', font='arial 14',value=5,variable=self.opcion)
        c5.grid(pady=5, padx=100, row=5, column=0,sticky="w")

        #print("selecciona euelr adelante: ", var3.get())

        """
        Variables y Parametros
        """
        frame32 = Frame(master=frame_abajo)
        frame32.grid( row=0, column=1, pady=0,padx=0)
        #frame31.config(bg="green")
        frame32.config(width="500",height="300")

        Label(frame32, text ="Variables",font=(18)).grid(pady=5,padx=0, row=0, column=3,columnspan=2)

        #Checkbuttons
        self.opcion_variable = IntVar() #V(t)
        #var7 = tk.BooleanVar() # dm= gk
        #var8 = tk.BooleanVar() # Gna = dn

        c6 = Radiobutton(frame32, text='V(t)',font='arial 11',value=1,variable=self.opcion_variable)
        c6.grid(pady=5, padx=0, row=1, column=1,sticky="e",columnspan=2)
        c7 = Radiobutton(frame32, text='Gk(t)',font='arial 11',value=2,variable=self.opcion_variable)
        c7.grid(pady=5, padx=0,row=1, column=3, columnspan=2)
        c8 = Radiobutton(frame32, text='GNa(t)',font='arial 11',value=3,variable=self.opcion_variable)
        c8.grid(pady=5, padx=0,row=1, column=5)


        """Parámetros"""

        #Entrys
        self.cuadro1 = Entry(frame32,width=8)
        self.cuadro2 = Entry(frame32,width=8)
        self.cuadro3 = Entry(frame32,width=8)
        self.cuadro4 = Entry(frame32,width=8)
        self.cuadro5 = Entry(frame32,width=8)

        Label(frame32, text ="Parámetros",font=(16)).grid(pady=15,padx=100, row=2, column=3,columnspan=2)

        Label(frame32, text ="EK",font=(16)).grid(pady=5,padx=0, row=3, column=1)
        self.cuadro1.grid(pady=5,padx=0, row=3, column=2)
        Label(frame32, text ="mV",font=(16)).grid(pady=5,padx=0, row=3, column=3)
        

        Label(frame32, text ="ENa",font=(16)).grid(pady=5,padx=0, row=4, column=1)
        self.cuadro2.grid(pady=5,padx=0, row=4, column=2)
        Label(frame32, text ="mV",font=(16)).grid(pady=5,padx=0, row=4, column=3)
        

        Label(frame32, text ="El",font=(16)).grid(pady=5,padx=0, row=5, column=1)
        self.cuadro3.grid(pady=5,padx=0, row=5, column=2)
        Label(frame32, text ="mv",font=(16)).grid(pady=5,padx=0, row=5, column=3)
        

        Label(frame32, text ="Gk",font=(16)).grid(pady=5,padx=0, row=3, column=4)
        self.cuadro4.grid(pady=5,padx=0, row=3, column=5)
        Label(frame32, text ="mS/cm3",font=(16)).grid(pady=5,padx=0, row=3, column=6)

        Label(frame32, text ="GNa",font=(16)).grid(pady=5,padx=0, row=4, column=4)
        self.cuadro5.grid(pady=5,padx=0, row=4, column=5)
        Label(frame32, text ="mS/cm3",font=(16)).grid(pady=5,padx=0, row=4, column=6)
    

        """
        Frame Tiempos y Botones
        """
        frame33 = Frame(master=frame_abajo )
        frame33.grid( row=0, column=2, pady=0,padx=0)
        #frame32.config(bg="orange")
        frame33.config(width="500",height="300")

        frame33.rowconfigure(0,  weight=4)
        frame33.rowconfigure(1,  weight=4)
        frame33.rowconfigure(2,  weight=1)

        frame321 = Frame(master=frame33 )
        frame321.grid( row=0, column=0, pady=5,padx=100)
        #frame321.config(bg="pink")
        frame321.config(width="500",height="100")

        #Entrys
        self.cuadro6 = Entry(frame321,width=8)
        self.cuadro7 = Entry(frame321,width=8)
        self.cuadro8 = Entry(frame321,width=8)
        self.cuadro9 = Entry(frame321,width=8)

        Label(frame321, text ="Tiempo de Simulación:",font='arial 12').grid(pady=0,padx=0, row=0, column=0,sticky="w")
        self.cuadro6.grid(pady=0,padx=0, row=0, column=1)
        Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=0, column=2)


        Label(frame321, text ="Tiempo de Inicio de Estimulación",font='arial 12').grid(pady=0,padx=0, row=1, column=0,sticky="w")
        self.cuadro7.grid(pady=0,padx=0, row=1, column=1)
        Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=1, column=2)
        self.ti = self.cuadro7.get()

        Label(frame321, text ="Tiempo de fin de Estimulación",font='arial 12').grid(pady=0,padx=0, row=2, column=0,sticky="w")
        self.cuadro8.grid(pady=0,padx=0, row=2, column=1)
        Label(frame321, text ="ms",font=(18)).grid(pady=0,padx=0, row=2, column=2)
        self.tf = self.cuadro8.get()

        Label(frame321, text ="Valor de Estimulación",font='arial 12').grid(pady=0,padx=0, row=3, column=0,sticky="w")
        self.cuadro9.grid(pady=0,padx=0, row=3, column=1)
        Label(frame321, text ="ma",font=(18)).grid(pady=0,padx=0, row=3, column=2)
        self.valor_estimulacion = self.cuadro9.get()


        #TABLA
        frame322 = Frame(master=frame33, borderwidth=1, relief="solid")
        frame322.grid( row=1, column=0, pady=5,padx=100)
        #frame322.config(bg="brown")
        frame322.config(width="500",height="100")

        Label(frame322, text ="T inicial (ms)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=0,sticky="w")
        Label(frame322, text ="T final (ms)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=1,sticky="w")
        Label(frame322, text ="Estimulación (mA)",highlightcolor="black",highlightbackground="black",highlightthickness=1).grid(pady=2,padx=0, row=0, column=2,sticky="w")

        Label(frame322, text ="0").grid(pady=2,padx=0, row=1, column=0,sticky="w")
        Label(frame322, text ="200").grid(pady=2,padx=0, row=1, column=1,sticky="w")
        Label(frame322, text ="0").grid(pady=2,padx=0, row=1, column=2,sticky="w")

        Label(frame322, text ="200").grid(pady=2,padx=0, row=2, column=0,sticky="w")
        Label(frame322, text ="300").grid(pady=2,padx=0, row=2, column=1,sticky="w")
        Label(frame322, text ="14").grid(pady=2,padx=0, row=2, column=2,sticky="w")

        Label(frame322, text ="300").grid(pady=2,padx=0, row=3, column=0,sticky="w")
        Label(frame322, text ="900").grid(pady=2,padx=0, row=3, column=1,sticky="w")
        Label(frame322, text ="0").grid(pady=2,padx=0, row=3, column=2,sticky="w")



        #BOTONES DE SIMULAR, CARGAR, IMPORTAR, EXPORTAR
        frame323 = Frame(master=frame33)
        frame323.grid( row=2, column=0, pady=5,padx=100)
        #frame322.config(bg="brown")
        frame323.config(width="500",height="100")


        frame323.columnconfigure(0,  weight=2)
        frame323.columnconfigure(1,  weight=2)
        frame323.columnconfigure(2,  weight=2)
        
        #Buttons
        button1 = Button(frame323, text="Cargar", font=7, bg='gray')
        button2 = Button(frame323, text="Simular", font=7, bg='gray', command=self.iniciar_simulacion)
        button3 = Button(frame323, text="Importar", font=7, bg='gray')
        button4 = Button(frame323, text="Exportar", font=7, bg='gray')

        button1.grid(pady=0,padx=0, row=0, column=0,sticky="e")
        button2.grid(pady=0,padx=0, row=0, column=1,sticky="e")
        button3.grid(pady=0,padx=0, row=0, column=2,sticky="e")
        button4.grid(pady=0,padx=0, row=0, column=3,sticky="e")
        self.root.mainloop()

    def graficar(self):
        
        metodo_eleccion = elegir(int(self.opcion.get()),[ float(self.cuadro7.get()), float(self.cuadro8.get()),float(self.cuadro1.get()), float(self.cuadro2.get()), float(self.cuadro3.get()), float(self.cuadro4.get()), float(self.cuadro5.get()),int(self.opcion_variable.get())]) 
        self.frame1 = LabelFrame(self.frame_arriba, text='Gráfica')
        self.frame1.grid(pady=5,padx=0, row=0, column=0)
        self.frame1.config(width="750",height="350")
        self.fig = plt.Figure(figsize=(6.5, 3.2), dpi=100)
        self.fig.add_subplot(111).plot(metodo_eleccion[1],metodo_eleccion[0] )     # subplot(filas, columnas, item)
        plt.close()

        plt.style.use('seaborn-darkgrid')
        self.cvs = FigureCanvasTkAgg(self.fig, master=self.frame1)
        self.cvs.draw()
        self.barra_navegacion = NavigationToolbar2Tk(self.cvs, self.frame1)
        self.barra_navegacion.update()
        self.cvs.get_tk_widget().pack(padx=0, pady=5, expand=True)

    def validar_entradas(self ):
        return self.opcion.get() !=0 and self.opcion_variable.get()!=0 and len(self.cuadro1.get())!=0 and len(self.cuadro2.get())!=0 and len(self.cuadro3.get())!=0 and len(self.cuadro4.get())!=0 and len(self.cuadro5.get())!=0 and len(self.cuadro6.get())!=0 and len(self.cuadro7.get())!=0 and len(self.cuadro8.get())!=0 and len(self.cuadro9.get())!=0 

    def iniciar_simulacion(self):
        if self.validar_entradas():
            self.graficar()
        else:
            messagebox.showerror(message="Escriba en todos los campos",title="Mensaje")

    def close_window(self):
        MsgBox = messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?',icon = 'warning')
        if MsgBox == 'yes':
            self.root.destroy()
        else:
            messagebox.showinfo('Retornar','Será retornado a la aplicación')
    
    ##Centrar
    def center(self,ancho,alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x_cor = int((ancho_pantalla/2)-(ancho_ven/2))
        y_cor = int((alto_pantalla/2)-(alto_ven/2))
        self.root.geometry("{}x{}+{}+{}".format(ancho_ven, alto_ven, x_cor, y_cor))



if __name__ == '__main__':
    Ventana()

# -77.0,  50.0,  -54.0,  36.0, 120.0, 6, 0.00, 500.00, 2