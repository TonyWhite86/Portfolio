"""Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
 La función recibirá por parámetro sólo UN polígono a la vez.
 Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 Imprime el cálculo del área de un polígono de cada tipo."""

def calcular_area(tipo, *dimensiones):
    if tipo == "triangulo":
        base, altura = dimensiones
        area = (base * altura) / 2
        print(f"El área del triángulo es {area}")
    elif tipo == "rectangulo":
        largo, ancho = dimensiones
        area = largo * ancho
        print(f"El área del rectángulo es {area}")
    elif tipo == "cuadrado":
        lado, = dimensiones
        area = lado * lado
        print(f"El área del cuadrado es {area}")
    else:
        print("Tipo de polígono no soportado.")
        area = None
    return area

calcular_area("triangulo", 10.0, 5.0)
calcular_area("rectangulo", 5.0, 7.0)
calcular_area("cuadrado", 4.0)