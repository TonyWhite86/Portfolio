"""Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 indicándole únicamente el tamaño del lado.

 - Aquí puedes ver rápidamente cómo se calcula el triángulo:
   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif"""
   
import math

def generar_triangulo_pascal(lado: int):
    # Creo una lista para almacenar cada fila
    triangulo = []
    # Creo cada fila del triangulo
    for i in range(lado):
        # Relleno la fila con todo 1
        fila = [1] * (i + 1)
        # Cambio los valores centrales por la suma de el valor superior izquierdo y el superior derecho
        for j in range(1, i):
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    # Imprimo el triangulo
    raiz = int(math.sqrt(lado))
    for fila in triangulo:
        # Los valores de la fila los convierto a string y los uno con un espacio
        print(" ".join(map(str, fila)).center(lado * raiz + lado)) # Para centrar el triangulo (hecho a prueba y error)
    
lado = 16
generar_triangulo_pascal(lado)
