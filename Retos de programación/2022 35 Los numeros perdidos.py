"""Dado un array de enteros ordenado y sin repetidos,
 crea una función que calcule y retorne todos los que faltan entre
 el mayor y el menor.
 - Lanza un error si el array de entrada no es correcto."""
 
def num_lost(arr: list) -> list:
    lost = list()
    first_num = arr[0]
    last_num = arr[-1]
    set_arr = set(arr)
    set_full = set(range(first_num, last_num + 1))
    if len(arr) != len(set_arr):
        return("Array con valores repetidos")
    if arr != sorted(arr):
        return("Array no ordenado")
    lost = list(set_full - set_arr)
    
    return(lost)

print(num_lost([2, 2, 6, 8, 9, 10])) # [11]