import tkinter as tk
from tkinter import *
import pygame.mixer as mx
from tkinter import filedialog
from Tooltip import Tooltip
from tkinter import messagebox

class Reproductor():

    def Abrirmenu(self, event):
        ventanaMenu = tk.Toplevel(self.ventana)
        ventanaMenu.title("Carpeta de Canciones")
        ventanaMenu.config(width=400, height=300)
        ventanaMenu.config(bg="black")

        self.listaCancionesBox = Listbox(ventanaMenu, bg="#FFFFFF", width=43, height=17)
        self.listaCancionesBox.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el Listbox en la ventana

    def moverVolumen(self, event):
        x = event.x
        if 20 <= x <= 184:
            self.Volumen.coords(self.volumenMarker, x - 5, 25 - 5, x + 5, 25 + 5)
            mx.music.set_volume(self.volumen)

    def mostrarAyuda(self, event):
        ayuda_texto = ("hola")
        messagebox.showinfo("Ayuda", ayuda_texto)

    def __init__(self):
        mx.init()
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Musica")
        self.ventana.config(width=700, height=600)
        self.ventana.config(bg="#FFFFFF")
        self.ventana.resizable(0,0)

        # Variables de control
        self.listaCanciones = []#lista de canciones
        self.cancionActual = None
        self.volumen = 0.5  # Volumen inicial

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
        self.mute = tk.PhotoImage(file=r"Reproductor/iconos/volume-mute.png")
        self.volume = tk.PhotoImage(file=r"Reproductor/iconos/volume.png")
        self.help= tk.PhotoImage(file=r"Reproductor/iconos/help.png")

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
        self.btnMenu.bind("<Button-1>", self.Abrirmenu)
        Tooltip(self.btnMenu,"Presione para ver carpeta de canciones")

        self.btnHelp = tk.Button(self.ventana, image=self.help, bg="#FFFFFF")
        self.btnHelp.place(relx=1.0, rely=0.02, anchor="ne", width=40, height=40)
        self.btnHelp.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnHelp,"Presione para mirar ayuda")

        self.lblMute = tk.Label(self.ventana, image=self.mute, bg="#FFFFFF")
        self.lblMute.place(relx=0.34, rely=0.84, width=20, height=20, anchor="center")

        self.lblVolumen = tk.Label(self.ventana, image=self.volume, bg="#FFFFFF")
        self.lblVolumen.place(relx=0.66, rely=0.84, width=20, height=20, anchor="center")

        # Barra de progreso 
        self.barra = tk.Canvas(self.ventana, width=509, height=10, bg="#555", bd=0, relief="flat")
        self.barra.place(relx=0.14, rely=0.67)
        self.barraprogreso = self.barra.create_rectangle(0, 0, 0, 10, fill="#1db954", outline="") 
        self.barraprogreso = self.barra.create_rectangle(0, 0, 0, 10, fill="#1db954", outline="")

        #Crear un Canvas para el control de volumen
        self.Volumen = tk.Canvas(self.ventana, width=190, height=50, bg="#FFFFFF", highlightthickness=0)
        self.Volumen.place(relx=0.49, rely=0.84, anchor="center")
        self.Volumen.create_line(20, 25, 200, 25, fill="#333", width=1)
        self.volumenMarker = self.Volumen.create_oval(20 - 5, 25 - 5, 20 + 5, 25 + 5, fill="black")
        self.Volumen.bind("<B1-Motion>", self.moverVolumen)

        
       
        

        self.ventana.mainloop()
