"""Escribe un programa que se encargue de comprobar si un número es o no primo.
  Hecho esto, imprime los números primos entre 1 y 100."""

num = input("Introduce el número para saber si es primo: ")
num = int(num)
prim = True

if num < 2:
    prim = True

for i in range(2, num-1):
    if num % i == 0:
        prim = False

if prim == True:
    print("El número es primo")
else:
    print("El número NO es primo")