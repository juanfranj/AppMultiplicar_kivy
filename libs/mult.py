from time import sleep
from random import randint, shuffle
from bd.funcionesBD import *
import os
import threading


def continuar(pasar):
    while not pasar.get():
        #print("pasar: ", pasar.get())
        sleep(0.1)
    #print("Pasar Actualizado: ", pasar.get())

def comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas, repaso):
    t1 = threading.Thread(target =   multiplicar, args = (total,texto, resultado, pasar, texto_multi, mul, tablas, repaso), daemon = True)
    t1.start()

def multiplicar(total, texto, resultado, pasar, texto_multi, multi, tablas_chk, repaso):
    tab = tablas_chk
    #print(tablas_chk)
    #tablas = [2,3,4,5]
    tablas = [i+2 for i in range(len(tablas_chk)) if tablas_chk[i] is True]
    #print(tablas)
    try:
        if repaso:
            total.set(numero_errores())
        num = total.get()
    except:
        num = 0

    texto.set("")
    mul = 1
    error = 0
    errores = 0
    while mul <= num:
        try:
            a, b = numeros_random(tablas, repaso)
            texto_multi.set(f"{a}x{b}")
            multi.set(f"Multiplicaciones: {mul}")
            #cmd = resultado.bind("<Return>",resultado.get())
            #cmd = int(resultado.get())
            fin_cuenta = False
            while not fin_cuenta:
                texto.set("")
                continuar(pasar)
                if int(resultado.get()) == a * b:
                    modificar_valor(f"{a}x{b}", True)
                    texto.set("¡¡Bien!!")
                    sleep(1)
                    fin_cuenta = True
                    mul += 1
                    error = 0
                 
                else:
                    modificar_valor(f"{a}x{b}", False)
                    path = os.getcwd()+ "\\files\errores.txt"
                    escribir_fichero(f"{a}x{b}", path)
                    errores += 1
                    if error == 1:
                        texto.set("Dejate de rollo Carmen y no la cagues más")
                        sleep(1)
                        error -= 1
                    else:
                        texto.set(f"Lo siento te has equivocado, intentalo otra vez")
                        sleep(1)
                        error += 1
                pasar.set(False)
                resultado.set("")
        
                   
        except:
            texto.set("Dejate de rollo Carmen y sigue multiplicando")
            sleep(1)
            pasar.set(False)
            resultado.set("")

    modificar_archivo()    
    total.set("")
    if num > 0:
        texto_multi.set(f"Errores: {errores}")
        texto.set(f"Multiplicaciones: {num}")
    else:
        if not repaso:
            texto_multi.set(f"Introduce número de")
            texto.set(f"Multiplicaciones")
        else:
            texto_multi.set(f"No existen errores")
            texto.set(f"para repasar")
    
    sleep(4)
    texto_multi.set(f" ")
    texto.set("Hola Carmen, ¿preparada para repasar las tablas?")
    multi.set(f" ")


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
    path = os.getcwd()+ "\\files\errores.txt"
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

#if __name__ == '__main__':
#    modificar_archivo()
