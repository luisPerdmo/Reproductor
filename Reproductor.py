import tkinter as tk
from tkinter import *
import pygame.mixer as mx
from tkinter import filedialog
from Tooltip import Tooltip
from tkinter import messagebox
import os 

class Reproductor():

    def adelantar10Segundos(self, event):
        if self.cancionActual and mx.music.get_busy():  
            tiempoActual = mx.music.get_pos() / 1000  
            nuevoTiempo = tiempoActual + 10         
            if nuevoTiempo < self.duracionTotal:      
                mx.music.set_pos(nuevoTiempo)       
            else:
                mx.music.stop()

    def retrocederCancion(self, event):
        pass

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

    def cambiarCancionSiguiente(self, event):
        if self.archivosCanciones:
            actual = self.listaCanciones.curselection()
            if not actual:
                return     
            actual = actual[0]
            siguiente = (actual + 1) % len(self.archivosCanciones)
            self.listaCanciones.selection_clear(0, tk.END)
            self.listaCanciones.selection_set(siguiente)
            self.play(event)

    def cambiarCancionAnterior(self, event):
        if self.archivosCanciones:
            caActual = self.listaCanciones.curselection()
            if not caActual:
                return
            caActual = caActual[0]
            caAnterior = (caActual - 1) % len(self.archivosCanciones)
            self.listaCanciones.selection_clear(0, tk.END)
            self.listaCanciones.selection_set(caAnterior)
            self.play(event)

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
                self.duracionTotal = self.obtenerDuracionCancion(cancion) 
                self.tiempoGuardado = 0 
                self.actualizarProgreso()
                nombreCancion = self.archivosCanciones[indice]
                self.lblNombreCancion.config(text=nombreCancion)
            else:  
                if mx.music.get_busy(): 
                    mx.music.pause() 
                    self.btnPlay.config(image=self.play1) 
                else: 
                    posicion = mx.music.get_pos()  
                    mx.music.unpause()  
                    self.btnPlay.config(image=self.pause) 
                    self.tiempoGuardado = posicion / 1000
        else:            
            messagebox.showerror("Advertencia!", "No Ha Puesto La Canción...")

    def actualizarProgreso(self):
        if self.cancionActual:
            if mx.music.get_busy():
                tiempoTranscurrido = mx.music.get_pos() / 1000
                self.tiempoGuardado = tiempoTranscurrido  
            else:
                tiempoTranscurrido = self.tiempoGuardado
            progreso = tiempoTranscurrido / self.duracionTotal 
            self.barra.coords(self.barraprogreso, (0, 0, progreso * 520, 20))
            minutosTranscurridos = int(tiempoTranscurrido // 60)
            segundosTranscurridos = int(tiempoTranscurrido % 60)
            tiempoTranscurridoStr = f"{minutosTranscurridos:02}:{segundosTranscurridos:02}"
            minutosTotal = int(self.duracionTotal // 60)
            segundosTotal = int(self.duracionTotal % 60)
            duracionTotalStr = f"{minutosTotal:02}:{segundosTotal:02}"
            self.lblTiempoTranscurrido.config(text=tiempoTranscurridoStr)
            self.lblDuracionTotal.config(text=duracionTotalStr)
            self.ventana.after(100, self.actualizarProgreso)
    
    def obtenerDuracionCancion(self, cancion):
        sound = mx.Sound(cancion)
        return sound.get_length()

    #Muestra la ayuda 
    def mostrarAyuda(self, event):
        ayuda_texto = ("Bienvenido al Reproductor de Música.\n\n"
        "Aquí están los atajos de teclado disponibles:\n\n"
        "• Espacio (space): Reproducir/Pausar la canción actual.\n"
        "• Flecha derecha (Right): Avanzar a la siguiente canción.\n"
        "• Flecha izquierda (Left): Retroceder a la canción anterior.\n"
        "• Ctrl + S: Siguiente canción.\n"
        "• Ctrl + C: Canción anterior.\n"
        "• Ctrl + M: Abrir el menú de canciones.\n"
        "• F1: Mostrar esta ayuda.\n\n"
        "¡Disfruta de la música!")
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
        self.duracionTotal = 0  # Duración total de la canción

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
        self.btnPlay = tk.Label(self.ventana, image=self.play1, bg="#FFFFFF")
        self.btnPlay.place(relx=0.5, rely=0.76, width=40, height=40, anchor="center")
        self.btnPlay.bind("<Button-1>", self.play)
        Tooltip(self.btnPlay,"Presione para iniciar la cancion")

        self.btnSkip = tk.Label(self.ventana, image=self.skip, bg="#FFFFFF")
        self.btnSkip.place(relx=0.60, rely=0.76, width=40, height=40, anchor="center")
        self.btnSkip.bind("<Button-1>", self.cambiarCancionSiguiente)
        Tooltip(self.btnSkip,"Presione para cambiar de cancion")

        self.btnSkip2 = tk.Label(self.ventana, image=self.skip2, bg="#FFFFFF")
        self.btnSkip2.place(relx=0.40, rely=0.76, width=40, height=40, anchor="center")
        self.btnSkip2.bind("<Button-1>", self.cambiarCancionAnterior)
        Tooltip(self.btnSkip2,"Presione para cambiar la cancion")

        self.btnBack2 = tk.Label(self.ventana, image=self.back2, bg="#FFFFFF")
        self.btnBack2.place(relx=0.33, rely=0.76, width=40, height=40, anchor="center")
        Tooltip(self.btnBack2,"Presione para regresar 10 segundos")

        self.btnBack = tk.Label(self.ventana, image=self.back, bg="#FFFFFF")
        self.btnBack.place(relx=0.67, rely=0.76, width=40, height=40, anchor="center")
        self.btnBack.bind("<Button-1>", self.adelantar10Segundos)
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

        #Barra de progreso 
        self.barra = tk.Canvas(self.ventana, width=509, height=10, bg="#C6C6C6", bd=0, relief="flat")
        self.barra.place(relx=0.14, rely=0.67)
        self.barraprogreso = self.barra.create_rectangle(0, 0, 0, 10, fill="#000000", outline="") 

        #tiempo transcurrido y la duración total
        self.lblTiempoTranscurrido = tk.Label(self.ventana, text="00:00", bg="#FFFFFF", font=("Helvetica", 10))
        self.lblTiempoTranscurrido.place(relx=0.15, rely=0.64)
        self.lblDuracionTotal = tk.Label(self.ventana, text="00:00", bg="#FFFFFF", font=("Helvetica", 10))
        self.lblDuracionTotal.place(relx=0.82, rely=0.64)

        #Nombre de la cancion 
        self.lblNombreCancion = tk.Label(self.ventana, text="", bg="#FFFFFF", font=("Helvetica", 12))
        self.lblNombreCancion.place(relx=0.5, rely=0.60, anchor="center")

        #control de volumen
        self.Volumen = tk.Canvas(self.ventana, width=190, height=50, bg="#FFFFFF", highlightthickness=0)
        self.Volumen.place(relx=0.49, rely=0.84, anchor="center")
        self.Volumen.create_line(20, 25, 200, 25, fill="#333", width=1)
        self.volumenMarker = self.Volumen.create_oval(self.posicionVolumen - 5, 25 - 5, self.posicionVolumen + 5, 25 + 5, fill="black")
        self.Volumen.bind("<B1-Motion>", self.moverVolumen)

        #Atajos 
        self.ventana.bind("<space>", self.play)  
        self.ventana.bind("<Right>", self.adelantar10Segundos)  
        self.ventana.bind("<Left>", self.retrocederCancion) 
        self.ventana.bind("<Control-s>", self.cambiarCancionSiguiente) 
        self.ventana.bind("<Control-c>", self.cambiarCancionAnterior)
        self.ventana.bind("<Control-m>", self.Abrirmenu)
        self.ventana.bind("<F1>", self.mostrarAyuda)         
  
        self.ventana.mainloop()
