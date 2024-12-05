"""Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"""

input_str = input("Escribe el texto que quieres invertir: ")
str_inv = ""
lenght = len(input_str) - 1

for i in range(0, lenght + 1):
    str_inv += input_str[lenght - i]
        
print(str_inv)
  
    