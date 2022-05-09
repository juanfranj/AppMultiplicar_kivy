from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextFieldRound

class Fila_Tabla(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()
        
        self.tabla = kwargs["tabla"]
        self.num = kwargs["num"]
        self.tablas =  kwargs["filas"]
        self.nombre = kwargs["nombre"]
        if self.num == 0:
            texto = f"Tabla del {self.nombre}"
            desv = 0
        else:
            texto = f"{self.tabla} x {self.num}  = "
            desv = 0.05
        self.title = Label(text = texto,
                        pos_hint={"center_x": .5 - desv, "center_y": .5}, size_hint=(.5, .3),
                        theme_text_color="Custom", font_style="H6", halign="center",
                        font_name = "UrbanClass", font_size = "40sp")
        self.textfield = MDTextFieldRound(
                                    pos_hint={"center_x": .75 - desv, "center_y": .5}, size_hint=(.08, .7),
                                    halign = "center", readonly = True, font_size = "40sp", font_name = "UrbanClass",
                                    #background_active = "Blue", background_disabled_normal = "Blue", background_normal = "Blue",
                                    #background_color = (.90, .50, .14, 1),
                                    normal_color = (.75, .79, .79, 1), color_active = (.52, .75, .91, 1)
    
                                  )
        self.boton = Button(
                        pos_hint={"center_x": .75 - desv, "center_y": .5}, size_hint=(.15, .9),
                        halign = "center",  font_size = "35sp", font_name = "UrbanClass",
                        background_normal = '',
                        background_color = (153/255, 163/255, 164/255, 1),
                        #background_disabled_normal = "Green",
                        #disabled_color = (.52, .75, .91, 1),
                        #border = (32,32,32,32)
                        )
        self.boton.bind(on_press = self.desactivar)

        if self.num == 1: 
            #self.textfield.focus = True
            self.boton.disabled = True
            #self.boton.text = str(self.tabla)

        self.add_widget(self.title)
        if self.num >0:
            #self.add_widget(self.textfield)
            self.add_widget(self.boton)
    
    def desactivar(self, instance):

        #print(instance)
        #print(self.tablas)
        for widget in self.tablas:
            if isinstance(widget, Fila_Tabla):
                #print(widget.boton)
                widget.boton.disabled = False
        #self.boton.background_color = (.52, .75, .91, 1)
        self.boton.disabled = True

class Digitos(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()
        self.texto = kwargs["texto"]
        self.widgets = kwargs["widgets"]
        self.boton = Button(
                        pos_hint={"center_x": .5, "center_y": .5}, size_hint=(.8, .8),
                        halign = "center",  font_size = "30sp", font_style = "H6", font_name = "UrbanClass",
                        text = self.texto,
                        color = (23/255, 32/255, 42/255, 1),
                        background_normal = '',
                        background_color = (250/255, 229/255, 211/255, 1),
                        #on_press = self.escribir_num
                        )
        self.boton.bind(on_press = self.escribir_num)
        self.add_widget(self.boton)
    
    def escribir_num(self, instance):
        for widget in self.widgets:
            if isinstance(widget, Fila_Tabla) and widget.boton.disabled:
                widget.boton.text = self.texto
                self.activar_siguiente(self.widgets.index(widget))
                break

    def activar_siguiente(self, indice):
        for widget in self.widgets:
            if isinstance(widget, Fila_Tabla):
                widget.boton.disabled = False

        for widget in self.widgets:
                if isinstance(widget, Fila_Tabla):
                    widget.boton.disabled = False
                    if indice == 11:
                        self.widgets[2].boton.disabled = True
                    else:
                        self.widgets[indice + 1].boton.disabled = True
    
    
                