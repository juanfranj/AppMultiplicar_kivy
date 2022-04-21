from random import randint

def suma(numeros):
    numeros, matriz, num_col, num_fil = devolver_datos(numeros)
    numeros = [devolver_numero(numero, num_col) for numero in numeros]
    lista = devolver_lista(numeros)
    matriz = devolver_matriz(num_fil, num_col, lista, matriz)
    restos = devolver_restos(matriz, num_col, num_fil)
    matriz = actualizar_matriz(restos, matriz)
    imprimir_pregunta(matriz, num_fil)
    imprimir_resultado(matriz, num_fil)

def imprimir_pregunta(matriz, num_fil):
    j = 0
    print("Calcular:\n")

    for fila in matriz[1:][:]:
        if j == (num_fil-3):
            print(f"+ {fila}")
            linea = "------" * len(fila) + "--"
            print(linea)
        elif j == (num_fil-2):
            print("")
        else:
            print(f"  {fila}")
        j += 1

def imprimir_resultado(matriz, num_fil):
    j = 0
    print("Resultado:\n")
    for fila in matriz:
        if j == (num_fil-2):
            print(f"+ {fila}")
            linea = "------" * len(fila) + "--"
            print(linea)
        else:
            print(f"  {fila}")
        j += 1

def actualizar_matriz(restos,matriz):
    for i in range(0, len(restos)):
        matriz[0][i] = restos[i]
    return matriz

def devolver_restos(matriz, num_col, num_fil):
    columnas = []
    restos = []
    for i in range(0,num_col):
        columna = [int(fila[i]) for fila in matriz[1::][:-1]]
        #print(columna)
        columnas.append(columna)
        restos.append(sum(columna))
    restos = actualizar_restos(restos[::-1])
    #print(restos)
    #print(columnas)
    return restos

def actualizar_restos(restos):
    #print(restos)
    resto_actualizado = ['-']
    for resto in restos:
        if len(str(resto)) > 1:
            resto_actualizado.append(str(resto)[0])
        else:
            resto_actualizado.append("-")
    #print(resto_actualizado)
    return resto_actualizado[::-1][1::]

def  devolver_matriz(num_fil, num_col, lista, matriz):
    for i in range(1,num_fil):
        for j in range(0,num_col):
            matriz[i][j] = lista.pop()
    return matriz

def devolver_datos(numeros):
    numeros.append(sum(numeros))
    numeros = [str(num) for num in numeros]
    num_col = max([len(str(digito)) for digito in numeros])
    num_fil = len(numeros)+1
    matriz = [[None] * num_col for i in range(num_fil)]
    return numeros, matriz, num_col, num_fil

def devolver_numero(num,max):
    return "0" * (max - len(num)) + num

def devolver_lista(numeros):
    texto = ""
    for numero in numeros:
        texto += numero
    lista = list(texto)[::-1]
    return lista

def devolver_sumandos(sumandos, digitos):
    maximo = [0, 9, 99, 999, 9999]
    numeros = [randint(1, maximo[digitos]) for i in range(sumandos)]
    return numeros

if __name__ == '__main__':
    # maximo 5
    sumandos = 2
    # maximo 4
    digitos = 3
    numeros = devolver_sumandos(sumandos, digitos)
    suma(numeros)
    