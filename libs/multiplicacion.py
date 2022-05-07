from kivy.uix.screenmanager import Screen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp

from libs.mutliplicaciones import *

class Multiplicacion(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.dificultad = []
        self.celdas = []

    def on_pre_enter(self, *args):
        self.app.title = "Multiplicar"
        self.comprobar_celdas()

    def checkbox_click(self, instance, value):
        for i in self.dificultad:
            if i != instance:
                i.active = False
            else:
                i.active = value
        instance.active = value
    
    def on_kv_post(self, *args):
        self.nivel = self.ids["dificultad"]
        niveles = ["Facil", "Medio", "Dificil"]
        for nivel in niveles:
            self.nombre = MDLabel(
                text = nivel,
                size_hint = (.8, .5),
                theme_text_color = "Custom",
                text_color = (1, 1, 1, 1),
                halign = "center"
                )
            self.nombre.font_name = "Urban Class"
            self.font_size = "15sp"
            self.check = MDCheckbox(size_hint= (.2, .2))
            self.check.bind(active=self.checkbox_click)
            self.dificultad.append(self.check)
            self.nivel.add_widget(self.nombre)
            self.nivel.add_widget(self.check)
        
        self.dificultad[0].active = True
    
    def mostrar_multiplicacion(self):
        self.comprobar_celdas()
        self.texto_ayuda = self.ids["informacion"]
        fin = False
        while not fin:
            try:
                self.datos_entrada()
                self.matriz, self.num_col, self.num_fil = multiplicar([self.multiplicando, self.multiplicador])
                fin = True
            except:
                print(f"error")
        if self.str_dif == "facil": self.num_fil = 5
        self.grid = self.ids["grid"]
        self.grid.cols = 8
        self.grid.rows = 15
        self.escribir_multiplicacion_media()
        self.imprimir_resultado(self.matriz)
        self.texto_ayuda.text = f"Multiplicar"

    def mostrar_resultado(self):
        try:
            self.comprobar_celdas() 
            self.escribir_resultado_media()
            self.texto_ayuda.text = f"RESULTADO"  
            self.texto_ayuda.haling = "center" 
        except:
            self.texto_ayuda = self.ids["informacion"]
            self.texto_ayuda.text = f"Pulsa Boton Calcular"  
            self.texto_ayuda.haling = "center" 

    def escribir_multiplicacion_media(self):
        self.resultados = [['-' for j in range(0,self.num_col)] for i in range(0,self.num_fil)]
        #imprimir_resultado(self.resultados, self.num_fil)
        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):
                self.resultados[i][j] = self.matriz[i][j]
                if (i > 3)  and i != self.num_fil-2 and self.matriz[i][j] != '-':
                    self.texto = MDTextField(
                        input_type = "number",
                        halign ="center",
                        text_color = (1.0, 1.0, 1.0, 1),
                        font_name = "UrbanClass",
                        hint_text = '?',
                        font_size = "25sp",
                        # background_disabled_normal =  '',
                        # background_normal = '',
                        # background_color = (0.207, 0.635, 0.423, 0.9)
                        foreground_color = (.3,.3,.3,1),
                        disabled_foreground_color = (.3,.3,.3,1)
                        
                    )
                    #self.texto.fill_color = (.0, .0, .0, 0)
                    self.resultados[i][j] = self.texto
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif self.matriz[i][j] != '-' and i != 3 and i != self.num_fil-2:
                    self.texto = Label(
                        text = f"{self.matriz[i][j]}",
                        #theme_text_color = "Custom",
                        #text_color = (1, 1, 1, 1),
                        )
                    self.texto .font_name = "UrbanClass"
                    self.texto.font_size = "25sp"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif i == 3:
                    if j >= 7 - len(str(self.multiplicando)):
                        self.texto = Label( text = f"______")                                  
                    else:
                        self.texto = Label( text = f" ")
                        
                    self.texto.font_size = "40sp" 
                    self.texto.size_hint_y = None
                    self.texto.height= "1dp"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)
                
                elif i == self.num_fil-2:
                    if j >= 8 - len(str(self.multiplicador*self.multiplicando)):
                        self.texto = Label( text = f"______")                                  
                    else:
                        self.texto = Label( text = f" ")

                    self.texto.font_size = "40sp" 
                    self.texto.size_hint_y = None
                    self.texto.height= "1dp"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)
                

                else:
                    self.texto = Label(text = f"")
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

        comenzar =  self.num_col * self.num_fil
        #print("Comenzando en blanco: ", comenzar)
        for celda in range(comenzar, 120):
            self.texto = Label(text = f" ")
            self.celdas.append(self.texto)
            self.grid.add_widget(self.texto)

    def escribir_resultado_media(self):

        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):

                if self.matriz[i][j] != '-' and i != 3 and i != self.num_fil-2:
                    self.texto = Label(
                        text = f"{self.matriz[i][j]}",
                        )
                    self.texto .font_name = "UrbanClass"
                    self.texto.font_size = "25sp"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)

                elif i == 3:
                    if j >= 7 - len(str(self.multiplicando)):
                        self.texto = Label( text = f"-----")                                  
                    else:
                        self.texto = Label( text = f" ")
                        
                    self.texto.font_size = "40sp" 
                    self.texto.size_hint_y = None
                    self.texto.height= "1dp"
                    self.celdas.append(self.texto)
                    self.grid.add_widget(self.texto)
                
                elif i == self.num_fil-2:
                    if j >= 8 - len(str(self.multiplicador*self.multiplicando)):
                        self.texto = Label( text = f"-----")                                  
                    else:
                        self.texto = Label( text = f" ")

                    self.texto.font_size = "40sp" 
                    self.texto.size_hint_y = None
                    self.texto.height= "1dp"
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

    def comprobar_celdas(self):
        if len(self.celdas) > 0:
            for celda in self.celdas:
                self.grid.remove_widget(celda)
            self.celdas = []
    
    def datos_entrada(self):

        if self.dificultad[0].active == True:
            self.str_dif = "facil"
            multiplicando = 3
            multiplicador = 1
        elif self.dificultad[1].active == True:
            self.str_dif = "medio"
            multiplicando = 4
            multiplicador = 2
        elif self.dificultad[2].active == True:
            self.str_dif = "dificil"
            multiplicando = 4
            multiplicador = 3
        else:
            self.str_dif = "facil"
            multiplicando = 3
            multiplicador = 1
        
        self.multiplicando, self. multiplicador = devolver_factores(multiplicando, multiplicador)
    
    
    def mostrar_comprobar_resultado(self):
        try:
            
            self.comprobar_resultado()
        except AttributeError as e:
            print(f"Error obtenido es: {e}")
            self.texto_ayuda = self.ids["informacion"]
            self.texto_ayuda.text = f"Pulsa Boton Calcular"  
            self.texto_ayuda.haling = "center"
    
    def comprobar_resultado(self):
        resultados_pantalla = self.obtener_resultados_pantalla()
        errores = self.comprobar_multi(resultados_pantalla)
        self.escribir_errores(errores)

        imprimir_resultado(resultados_pantalla, self.num_fil)
        
    def obtener_resultados_pantalla(self):
        resultados = [['-' for j in range(0,self.num_col)] for i in range(0,self.num_fil)]
        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):
                if not isinstance(self.resultados[i][j], str):
                    resultados[i][j] = self.resultados[i][j].text
        return resultados
    
    def comprobar_multi(self, resultados_pantalla):
        errores = 0
        for i in range(0,self.num_fil):
            for j in range(0,self.num_col):
                if not isinstance(self.resultados[i][j], str):
                    if resultados_pantalla[i][j] != self.matriz[i][j]:
                        self.resultados[i][j].text_color = (1.0, .0, .0, 1)
                        self.resultados[i][j].text = ""
                        self.resultados[i][j].hint_text = "?"
                        errores += 1
                    else:
                        self.resultados[i][j].hint_text = ""
                        self.resultados[i][j].text_color = (1.0, 1.0, 1.0, 1)
        return errores
                        
    def escribir_errores(self, errores):
        if errores > 0:
            self.texto_ayuda.text = f"{errores} ERRORES"  
            self.texto_ayuda.haling = "center"
        else:
            self.texto_ayuda.text = f"¡¡CORRECTO!!"  
            self.texto_ayuda.haling = "center"                   
                   
    def imprimir_resultado(self, matriz):
        j = 0
        print("Resultado:\n")
        for fila in matriz:
            print(f"  {fila}")
            j += 1