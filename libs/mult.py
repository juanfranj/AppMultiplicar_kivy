from importlib.resources import path
from time import sleep
from random import randint, shuffle
from bd.funcionesBD import *
import os
from threading import Thread




def comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas, repaso, semaforo, hilos):
    if len(hilos) == 0:
        #print("No existen hilos abiertos")
        t1 = Thread(target =   multiplicar, args = (total,texto, resultado, pasar, texto_multi, mul, tablas, repaso, semaforo, hilos), daemon = True)
        t1.start()
        hilos.append(t1)
    """ else:
        print(f"hay {len(hilos)} abiertos no se inicializa el nuevo")
        for hilo in hilos:
            if hilo.is_alive():
                print(f"El hilo {hilo.name} esta vivo")
            else:
                print(f"El hilo {hilo.name} NO esta vivo") """
   
    #t1.start()
    

def multiplicar(total, texto, resultado, pasar, texto_multi, multi, tablas_chk, repaso, semaforo, hilos):
    tab = tablas_chk
    tablas = [i+2 for i in range(len(tablas_chk)) if tablas_chk[i] is True]
    #print(tablas)
    try:
        if repaso:
            num = numero_errores()
        else:
            num = int(total.text)
            if len(tablas) == 0:
                num = 0
    except:
        num = 0

    texto.text = ""
    mul = 1
    error = 0
    errores = 0
    while mul <= num:
        try:
            a, b = numeros_random(tablas, repaso)
            #print(f"{a}x{b}")
            texto_multi.font_size = "80"
            texto_multi.text = (f"{a}x{b}")
            multi.text = (f"Totales: {num}     Realizadas: {mul}")
            fin_cuenta = False
            while not fin_cuenta:
                texto.text = ""
                semaforo.acquire()
                #print(f"Despues del semaforo, resultado: {resultado.text}, {type(resultado.text)}")
                if int(resultado.text) == a * b:
                    #print("El resultado es correcto: ", resultado.text)
                    modificar_valor(f"{a}x{b}", True)
                    texto.text = "¡¡Bien!!"
                    sleep(1)
                    fin_cuenta = True
                    mul += 1
                    error = 0
                 
                else:
                    #print("El resultado es erroneo: ", resultado.text)
                    modificar_valor(f"{a}x{b}", False)
                    path = os.getcwd()+ "\\files\errores.txt"
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
                   
        except:
            texto.text = "Dejate de rollo y sigue multiplicando"
            sleep(1)
            
    modificar_archivo()    
    texto_multi.font_size = "40"
    texto.font_size = "40"


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
    texto_multi.font_style = "H6"
    texto_multi.text = f" "
    multi.text = "¿Preparad@ para repasar las tablas?"
    texto.text = f" "
    hilos.pop()


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
    path = os.getcwd()+ "\\files\errores.txt"
    #print("Buscando error en: ", path)
    file = open(path, "r")
    errores = file.read().split("//")[:-1]
    #print(errores)
    file.close()
    if len(errores) == 0:
        return 3, 3
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
    path = os.getcwd()+ "\\files\errores.txt"
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
    path = os.getcwd()+ "\\files\errores.txt"
    file = open(path, "r")
    errores = file.read().split("//")[:-1]
    file.close()
    return len(errores)

