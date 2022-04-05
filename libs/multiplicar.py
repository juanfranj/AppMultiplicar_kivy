from tabnanny import check
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel



        

class Multiplicar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.selecciones = []

    
    def on_kv_post(self, *args):
        self.mult = self.ids["tablas"]
        tablas = {f"tabla{i}":str(i) for i in range(2,11)}
        for nombre, tabla in tablas.items():
            self.check = MDCheckbox(size_hint= (.2, .2), pos_hint={"left": 0, "top": .9})
            self.tab = MDLabel(text=tabla, size_hint= (.3, .3))
            self.selecciones.append(self.check)
            if int(tabla) <=5:
                self.check.active = True
            self.mult.add_widget(self.check)
            self.mult.add_widget(self.tab)

    def on_pre_enter(self, *args):
        self.app.title = "Multiplicar"
    
    def limpiar_tablas(self):
        for select in self.selecciones:
            select.active = False

    def rellenar_tablas(self):
        for select in self.selecciones:
            select.active = True

    
