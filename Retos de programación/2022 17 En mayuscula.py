"""Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente."""

def change_cap(text):
    aux = str()
    text_list = list()
    for i in text:
        if i != " ":
            aux += i
        else:
            text_list.append(aux)
            aux = ""
    text_list.append(aux)
    aux = ""
    text_list_cap = list()     
    for x in text_list:
        text_list_cap.append(x.capitalize())
    for u in text_list_cap:
        aux += u + " "
    
    return(aux)

print(change_cap("hola como estas"))