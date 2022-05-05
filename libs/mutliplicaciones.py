from random import randint

def multiplicar(numeros):
    numeros, matriz, num_col, num_fil = devolver_datos(numeros)
    numeros = [devolver_numero(numero, num_col) for numero in numeros]
    numeros = convertir_numeros(numeros)
    lista = devolver_lista(numeros)
    matriz = devolver_matriz(num_fil, num_col, lista, matriz)
    matriz, num_fil = incluir_por(matriz, num_fil, num_col)
    #imprimir_resultado(matriz, num_fil)

    return matriz, num_col, num_fil

def incluir_por(matriz,num_fil, num_col):
    fila = ['-' for i in range(0,num_col)]
    digito = 0
    fin = False
    while digito < num_col and not fin:
        if matriz[1][digito] != '-':
            matriz[1][digito-1] = 'x'
            fin = True
        digito += 1
    
    matriz.insert(2, fila)
    matriz.insert(num_fil, fila)
    matriz.insert(0, fila)
    return matriz, num_fil+3

def  devolver_matriz(num_fil, num_col, lista, matriz):
    for i in range(0,num_fil):
        for j in range(0,num_col):
            matriz[i][j] = lista.pop()
    return matriz

def convertir_numeros(numeros):
    for i in range(3,len(numeros)-1):
        numeros[i] = numeros[i][i-2::] + "-" * (i-2)
    return numeros

def devolver_lista(numeros):
    texto = ""
    for numero in numeros:
        texto += numero
    lista = list(texto)[::-1]
    return lista

def devolver_numero(num,max):
    return "-" * (max - len(num)) + num

def devolver_datos(numeros):
    for numero in str(numeros[1])[::-1]:
        numeros.append(int(numero) *  numeros[0])
    numeros.append(numeros[0]*numeros[1])
    #print(numeros)
    numeros = [str(num) for num in numeros]
    num_col = 8
    num_fil = len(numeros)
    matriz = [[None] * num_col for i in range(num_fil)]
    return numeros, matriz, num_col, num_fil   


def devolver_factores(digitos_multiplicando, digitos_multiplicador):
    maximo = [2, 9, 99, 999, 9999]
    multiplicando = randint(2, maximo[digitos_multiplicando])
    multiplicador = randint( maximo[digitos_multiplicador -1], maximo[digitos_multiplicador])
    return [multiplicando, multiplicador]

def imprimir_resultado(matriz, num_fil):
    j = 0
    print("Resultado:\n")
    for fila in matriz:
        print(f"  {fila}")
        j += 1

# if __name__ == '__main__':
#     #maximo 4
#     digitos_multiplicando = 4
#     #maximo 3
#     digitos_multipplicador = 1
#     numeros = devolver_factores(digitos_multiplicando, digitos_multipplicador)
#     multiplicar(numeros)