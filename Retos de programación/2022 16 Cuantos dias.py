"""Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción."""

from datetime import datetime

def count_days (str1, str2):
    try:
        dat1 = datetime.strptime(str1, "%d/%m/%Y")
        dat2 = datetime.strptime(str2, "%d/%m/%Y")
        days_dif = abs(dat1 - dat2)
        
        return (days_dif.days)

    except ValueError:
        print("El formato de la fecha no es correcto, debe ser dd/mm/yyyy")
               
print(count_days("1/10/2024", "1/10/2025"))