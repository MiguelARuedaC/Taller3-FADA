import random


def stoogesort(arr, s, e):
    if s >= e:  # Condicion de parada, si el indice de inicio es igual o mayor al del final.
        return

    if arr[s] > arr[e]:  # Aqui ocurre el cambio de posicion en caso de que el menor este al lado derecho del mayor.
        t = arr[s]  # La variable t se queda con el valor mayor, osea el que esta en la posicion s.
        arr[s] = arr[e]  # A la posicion s que esta a la izquierda, se le asigna el valor que tiene a la derecha.
        arr[e] = t  # En la posicion e se guarda lo que tenia la variable temporal t.


    if e - s + 1 > 2:  #  Verifica si el array tiene mas de dos elementos
        t = int((e - s + 1) / 3)  # Se le asigna un valor a t, el cual es el valor de 1/3 del segmento

        stoogesort(arr, s, (e-t))  # Recursion para ordenar los primeros 2/3 de segmento
        stoogesort(arr, s + t, e)  # Recursion para ordenar los ultimos 2/3 de segmento
        stoogesort(arr, s, (e-t))  # Repetimos la recursion inicial para organizar de nuevo los primeros 2/3, es necesario porque con el paso
                                   # anterior, pudo haber cambiado el segundo sector.



arr = []  # definicion del arreglo
# n = 0 # Tamaño del arreglo
# n = 10
n = 100
# n = 1000
for i in range(n):  # Darle valores aleatorios al arreglo.
    arr.append(random.randint(0, 100))

stoogesort(arr, 0, n-1)  # Valores con los que va a trabajar el stoogesort

for i in range(0, n):
    print(arr[i], end=' ')  # Impresion de resultados


