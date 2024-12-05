"""Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva."""

def fact(num):
    if num == 0 or num == 1:
        return(1)
    else:
        return num * fact(num - 1)

print(fact(5))