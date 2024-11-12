import tkinter as tk
from tkinter import *
import pygame.mixer as mx
from tkinter import filedialog
from Tooltip import Tooltip

class Reproductor():

    
    def __init__(self):
        mx.init()
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Musica")
        self.ventana.config(width=700, height=600)
        self.ventana.config(bg="#FFFFFF")
        self.ventana.resizable(0,0)

        # Variables de control
        self.listaCanciones=[]#lista de canciones
        self.cancionActual=None

        #frame
        self.frameBorde = tk.Frame(self.ventana, bd=5, relief="ridge", bg="black")
        self.frameBorde.place(relx=0.15, rely=0.15, width=500, height=240)
        self.frame = tk.Frame(self.frameBorde, bg="#FFFFFF")
        self.frame.place(width=490, height=230)

        #Iconos 
        self.play = tk.PhotoImage(file=r"Reproductor/iconos/play.png")
        self.pause = tk.PhotoImage(file=r"Reproductor/iconos/pause.png")
        self.skip2 = tk.PhotoImage(file=r"Reproductor/iconos/play-skip2.png")
        self.skip = tk.PhotoImage(file=r"Reproductor/iconos/play-skip.png")
        self.back = tk.PhotoImage(file=r"Reproductor/iconos/back.png")
        self.back2 = tk.PhotoImage(file=r"Reproductor/iconos/back2.png")
        self.menu = tk.PhotoImage(file=r"Reproductor/iconos/menu.png")

         #Botones
        self.btnPlay = tk.Button(self.ventana, image=self.play)
        self.btnPlay.place(relx=0.5, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnPlay,"Presione para iniciar la cancion")

        self.btnSkip = tk.Button(self.ventana, image=self.skip)
        self.btnSkip.place(relx=0.60, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnSkip,"Presione para cambiar de cancion")

        self.btnSkip2 = tk.Button(self.ventana, image=self.skip2)
        self.btnSkip2.place(relx=0.40, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnSkip2,"Presione para cambiar la cancion")

        self.btnBack2 = tk.Button(self.ventana, image=self.back2)
        self.btnBack2.place(relx=0.33, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnBack2,"Presione para regresar 10 segundos")

        self.btnBack = tk.Button(self.ventana, image=self.back)
        self.btnBack.place(relx=0.67, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnBack,"Presione para adelantar 10 segundos")

        self.btnMenu = tk.Button(self.ventana, image=self.menu, bg="#FFFFFF")
        self.btnMenu.place(relx=0.80, rely=0.56, width=42, height=25)
        Tooltip(self.btnMenu,"Presione para ver carpeta de canciones")

        # Barra de progreso 
        self.barra = tk.Canvas(self.ventana, width=509, height=10, bg="#555", bd=0, relief="flat")
        self.barra.place(relx=0.14, rely=0.67)
        self.barraprogreso = self.barra.create_rectangle(0, 0, 0, 10, fill="#1db954", outline="") 
        self.barraprogreso = self.barra.create_rectangle(0, 0, 0, 10, fill="#1db954", outline="")


        self.ventana.mainloop()
