from turtle import pos
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp 
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.metrics import dp

from bd.funcionesBD import resultados_totales, consultar_resultados

class Resultados(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
    def tabla_resultados(self):
        #self.clear_canvas()
        self.tablas = self.ids["tablas"]
        self.values = resultados_totales()
        self.resultados = MDDataTable(
            size_hint = (1, 1),
            pos_hint = {"x":0, "top":1},
            use_pagination=True,
            check = False,
            rows_num = 8,
            column_data=[
                    ("MULTIPLICACIONES", dp(50)),
                    ("ACIERTOS", dp(30)),
                    ("ERRORES", dp(30)),
                ],
            row_data=[
                resultados
                for resultados in self.values
            ]
        )
        self.tablas.add_widget(self.resultados)

    def tabla_estadisticas(self):
        self.estadistica = self.ids["tablas"]
        self.values = consultar_resultados()
        self.total = sum(self.values)
        self.resultados = MDDataTable(
            size_hint = (1, 1),
            pos_hint = {"x":0, "top":1},
            use_pagination=True,
            check = False,
            rows_num = 8,
            column_data=[
                    ("ESTADISTICAS", dp(50)),
                    ("TOTAL", dp(30)),
                    ("(%)", dp(30)),
                ],
            row_data=[
                ("Multiplicaciones", self.total, ""),
                ("Aciertos", self.values[0], f"{round((self.values[0]/self.total)*100, 1)} %"),
                ("Errores", self.values[1], f"{round((self.values[1]/self.total)*100, 1)} %")
            ]
        )
        self.estadistica.add_widget(self.resultados)
    


    def clear_canvas_tablas(self):
        self.clear_widgets()
        base=Resultados()
        self.add_widget(base)


    def on_pre_enter(self, *args):
        self.app.title = "Resultados"
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
