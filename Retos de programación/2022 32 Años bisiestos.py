"""Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio."""


def bisiesto(year: int):
    n = 0
    bis = False
    if year >= 1582:
        while n != 30:
            if year % 4 == 0 and year % 100 != 0:
                bis = True
            elif year % 100 == 0 and year % 400 != 0:
                bis = False
            elif year % 4 == 0 and year % 400 == 0:
                bis = True
            if bis == True:
                print(n + 1,"-", year)
                n += 1
            year += 1
            bis = False
    else:
        while n != 30:
            if year % 4 == 0:
                print(n + 1,"-", year)
                n += 1
            year += 1
    return(None)

bisiesto(1540)