
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel

from kivy.core.window import Window
from threading import Semaphore
from time import sleep
from libs.mult import comenzar

class Multiplicar(Screen):

    def __init__(self, **kwargs):
        super(Multiplicar, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.app = MDApp.get_running_app()
        self.selecciones = []
        self.semaforo = Semaphore(0)
        self.hilos = []
        
    
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        self.tecla=self.ids["resultado"]
        self.tecla2 = self.ids["total"]

        if self.tecla.focus and (keycode == 40 or keycode == 88):
            self.pulsar_enter
            self.tecla.text = ""
            #self.tecla.hint_text = "Ingresa Valor"

        if self.tecla2.focus and (keycode == 40 or keycode == 88):
            self.boton_comenzar()
            self.iniciar_total()

 
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
        self.app.title = "Repasar Tablas"
        self.tecla2 = self.ids["total"]
        self.tecla2.focus = True

    
    def limpiar_tablas(self):
        for select in self.selecciones:
            select.active = False

    def rellenar_tablas(self):
        for select in self.selecciones:
            select.active = True

    def seleccion_estado(self):
        estados = []
        for estado in self.selecciones:
            if estado.active == True:
                estados.append(True)
            else:
                estados.append(False)
        return estados
    @property
    def pulsar_enter(self):
        self.semaforo.release()
        sleep(0.1)
        #print("semaforo verde")

    def iniciar_total(self):
        self.total = self.ids["total"]
        self.total.text = ""
    
    def boton_comenzar(self):
        self.total = self.ids["total"]
        self.texto = self.ids["texto"]
        self.resultado = self.ids["resultado"]
        self.texto_multi = self.ids["texto_multi"]
        self.multi = self.ids["multi"]
        self.estados = self.seleccion_estado()
        self.pasar = False
        self.resultado.focus = True
        #self.texto.text = f"Hola Carmen, ¿preparada para repasar las tablas?"
        #self.texto_multi.text = f"variable texto_multi: resultado = {self.resultado.text}"
        #self.multi.text = f"Probando la variable multi: total = {self.total.text}"
        #print(f"funcion multiplicar texto_mlti: {self.texto_multi} id: {id(self.texto_multi)}")
        #print(f"funcion boton_comenzar self.pasar: {self.pasar} id: {id(self.pasar)}")
        comenzar(self.total, self.texto, self.resultado, self.pasar, self.texto_multi, self.multi, self.estados, False, self.semaforo, self.hilos)
        self.iniciar_total()
    
    def boton_error(self):
        self.total = self.ids["total"]
        self.texto = self.ids["texto"]
        self.resultado = self.ids["resultado"]
        self.texto_multi = self.ids["texto_multi"]
        self.multi = self.ids["multi"]
        self.estados = self.seleccion_estado()
        self.pasar = False
        self.resultado.focus = True
        #self.texto.text = f"Hola Carmen, ¿preparada para repasar las tablas?"
        #self.texto_multi.text = f"variable texto_multi: resultado = {self.resultado.text}"
        #self.multi.text = f"Probando la variable multi: total = {self.total.text}"
        #print(f"funcion multiplicar texto_mlti: {self.texto_multi} id: {id(self.texto_multi)}")
        #print(f"funcion boton_comenzar self.pasar: {self.pasar} id: {id(self.pasar)}")
        comenzar(self.total, self.texto, self.resultado, self.pasar, self.texto_multi, self.multi, self.estados, True, self.semaforo, self.hilos)
        self.iniciar_total()
        


    
