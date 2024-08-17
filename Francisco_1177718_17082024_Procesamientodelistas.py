"""
doble(lista). Debe retornar una lista con la multiplicación de cada valor por dos, es decir, una lista con el doble de cada elemento. Ejemplo de uso y resultado esperado: 

doble([1, 1, 2, 3, 5]) → [2, 2, 4, 6, 10] 
"""

def doble(lista): #Creamos la funcion "doble"
    listaX2 = []
    for i in range(len(lista)):
        listaX2.append(lista[i] * 2) #Agreamos los valores de la lista original multiplicados por 2 a la lista nueva
    print("doble(",lista,")", " -> ", listaX2)

listaEjA = [1,1,2,3,5]
doble(listaEjA) #Llamamos a la funcion pasandole como parametro la lista original

"""
cantidadEntre(lista, desde, hasta). Retorna la cantidad de valores que se encuentran en la lista, de acuerdo con el rango de parámetros recibidos (desde y hasta; inclusive ambos). Ejemplo de uso y resultado esperado: 

cantidadEntre([1, 1, 2, 3, 5], 3, 11) → 2 
"""

def cantidadEntre(lista, desde, hasta):
    contador = 0 #Creamos un contador
    for i in range(len(lista)): #Iteramos sobre todos los elementos de la lista
        if desde <= lista[i] and lista[i] <= hasta: #Con la condicion de que el valor de i este entre "desde" y "hasta" sumamos 1 al contador
            contador += 1
    print("cantidadEntre(",lista,",",desde,",",hasta,")", " -> ",contador)

listaEjB = [1,1,2,3,5]
cantidadEntre(listaEjB,3,11)

"""
cantidadNegativos(lista). Retorna la cantidad de valores negativos existentes en la lista. Ejemplo de uso y resultado esperado: 

cantidadNegativos([1, 1, 2, 3, 5]) → 0 
"""

def cantidadNegativos(lista):
    contador = 0 #Inicializamos un contador en 0
    for i in range(len(lista)):
        if lista[i] < 0: #Si el valor de la lista sobre el q se esta iterando es menor a 0 sumamos 1 al contador
            contador += 1
    print("cantidadNegativos(",listaEjC,")", " -> ",contador)

listaEjC = [1,1,2,3,5]
cantidadNegativos(listaEjC)

"""
promedio(lista). Debe imprimir (no retornar) en pantalla el contenido de toda la lista y, al final, el promedio de valores de esta. No utilice funciones de agregación para obtener el resultado del promedio. Ejemplo de uso y resultado esperado: 

promedio([1, 1, 2, 3, 5]) → 

0 → 1 

1 → 1 

2 → 2 

3 → 3 

4 → 5 

Promedio:  2.4 
"""

def promedio(lista):
    x = 0
    for i in range(len(lista)):
        print(x, " -> ", lista[i]) #Imprimimos por pantalla los valores de la lista con su respectiva posicion
        x+=1

    contador = 0
    totalLista = 0
    for j in range(len(lista)):
        totalLista += lista[j] #Sumamos el valor sobre el que se esta iterando a un sumador
        contador += 1 #Sumamor 1 al contador
    prom = totalLista / contador #Dividimos el total con el contador para obtener el promedio
    print("Promedio: ", prom)

listaEjD = [1,1,2,3,5]
promedio(listaEjD)
