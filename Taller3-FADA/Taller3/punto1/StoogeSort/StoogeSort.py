import random

def stoogesort(arr, s, e):
    if s >= e: # Condicion de parada, si el indice de inicio es igual o mayor al del final
        return

    if arr[s]>arr[e]:
        t = arr[s]
        arr[s] = arr[e]
        arr[e] = t

# If there are more than 2 elements in
# the array
    if e-s+1 > 2:
        t = int((e - s + 1) / 3)

# Recursively sort first 2/3 elements
        stoogesort(arr, s, (e-t))

# Recursively sort last 2/3 elements
        stoogesort(arr, s + t, e)

# Recursively sort first 2/3 elements
# again to confirm
        stoogesort(arr, s, (e-t))



arr = [2, 4, 5, 3, 1]
n = len(arr)

stoogesort(arr, 0, n-1)

for i in range(0, n):
    print(arr[i], end = ' ')


