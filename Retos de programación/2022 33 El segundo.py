"""Dado un listado de números, encuentra el SEGUNDO más grande"""

text = input("Introduce los numeros separados por comas: ")
text_list = text.split(",")
long = len(text_list)
text_list.sort()
print(text_list[long-2])