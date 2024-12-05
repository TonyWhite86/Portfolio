"""Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente."""
import re

input_text = input("Pasa el texto que quieras: ")
input_word = input("Dame la palabra que quieres contar: ")
list_text = []

input_text = input_text.lower()
input_word = input_word.lower()

input_text = re.sub(r"[^a-zA-Z0-9]", " ", input_text)
list_text = input_text.split()
print(list_text.count(input_word))
