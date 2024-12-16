"""Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente."""
from collections import Counter

def mcd(num_1: int, num_2: int):
    fact_1 = list()
    div = 2
    res_mcd = 1
    n_1 = num_1
    while n_1 > 1:
        while n_1 % div ==0:
            fact_1.append(div)
            n_1 //= div
        div += 1
    fact_2 = list()
    div = 2
    n_2 = num_2
    while n_2 > 1:
        while n_2 % div ==0:
            fact_2.append(div)
            n_2 //= div
        div += 1
        
    cont_1 = Counter(fact_1)
    cont_2 = Counter(fact_2)
    res_mcd_list = list((cont_1 & cont_2).elements())
    for i in res_mcd_list:
        res_mcd *= i
        
    return(res_mcd)

def mcm(num_1: int, num_2: int):
    fact_1 = list()
    div = 2
    res_mcm = 1
    n_1 = num_1
    while n_1 > 1:
        while n_1 % div ==0:
            fact_1.append(div)
            n_1 //= div
        div += 1
    fact_2 = list()
    div = 2
    n_2 = num_2
    while n_2 > 1:
        while n_2 % div ==0:
            fact_2.append(div)
            n_2 //= div
        div += 1
        
    cont_1 = Counter(fact_1)
    cont_2 = Counter(fact_2)
    res_mcm_list = list((cont_1 | cont_2).elements())
    for i in res_mcm_list:
        res_mcm *= i
    
    return(res_mcm)
    
print(mcd(48, 60))
print(mcm(72, 50))