"""Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra."""
 
shape = input("Dime la forma a dibujar: ")
length = int(input("Dime la longitud del lado: "))

if length < 2:
    print("El tamaño tiene que ser mayor a 1")

if shape == "cuadrado":
    for i in range(0, length):
        print("* " * length)

if shape == "triangulo":
    for i in range(1, length + 1):
        print("*" * i)
        
if shape == "equilatero":
    for i in range(1, length + 1):
        espacios = " " * (length - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)
    