from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
#import os



from libs.inicio import Inicio
from libs.multiplicar import Multiplicar
from libs.resultados import Resultados
from libs.ajustes import Ajustes
from libs.reiniciar import Reiniciar_BaseDatos
from libs.sumar import Sumar

#Clock.max_iteration = 1000 
#path_global = os.getcwd()
#print(path_global)
class AppMulti(MDApp):
    
    
    
    def build(self):
        Window.size = (460,720)
        self.title = "PequeMates"
        self.theme_cls.primary_palette = "Teal"

        # Carga del archivo kivy
        return Builder.load_file("main.kv")

   
AppMulti().run()