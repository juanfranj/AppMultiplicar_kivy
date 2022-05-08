from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextFieldRound

class Fila_Tabla(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()
        
        self.tabla = kwargs["tabla"]
        self.num = kwargs["num"]
        if self.num == 0:
            texto = f"Tabla del {self.tabla}"
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
        if self.num == 1: self.textfield.focus = True
        self.add_widget(self.title)
        if self.num >0:
            self.add_widget(self.textfield)
        