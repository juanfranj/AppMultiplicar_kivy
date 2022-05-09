from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.app import MDApp

from random import shuffle
from libs.estudiar_tabla import Fila_Tabla, Digitos

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
                background_normal = '',
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
                if isinstance(celda, Digitos):
                    self.digitos.remove_widget(celda)
                if isinstance(celda, MDFillRoundFlatButton):
                    self.layout.remove_widget(celda)
            self.tablas = []
            self.informacion.text = ""

    def tabla_multiplicar(self, *args):
        self.limpiar_grid()
        #boton volver
        self.layout = self.ids["pizarra"]
        self.digitos = self.ids["digitos"]
        self.volver = MDIconButton(on_release=self.cargar_tablas,
                                   pos_hint={"center_x": .13, "top": 0.30},
                                   icon="arrow-left-bold-box", user_font_size = "65sp",
                                   theme_text_color = "Custom", text_color = (250/255, 229/255, 211/255, 1)
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
        nombre = tabla.split(" ")[2]
        tabla = tablas[tabla.split(" ")[2]]
        for num in range(0,11):
            fila = Fila_Tabla(tabla=tabla, num = num, filas = self.tablas, nombre = nombre)
            self.tablas.append(fila)
            self.grid.add_widget(fila)

        self.resultados = [int(tabla)*i for i in range(1,11)]
        self.resultados_ordenados = self.resultados[::]
        shuffle(self.resultados)
        #resultados.append("Comprobar")
        for num in self.resultados:
            digito = Digitos(texto = str(num), widgets = self.tablas)
            self.tablas.append(digito)
            self.digitos.add_widget(digito)
        
        self.comprobar = MDFillRoundFlatButton(pos_hint = {"x":0.67, "y":.02},
                                                text = "Comprobar",
                                                font_style = "H6",
                                                theme_text_color = "Custom",
                                                text_color = (23/255, 32/255, 42/255, 1),
                                                #md_bg_color = (.33, .33, .33, 1),
                                                md_bg_color = (250/255, 229/255, 211/255, 1),
                                                on_release = self.comprobar_resultado
                                                )
        self.tablas.append(self.comprobar)
        self.layout.add_widget(self.comprobar)
    
    def comprobar_resultado(self, instance):
        for widget in self.tablas:
            if isinstance(widget, Fila_Tabla):
                widget.boton.disabled = False
                
        widget_resultados = [widget for widget in self.tablas if isinstance(widget, Fila_Tabla)][1::]
        for correcto, numero in zip(self.resultados_ordenados, widget_resultados):
            print(f"correcto: {correcto} calculado: {numero.boton.text}, ", end = " ")
            if len(numero.boton.text) >0 and  correcto == int(numero.boton.text):
                print("CORRECTO")
                numero.boton.color = (0, 1, 0, 1)
            else:
                numero.boton.text = ""
                #numero.boton.color = (1, 0, 0, 1)
        