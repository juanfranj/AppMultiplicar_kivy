from time import sleep
from random import randint, shuffle
from bd.funcionesBD import *
import os
from threading import Thread



def comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas, repaso, semaforo):
    t1 = Thread(target =   multiplicar, args = (total,texto, resultado, pasar, texto_multi, mul, tablas, repaso, semaforo), daemon = True)
    t1.start()
    

def multiplicar(total, texto, resultado, pasar, texto_multi, multi, tablas_chk, repaso, semaforo):
    tab = tablas_chk
    #texto.text = "entrando en el programa de multiplicar"
    #print(tablas_chk)
    #tablas = [2,3,4,5]
    tablas = [i+2 for i in range(len(tablas_chk)) if tablas_chk[i] is True]
    #print(tablas)
    try:
        if repaso:
            #print("El numero de errores es: ", numero_errores())
            num = numero_errores()
        else:
            num = int(total.text)
        #print("numero de multiplicaciones: ", num)
    except:
        num = 0

    texto.text = ""
    mul = 1
    error = 0
    errores = 0
    while mul <= num:
        try:
            a, b = numeros_random(tablas, repaso)
            texto_multi.text = (f"{a}x{b}")
            #print(f"funcion multiplicar texto_mlti: {texto_multi} id: {id(texto_multi)}")
            
            multi.text = (f"Nº Multiplicaciones: {num}     Multiplicaciones: {mul}")
            #cmd = resultado.bind("<Return>",resultado.get())
            #cmd = int(resultado.get())
            fin_cuenta = False
            while not fin_cuenta:
                texto.text = ""
                #continuar(pasar)
                #print("semaforo rojo")
                semaforo.acquire()
                
                if int(resultado.text) == a * b:
                    #print("El resultado es: ", resultado.text)
                    #modificar_valor(f"{a}x{b}", True)
                    texto.text = "¡¡Bien!!"
                    sleep(1)
                    fin_cuenta = True
                    mul += 1
                    error = 0
                 
                else:
                    #modificar_valor(f"{a}x{b}", False)
                    path = os.getcwd()+ "\\AppMulti\\files\errores.txt"
                    escribir_fichero(f"{a}x{b}", path)
                    errores += 1
                    if error == 1:
                        texto.text = "Dejate de rollo y no la cagues más"
                        sleep(1)
                        error -= 1
                    else:
                        texto.text = f"Lo siento te has equivocado, intentalo otra vez"
                        sleep(1)
                        error += 1
                #pasar.set(False)
                #print("nueva multiplicacion")
                #resultado.hint_text = "Ingresar Valor"
        
                   
        except:
            texto.text = "Dejate de rollo y sigue multiplicando"
            sleep(1)
            pasar = False
            #resultado.hint_text = "Ingresar Valor"

    modificar_archivo()    
    #iniciar_total()

    if num > 0:
        texto_multi.text = f"Errores: {errores}"
        texto.text = f"Multiplicaciones: {num}"
    else:
        if not repaso:
            texto_multi.text = f"Introduce número de"
            texto.text =f"Multiplicaciones"
            multi.text = ""
        else:
            texto_multi.text = f"No existen errores"
            texto.text = f"para repasar"
            multi.text = ""
    
    sleep(3)
    texto_multi.text = f" "
    multi.text = "¿Preparad@ para repasar las tablas?"
    texto.text = f" "


def numeros_random(tablas, repaso):
    if not repaso:
        shuffle(tablas)
        a = tablas[randint(0, len(tablas)-1)]
        c= [i for i in range(2,10)]
        shuffle(c)
        b = c[randint(0, len(c)-1)]
    else:
        a, b = seleccionar_error()
    return a, b

def seleccionar_error():
    path = os.getcwd()+ "\\AppMulti\\files\errores.txt"
    #print("Buscando error en: ", path)
    file = open(path, "r")
    errores = file.read().split("//")[:-1]
    #print(errores)
    file.close()
    if len(errores) == 0:
        return "a", "b"
    else:
        nums = errores[0].split("x")
        #print(nums)
        a, b =  int(nums[0]), int(nums[1])
        file = open(path, "w")
        for i in errores[1:]:
            file.write(i+"//")
        file.close()
        return a, b

def escribir_fichero(string, path):
    file = open(path, "a")
    file.write(string+"//")
    file.close()

def modificar_archivo():
    path = os.getcwd()+ "\\AppMulti\\files\errores.txt"
    #print("error path: ", path)
    file = open(path, "r")
    errores_brutos = file.read().split("//")[:-1]
    errores_netos = {i for i in errores_brutos}
    file.close()
    file = open(path, "w")
    for i in errores_netos:
        file.write(i+"//")
    file.close()

def numero_errores():
    path = os.getcwd()+ "\\AppMulti\\files\errores.txt"
    file = open(path, "r")
    errores = file.read().split("//")[:-1]
    file.close()
    return len(errores)

#if __name__ == '__main__':
#    modificar_archivo()
