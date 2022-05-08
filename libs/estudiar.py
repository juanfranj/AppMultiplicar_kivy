from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp

from libs.estudiar_tabla import Fila_Tabla

class Estudiar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.tablas = []


    def on_pre_enter(self, *args):
        self.app.title = "Estudiar Tablas"
        self.cargar_tablas()
    
    def cargar_tablas(self, *args):
        self.limpiar_grid()
        
        self.grid = self.ids["botones"]
        self.grid.rows = 3
        self.grid.cols = 3
        self.informacion = self.ids["informacion"]
        self.informacion.text = "Elige la tabla que quieres Estudiar"
        nombres = ["Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"]
        for i in range (0,9):
            self.boton = Button(
                text = f"Tabla del {nombres[i]}",
                theme_text_color = "Custom",
                text_color = (1, 1, 1, 1),
                #background_disabled_normal = '',
                #disabled_color = (1, 1, 1, 1),
                #background_normal = '',
                background_color = (0.52, 0.76, 0.91, .8),
                font_name = "Urban Class",
                font_size = "12sp", 
                on_release = self.tabla_multiplicar
               
            )
            self.tablas.append(self.boton)
            self.grid.add_widget(self.boton)

    def limpiar_grid(self):
        if len(self.tablas) > 0:
            for celda in self.tablas:
                self.grid.remove_widget(celda)
                if isinstance(celda,MDIconButton):
                    self.layout.remove_widget(celda)
            self.tablas = []
            self.informacion.text = ""

    def tabla_multiplicar(self, *args):
        self.limpiar_grid()
        #boton volver
        self.layout = self.ids["pizarra"]
        self.volver = MDIconButton(on_release=self.cargar_tablas,
                                   pos_hint={"center_x": .1, "top": 1},
                                   icon="arrow-left-bold-box", user_font_size = "45sp",
                                   theme_text_color = "Custom", text_color = (1, 1, 1, 1)
                                   )
        self.layout.add_widget(self.volver)
        self.tablas.append(self.volver)
        #grid para las filas con la clase creada
        self.grid.rows = 11
        self.grid.cols = 1
        tablas = {"Dos": 2, "Tres" : 3, "Cuatro" : 4, 
            "Cinco" : 5, "Seis" : 6, "Siete" : 7,
             "Ocho" : 8, "Nueve" : 9, "Diez" : 10}
        tabla = [i.text for i in args][0]
        tabla = tablas[tabla.split(" ")[2]]
        for num in range(0,11):
            fila = Fila_Tabla(tabla=tabla, num = num)
            self.tablas.append(fila)
            self.grid.add_widget(fila)
        
        
        