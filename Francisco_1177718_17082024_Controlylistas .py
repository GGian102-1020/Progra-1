"""
Crear un programa que combine dos listas en un recorrido sucesivo de sus índices en una tercera. En caso de que una de las listas tenga más elementos que la otra, dichos elementos se deben sumar al final de la nueva lista. Ejemplo:     

Lista1 = ["Hola", "nombre", "Oliver", "García"] 

Lista2 = ["mi", "es"] 

Resultado esperado: Lista resultado: ['Hola', 'mi', 'nombre', 'es', 'Oliver', 'García'] 
"""
#Creamos las 2 listas que nos solicitan por enunciado
lista1 = ["Hola", "nombre", "Oliver", "García"] 

lista2 = ["mi", "es"]

lista3 = [] #Creamos una tercera lista vacia donde vamos a combinar las listas

lenListas = len(lista1) + len(lista2) #Creamos una variable para saber el len() de ambas listas

for i in range(lenListas): #itermos sobre la cantidad total de las listas combinadas
    #Si el valor de i esta dentro del len() de cada lista, agreamos esos valores a la lista vacia
    if i < len(lista1):
        lista3.append(lista1[i]) 
    if i < len(lista2):
        lista3.append(lista2[i])

print("Lista resultado:",lista3) #Imprimimos la lista combinada

print(not (3!=3))