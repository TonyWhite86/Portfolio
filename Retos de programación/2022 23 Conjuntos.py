"""Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente."""

def conj(array_1: list, array_2: list, bool_1: bool):
    set_1 = set(array_1)
    set_2 = set(array_2)
    re_array = set()
    if bool_1 == True:
        for x in set_1:
            if x in set_2:
                re_array.add(x)
    else:
        for y in set_1:
            if y not in set_2:
                re_array.add(y)
        for z in set_2:
            if z not in set_1:
                re_array.add(z)
    
    return(re_array)

print(conj([1,3,5,4,5,5,5,3], [2,2,2,3,3,5], False))