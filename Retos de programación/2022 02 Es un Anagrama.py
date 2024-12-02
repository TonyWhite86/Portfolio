"""Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama."""

def anagrama (word_1, word_2):
    if word_1 == word_2:
        return False
    else:
        list_1 = []
        list_2 = []
        for letter in word_1:
            list_1.append(letter)
        list_1.sort()
    
        for letter in word_2:
            list_2.append(letter)
        list_2.sort()

        return list_1 == list_2

input_1 = input("Escribe la primera palabla: ")
input_2 = input("Escribe la segunda palabla: ")

anagrama(input_1, input_2)
print(anagrama(input_1, input_2))
