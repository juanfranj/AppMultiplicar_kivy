from tkinter import Label
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
#import os



from libs.inicio import Inicio
from libs.multiplicar import Multiplicar
from libs.resultados import Resultados
from libs.ajustes import Ajustes
from libs.reiniciar import Reiniciar_BaseDatos
from libs.sumar import Sumar
from libs.puzle import Puzle

LabelBase.register(name = "UrbanClass",
    fn_regular = "Urban Class.ttf"
    )

class AppMulti(MDApp):
    
    def build(self):
        Window.size = (460,820)
        self.title = "PequeMates"
        self.theme_cls.primary_palette = "Teal"

        # Carga del archivo kivy
        return Builder.load_file("main.kv")

   
AppMulti().run()