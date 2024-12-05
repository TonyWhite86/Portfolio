"""Crea un programa que sea capaz de transformar texto natural a código
 morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras 
o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
 https://es.wikipedia.org/wiki/Código_morse."""
 
text = input("Escribe el texto que quieras traducir: ")
is_text = False
trad = ""
trad_list = []
codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
    "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", " " : "  "
}
text = text.lower()
if any(char.isalpha() for char in text) or any(char.isdigit() for char in text):
    is_text = True

if is_text == True:
    for val in text:
        trad += codigo_morse[val]
        trad += " "   
    print(trad)
else:
    for val in text:
        if val != " ":
            trad += val
        else:
            trad_list.append(trad)
            trad = ""
    for i in trad_list:
        clave_encontrada = ""
        for clave, valor in codigo_morse.items():
            if valor == i:
                clave_encontrada = clave
                break
        trad += clave_encontrada
    print(trad)