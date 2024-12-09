"""Escribe una función que calcule si un número dado es un número de Armstrong(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información al respecto."""

def num_armstrong (num):
    num_list = list()
    count = 0
    x = 0
    for i in num:
        num_list.append(i)
    
    while len(num) > x:
        count = count + pow(int(num_list[x]), len(num))
        x = x + 1
    
    return (int(num) == count)

print(num_armstrong("153"))