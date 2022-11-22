
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
import sys
sys.path.insert(1, os.getcwd())

class Principal:


    def __init__(self):
        self.window = tk.Tk()
                
        self.window.title("Sistema de inventarios")
        self.center(1100, 700)
       # self.window.geometry('1000x700')
        self.window.config(bg='#69DADB')
        self.window.resizable(1,1)

        self.window.columnconfigure(0, weight=2)


        """ Sección de la gráfica e imagen"""
        self.panel  = tk.Frame(self.window, borderwidth=1, relief="solid", height=400, width=1100)
        self.panel.grid(row=0, column=0, pady=10)
        



        """Gráfica"""
        fig = plt.Figure(figsize=(4, 2), dpi=100)
        t = np.arange(0,10, 0.01)
        fig.add_subplot(111).plot(t, np.sin(t))     # subplot(filas, columnas, item)
       
        #fig.suptitle(opcion.get())

        #plt.close()
        #plt.style.use('seaborn-darkgrid')
        self.cvs = FigureCanvasTkAgg(fig, master=self.panel)
        self.cvs.draw()
        barra_navegacion = NavigationToolbar2Tk(self.cvs, self.panel)
        barra_navegacion.update()
        self.cvs.get_tk_widget().pack(padx=80, pady=70, expand=True)
        
    



        """ Sección variables """
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

        #toolbar = NavigationToolbar2Tk(Plot, window)
        #toolbar.update()
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