""""
Punto 2 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - (codigo)

"""

def encontrar_moda(arr):
    # Utilizar un diccionario para almacenar las frecuencias de los elementos
    frecuencias = {}

    # Contar las frecuencias en la lista
    for elemento in arr:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    # Encontrar la moda
    moda = encontrar_moda_recursiva(list(frecuencias.items()))

    return moda


def encontrar_moda_recursiva(frecuencias):
    # Caso base: si la lista de frecuencias tiene un solo elemento, ese es el modo
    if len(frecuencias) == 1:
        return [frecuencias[0][0]]

    medio = len(frecuencias) // 2
    izquierda = frecuencias[:medio]
    derecha = frecuencias[medio:]

    moda_izquierda = encontrar_moda_recursiva(izquierda)
    moda_derecha = encontrar_moda_recursiva(derecha)

    # Fusionar las modas de las sub-listas
    return fusionar_modas(moda_izquierda, moda_derecha)


def fusionar_modas(moda_izquierda, moda_derecha):
    # Fusionar las modas de dos listas
    moda = moda_izquierda.copy()
    for elemento in moda_derecha:
        if elemento not in moda:
            moda.append(elemento)

    return moda


# Ejemplos de uso
arreglo_a = [1, 1, 2, 3]
arreglo_b = [1, 1, 2, 2, 3, 4]

moda_a = encontrar_moda(arreglo_a)
moda_b = encontrar_moda(arreglo_b)

print("Moda de arreglo A:", moda_a)
print("Moda de arreglo B:", moda_b)
