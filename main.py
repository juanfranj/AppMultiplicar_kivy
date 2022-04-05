from kivymd.app import MDApp
from kivy.lang import Builder



from libs.inicio import Inicio
from libs.multiplicar import Multiplicar
from libs.resultados import Resultados
from libs.ajustes import Ajustes

#Clock.max_iteration = 1000 
class AppMulti(MDApp):
    
    
    
    def build(self):
        self.title = "AppMultiplicar"
        self.theme_cls.primary_palette = "Teal"

        # Carga del archivo kivy
        return Builder.load_file("main.kv")

   
AppMulti().run()