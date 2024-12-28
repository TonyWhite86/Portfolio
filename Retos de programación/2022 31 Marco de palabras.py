""" Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
 - ¿Qué te parece el reto? Se vería así:
   **********
   * ¿Qué   *
   * te     *
   * parece *
   * el     *
   * reto?  *
   **********"""
   
def marc(text: str):
    max_long = 0
    text_list = text.split(" ")
    for word in text_list:
        if len(word) > max_long:
            max_long = len(word)
        print(word)
    max_long += 4
    print("*" * max_long)
    for word in text_list:
        print("* " + word + " " * (max_long - 3 - len(word)) + "*")
    print("*" * max_long)
    return(text)

marc("¿Qué te parece el reto?")