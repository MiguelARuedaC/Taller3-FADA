""""
Punto 2 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - (2159879)

"""

# Función principal para encontrar la moda de un arreglo
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
arreglo_a = [1, 1, 2, 3]
arreglo_b = [1, 1, 2, 2, 2, 3, 4, 4, 4]

# Llamar a la función para encontrar la moda de cada arreglo
moda_a = encontrar_moda(arreglo_a)
moda_b = encontrar_moda(arreglo_b)

# Imprimir los resultados
print("Moda de arreglo A:", moda_a)
print("Moda de arreglo B:", moda_b)


