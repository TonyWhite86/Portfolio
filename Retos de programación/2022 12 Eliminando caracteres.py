"""Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1."""

def delet_parameter (str1, str2):
    set1 = set()
    set2 = set()
    out1 = ""
    out2 = ""
    for char1 in str1:
        set1.update(char1)
    list1 = list(set1)
    list1.sort()
    
    for char2 in str2:
        set2.update(char2)
    list2 = list(set2)
    list2.sort()
    
    for char1 in str1:
        if not char1 in list2:
            out1 += char1
            
    for char2 in str2:
        if not char2 in list1:
            out2 += char2    

    return (out1, out2)

print(delet_parameter("Me gusta Java","Me gusta Kotlin"))