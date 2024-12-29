"""Crea una función que transforme grados Celsius en Fahrenheit
 y viceversa.
 - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
  y su unidad ("C" o "F").
 - En caso contrario retornará un error."""
 
def convertir_temperatura(temperatura: str) -> str:
    try:
        if "°C" in temperatura:
            return str(round((float(temperatura[:-2]) * 9 / 5) + 32, 2)) + "°F"
        elif "°F" in temperatura:
            return str(round((float(temperatura[:-2]) - 32) * 5 / 9, 2)) + "°C"
        else:
            return "Error"
    except:
        return "Error"

print(convertir_temperatura("0°C"))
print(convertir_temperatura("0°"))
print(convertir_temperatura("0°F"))