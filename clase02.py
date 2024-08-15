"Matrices"

#Estructura de datos bidimensional que se puede representar como una lista de listas o como una lista de tuplas de la misma longitud. 
#Primero se define la cantidad de filas y luego la cantidad de columnas.
#Para acceder a un elemento de la matriz se debe indicar la fila y la columna correspondiente.
#Se puede acceder a las filas y columnas de la matriz utilizando listas por comprensión.
#Se pueden realizar operaciones con matrices como la suma, la resta, la multiplicación y la transposición.

matriz = [
    ["a","b","c","d"], 
    [1,2,3,4], 
    [5,6,7,8] 
    ]

print(matriz[0][3]) #Trae la D
print(matriz[1][2]) #Trae el 3
print(matriz[2][1]) #Trae el 6

"Recorrer una matriz"

for fila in range(0, len(matriz)):
    for columna in range(0, len(matriz[fila])):
        print(matriz[fila][columna])

matrizAlumnos = []

cantAlumnos = int(input("Ingrese la cantidad de alumnos: "))

for fila in range(0,cantAlumnos):
    alumno = []

    print("Ingrese los datos del alummno ", fila + 1)
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    legajo = int(input("Legajo: "))

    alumno.append(nombre)
    alumno.append(apellido)
    alumno.append(legajo)

    matrizAlumnos.append(alumno)

for fila in range(0, len(matrizAlumnos)):
    print("Datos del alumno ", fila + 1)
    print("Nombre: ", matrizAlumnos[fila][0],"Apellido: ", matrizAlumnos[fila][1], "Legajo: ", matrizAlumnos[fila][2])

