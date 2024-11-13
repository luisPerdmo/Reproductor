import tkinter as tk
from tkinter import *
import pygame.mixer as mx
from tkinter import filedialog
from Tooltip import Tooltip
from tkinter import messagebox
import os 

class Reproductor():

    def Abrirmenu(self, event):
        self.ventanaMenu = tk.Toplevel(self.ventana)
        self.ventanaMenu.title("Carpeta de Canciones")
        self.ventanaMenu.config(width=400, height=300)
        self.ventanaMenu.resizable(0,0)
        self.ventanaMenu.config(bg="gray")

        # Crear el Listbox dentro de la ventana del menú
        self.listaCanciones = Listbox(self.ventanaMenu, bg="#FFFFFF", width=43, height=17)
        self.listaCanciones.place(relx=0.5, rely=0.5, anchor="center")

        # Botón para cargar la carpeta de canciones
        self.lblCargarCarpeta = tk.Label(self.ventanaMenu, image=self.carpeta1, bg="#FFFFFF")
        self.lblCargarCarpeta.place(relx=0.5, rely=0.9, anchor="center", width=40, height=40)
        self.lblCargarCarpeta.bind("<Button-1>", self.cargarCarpetaCanciones)
        Tooltip(self.lblCargarCarpeta, "Haz clic para cargar una carpeta de canciones")

    # Método para actualizar el Listbox con los nombres de las canciones
    def actualizarListaCanciones(self):
        self.listaCanciones.delete(0, tk.END)  
        for cancion in self.archivosCanciones:
            self.listaCanciones.insert(tk.END, cancion) 

    # Método para cargar la carpeta de canciones
    def cargarCarpetaCanciones(self, event):
        self.carpeta = filedialog.askdirectory()
        if self.carpeta:
            self.archivosCanciones = [f for f in os.listdir(self.carpeta) if f.endswith('.mp3')]
            self.actualizarListaCanciones()

    def moverVolumen(self, event):
        if 20 <= event.x <= 184:  
            self.Volumen.coords(self.volumenMarker, event.x - 5, 25 - 5, event.x + 5, 25 + 5) 
            self.posicionVolumen = event.x 
            nuevoVolumen = (self.posicionVolumen - 20) / 180 
            self.volumen = max(0, min(1, nuevoVolumen)) 
            mx.music.set_volume(self.volumen) 

    # Método para reproducir la canción seleccionada
    def play(self, event):    
        if self.listaCanciones.curselection(): 
            indice = self.listaCanciones.curselection()[0] 
            cancion = os.path.join(self.carpeta, self.archivosCanciones[indice])
            if self.cancionActual != cancion:  
                mx.music.load(cancion)
                mx.music.play()
                self.cancionActual = cancion  
                self.btnPlay.config(image=self.pause) 
            else:  
                if mx.music.get_busy(): 
                    mx.music.pause() 
                    self.btnPlay.config(image=self.play1) 
                else: 
                    posicion = mx.music.get_pos()  
                    mx.music.unpause()  
                    self.btnPlay.config(image=self.pause)  

    #Pausa la cancion
    def pausa(self):
        mx.music.pause()
        self.btnPlay.config(image=self.play)  
        print("Canción pausada.")

    #Muestra la ayuda 
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
        self.posicionVolumen = 20

        #frame
        self.frameBorde = tk.Frame(self.ventana, bd=5, relief="ridge", bg="black")
        self.frameBorde.place(relx=0.15, rely=0.15, width=500, height=240)
        self.frame = tk.Frame(self.frameBorde, bg="#FFFFFF")
        self.frame.place(width=490, height=230)

        #Iconos 
        self.play1 = tk.PhotoImage(file=r"Reproductor/iconos/play.png")
        self.pause = tk.PhotoImage(file=r"Reproductor/iconos/pause.png")
        self.skip2 = tk.PhotoImage(file=r"Reproductor/iconos/play-skip2.png")
        self.skip = tk.PhotoImage(file=r"Reproductor/iconos/play-skip.png")
        self.back = tk.PhotoImage(file=r"Reproductor/iconos/back.png")
        self.back2 = tk.PhotoImage(file=r"Reproductor/iconos/back2.png")
        self.menu = tk.PhotoImage(file=r"Reproductor/iconos/menu.png")
        self.mute = tk.PhotoImage(file=r"Reproductor/iconos/volume-mute.png")
        self.volume = tk.PhotoImage(file=r"Reproductor/iconos/volume.png")
        self.help = tk.PhotoImage(file=r"Reproductor/iconos/help.png")
        self.carpeta1 = tk.PhotoImage(file=r"Reproductor/iconos/solidmusic.png")

        #Botones
        self.btnPlay = tk.Button(self.ventana, image=self.play1)
        self.btnPlay.place(relx=0.5, rely=0.76, width=40, height=40, anchor="center")
        self.btnPlay.bind("<Button-1>", self.play)
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

        self.lblMenu = tk.Label(self.ventana, image=self.menu, bg="#FFFFFF")
        self.lblMenu.place(relx=0.80, rely=0.56, width=42, height=25)
        self.lblMenu.bind("<Button-1>", self.Abrirmenu)
        Tooltip(self.lblMenu,"Presione para ver carpeta de canciones")

        self.btnHelp = tk.Label(self.ventana, image=self.help, bg="#FFFFFF")
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
        self.volumenMarker = self.Volumen.create_oval(self.posicionVolumen - 5, 25 - 5, self.posicionVolumen + 5, 25 + 5, fill="black")
        self.Volumen.bind("<B1-Motion>", self.moverVolumen)
        

        self.ventana.mainloop()
