"Listas"

lista = [] #Creo una lista vacía
lista = [1, 2, 3, 4, 5] #Creo una lista con elementos
lista = [1, 2, 3, 4, 5, "hola", "mundo"] #Creo una lista con elementos de diferentes tipos
lista = [1, 2, 3, 4, 5, "hola", "mundo", [1, 2, 3, 4, 5]] #Creo una lista con elementos de diferentes tipos y una lista anidada

lista.append() #Agrego un elemento al final de la lista
lista.pop() #Elimino el último elemento de la lista
lista.pop(0) #Elimino el elemento en la posición 0 de la lista
lista.remove(3) #Elimino el elemento 3 de la lista
lista.clear() #Elimino todos los elementos de la lista
lista.count(3) #Cuento cuántas veces aparece el elemento 3 en la lista
lista.index(3) #Devuelve la posición del elemento 3 en la lista
lista.reverse() #Invierte el orden de los elementos de la lista
lista.sort() #Ordena los elementos de la lista
lista.copy() #Devuelve una copia de la lista
lista.extend() #Extiende la lista con los elementos de otra lista
lista.insert(2, 3) #Inserta el elemento 3 en la posición 2 de la lista

"Listas por comprensión"

lista = [i for i in range(10)] #Creo una lista con los números del 0 al 9
lista = [i for i in range(10) if i % 2 == 0] #Creo una lista con los números pares del 0 al 9
lista = [i ** 2 for i in range(10)] #Creo una lista con los cuadrados de los números del 0 al 9
lista = [i ** 2 for i in range(10) if i % 2 == 0] #Creo una lista con los cuadrados de los números pares del 0 al 9

"Listas anidadas"

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Creo una lista con listas anidadas
lista[0] #Devuelve la primera lista anidada
lista[0][0] #Devuelve el primer elemento de la primera lista anidada
lista[0].append(4) #Agrego un elemento al final de la primera lista anidada
lista[0].pop() #Elimino el último elemento de la primera lista anidada
lista[0].pop(0) #Elimino el elemento en la posición 0 de la primera lista anidada
lista[0].remove(3) #Elimino el elemento 3 de la primera lista anidada
lista[0].clear() #Elimino todos los elementos de la primera lista anidada
lista[0].count(3) #Cuento cuántas veces aparece el elemento 3 en la primera lista anidada
lista[0].index(3) #Devuelve la posición del elemento 3 en la primera lista anidada
lista[0].reverse() #Invierte el orden de los elementos de la primera lista anidada
lista[0].sort() #Ordena los elementos de la primera lista anidada
lista[0].copy() #Devuelve una copia de la primera lista anidada
lista[0].extend() #Extiende la primera lista anidada con los elementos de otra lista

"Listas por comprensión anidadas"

lista = [[i for i in range(3)] for j in range(3)] #Creo una lista con listas anidadas con los números del 0 al 2
lista = [[i for i in range(3)] for j in range(3) if j % 2 == 0] #Creo una lista con listas anidadas con los números del 0 al 2 en las posiciones pares

frutas = ["manzana", "pera", "banana"]

if "manzana" in frutas: #Verifico si la manzana está en la lista de frutas
    print("La manzana está en la lista de frutas")
else: print("La manzana no está en la lista de frutas")

if "manzana" not in frutas: #Verifico si la manzana no está en la lista de frutas
    print("La manzana no está en la lista de frutas")
else: print("La manzana está en la lista de frutas")

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"Funciones"

def areaTriangulo(base, altura): #Defino una función que calcula el área de un triángulo
    resultado = base * altura / 2
    return resultado

area = areaTriangulo(10, 2) #Llamo a la función con los valores 3 y 4
print("El area es: ", area) #Imprimo el resultado de la función
print("El area es: ", areaTriangulo(10, 2)) #Imprimo el resultado de la función