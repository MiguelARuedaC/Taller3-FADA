""""
Punto 2 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - 2159879

"""

# Función principal para encontrar la moda de un arreglo
# Función principal para encontrar la moda de un arreglo
import random
import timeit

def encontrar_moda(arr):
    # Manejar caso base: arreglo vacío
    if not arr:
        return []

    # Contar las frecuencias de cada elemento en el arreglo
    frecuencias = contar_frecuencias(arr)
    # Obtener los elementos únicos del arreglo
    elementos = list(frecuencias.keys())
    # Llamar a la función iterativa para encontrar la moda
    return encontrar_moda_iterativa(elementos, frecuencias)

# Función para contar las frecuencias de los elementos en el arreglo
def contar_frecuencias(arr):
    frecuencias = {}
    for elemento in arr:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

# Función iterativa para encontrar la moda
def encontrar_moda_iterativa(elementos, frecuencias):
    moda = []  # Lista para almacenar la moda
    max_frecuencia = 0  # Variable para realizar un seguimiento de la frecuencia máxima

    # Iterar a través de los elementos únicos
    for valor in elementos:
        # Comparar la frecuencia del valor actual con la frecuencia máxima
        if frecuencias[valor] > max_frecuencia:
            # Si la frecuencia es mayor, actualizar la moda y la frecuencia máxima
            moda = [valor]
            max_frecuencia = frecuencias[valor]
        elif frecuencias[valor] == max_frecuencia:
            # Si la frecuencia es igual a la máxima, agregar el valor a la moda
            moda.append(valor)

    # Devolver la moda encontrada
    return moda

# Ejemplos de uso
#arreglo_a = [1, 1, 2, 3]
#arreglo_b = [1, 1, 2, 2, 2, 3, 4, 4, 4]


# Llamar a la función para encontrar la moda de cada arreglo
arreglo_aleatorioA = [random.randint(1, 100) for _ in range(10)]
arreglo_aleatorioB = [random.randint(1, 100) for _ in range(100)]
arreglo_aleatorioC = [random.randint(1, 100) for _ in range(1000)]
arreglo_aleatorioD = [random.randint(1, 100) for _ in range(10000)]

moda_A = encontrar_moda(arreglo_aleatorioA)
moda_B = encontrar_moda(arreglo_aleatorioB)
moda_C = encontrar_moda(arreglo_aleatorioC)
moda_D = encontrar_moda(arreglo_aleatorioD)


#Funcion para tomar el tiempo de culminación de ejecución
print(timeit.timeit(lambda: encontrar_moda(arreglo_aleatorioA), number=10))
print(timeit.timeit(lambda: encontrar_moda(arreglo_aleatorioB), number=10))
print(timeit.timeit(lambda: encontrar_moda(arreglo_aleatorioC), number=10))
print(timeit.timeit(lambda: encontrar_moda(arreglo_aleatorioD), number=10))




# Mostrar el arreglo generado
print("Arreglo Aleatorio de 5 Datos:", arreglo_aleatorioA)