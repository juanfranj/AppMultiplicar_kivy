
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
 

from kivymd.app import MDApp




from libs.suma import *


class Sumar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.celdas = []

    def on_pre_enter(self, *args):
        self.app.title = "Sumar"

    def mostrar_suma(self):
        #self.pizarra = self.ids["pizarra"]
        self.comprobar_celdas()

        self.texto_ayuda = self.ids["informacion"]
        self.sumandos = self.ids["sumandos"]
        self.digitos = self.ids["digitos"]
        self.datos_entrada()
        self.numeros = devolver_sumandos(self.int_sumandos, self.int_digitos)
        self.matriz, self.num_fil, self.num_col = suma(self.numeros, self.int_digitos)
        
        self.grid = self.ids["grid"]
        self.grid.cols = 8
        self.grid.rows = 12
        
        
            
        self.escribir_sumandos(self.int_digitos)
        
        #print(f"El numero de celdas es: {len(self.celdas)}")
        #imprimir_pregunta(self.matriz, self.num_fil)
        #imprimir_resultado(self.matriz, self.num_fil)
        self.texto_ayuda.text = f"SUMAR"  
        #self.texto_ayuda.haling = "center"           
    
    def mostrar_resultado(self):
        
        try:
            self.comprobar_celdas() 
            self.escribir_resultado(self.int_digitos)
            self.texto_ayuda.text = f"RESULTADO"  
            self.texto_ayuda.haling = "center" 
        except:
            self.texto_ayuda = self.ids["informacion"]
            self.texto_ayuda.text = f"Pulsa Botón Calcular"  
            self.texto_ayuda.haling = "center" 
             




    def comprobar_celdas(self):
        if len(self.celdas) > 0:
            for celda in self.celdas:
                self.grid.remove_widget(celda)
            self.celdas = []
           
            

    def escribir_resultado(self, mas):
        #print("el numero de filas es: ", self.num_fil)
        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):
                if i == 0 and self.matriz[i][j] != '-':
                    self.texto = Label(text = f"{self.matriz[i][j]}",
                     font_size = "25",
                     color = (.36, .68, .89, 1)
                    )
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif self.matriz[i][j] != '-' and i != self.num_fil-2:
                    self.texto = Label(text = f"{self.matriz[i][j]}", font_size = "35")
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif i == self.num_fil-2 and j >= (7-mas):
                    self.texto = Label(text = f"______")
                    self.texto.font_size = "40"
                    #self.texto.size_hint = (1., .5)
                    #self.texto.height = "20"
                    #self.texto.valign = "top"
                    #self.texto.halign = "center"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                else:
                    self.texto = Label(text = f"")
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

        comenzar =  self.num_col * self.num_fil
        #print("Comenzando en blanco: ", comenzar)
        for celda in range(comenzar, 96):
            self.texto = Label(text = f"")
            self.celdas.append(self.texto)
            self.grid.add_widget(self.texto)

    def escribir_sumandos(self, mas):
        #print("el numero de filas es: ", self.num_fil)
        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):
                if (i == 0 and j >= (7-mas)) or (i == self.num_fil-1 and j >= (7-mas)):
                    #self.texto = Label(text = f"")
                    self.texto = MDTextField(
                        #hint_text = "1..9",
                        input_type = "number",
                        halign ="center",
                        #font_size = "25",
                        #color_mode = 'custom',
                        text_color = (1.0, 1.0, 1.0, 1)
                        #foreground_color = (.0, .0, .0, 1)
                    )
                    if i == 0:
                        self.texto.font_size = '25'
                    else:
                        self.texto.font_size = '35'
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif self.matriz[i][j] != '-' and i != self.num_fil-2:
                    self.texto = Label(text = f"{self.matriz[i][j]}", font_size = "35")
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif i == self.num_fil-2 and j >= (7-mas):
                    self.texto = Label(text = f"_____")
                    self.texto.font_size = "40"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                else:
                    self.texto = Label(text = f"")
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

        comenzar =  self.num_col * self.num_fil
        #print("Comenzando en blanco: ", comenzar)
        for celda in range(comenzar, 96):
            self.texto = Label(text = f" ")
            self.celdas.append(self.texto)
            self.grid.add_widget(self.texto)
    
    def datos_entrada(self):
        try:
            if int(self.sumandos.text) > 5 or int(self.sumandos.text) < 2:
                self.int_sumandos = 3
            else:
                self.int_sumandos = int(self.sumandos.text)
        except:
            self.int_sumandos = 3
            #self.texto_ayuda.text = f"Sumandos_error: {self.int_sumandos} Digitos: {self.digitos.text}"
        
        #calculo de digitos
        try:
            if int(self.digitos.text) > 4 or int(self.digitos.text) < 1:
                self.int_digitos = 3
            else:
                self.int_digitos = int(self.digitos.text)
        except:
            self.int_digitos = 3
            #self.texto_ayuda.text = f"Sumandos: {self.int_sumandos} Digitos_error: {self.int_digitos}"

        self.sumandos.text = ""
        self.digitos.text = ""
        #return self.int_sumandos, self.int_digitos

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size