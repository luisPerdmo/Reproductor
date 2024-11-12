import tkinter as tk
from tkinter import *

class Reproductor():
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Musica")
        self.ventana.config(width=800, height=600)
        self.ventana.resizable(0,0)

        #frame
        self.frameBorde = tk.Frame(self.ventana, bd=5, relief="ridge", bg="black")
        self.frameBorde.place(relx=0.20, rely=0.20, width=500, height=200)
        self.frame = tk.Frame(self.frameBorde)
        self.frame.place(width=490, height=190)

        #Iconos 
        self.play = tk.PhotoImage(file=r"Reproductor/iconos/play.png")
        self.pause = tk.PhotoImage(file=r"Reproductor/iconos/pause.png")
        self.skip2 = tk.PhotoImage(file=r"Reproductor/iconos/play-skip2.png")
        self.skip = tk.PhotoImage(file=r"Reproductor/iconos/play-skip.png")
        self.back = tk.PhotoImage(file=r"Reproductor/iconos/back.png")

        #Botones
        self.btnPlay = tk.Button(self.ventana, image=self.play)
        self.btnPlay.place(relx=0.5, rely=0.65, width=40, height=40)

        self.ventana.mainloop()
