import tkinter as tk
from tkinter import *

class Reproductor():
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Musica")
        self.ventana.config(width=800, height=600)
        self.ventana.resizable(0,0)

        self.ventana.mainloop()
