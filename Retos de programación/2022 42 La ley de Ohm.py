"""Crea una función que calcule el valor del parámetro perdido
 correspondiente a la ley de Ohm.
 - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
   el valor del tercero (redondeado a 2 decimales).
 - Si los parámetros son incorrectos o insuficientes, la función retornará
   la cadena de texto "Invalid values"."""
   
def ley_ohm(V, R, I):
    try:
        if V == None:
            return round(R * I, 2)
        elif R == None:
            return round(V / I, 2)
        elif I == None:
            return round(V / R, 2)
        else:
            return ("Invalid values")
   
    except:
        return ("Invalid values")

print(ley_ohm(25,3,None))
print(ley_ohm("a",3,None))
print(ley_ohm(None,3,None))
print(ley_ohm(25,3,5))
print(ley_ohm(None,3,5))
print(ley_ohm(230,None,3.33))
