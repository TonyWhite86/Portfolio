"""Crea un programa se encargue de transformar un número binario
 a decimal sin utilizar funciones propias del lenguaje que
 lo hagan directamente."""
 
bin = str(input("Introduce el numero en binario: "))
dec = 0
show = True
bin_list = list(bin)
pot = len(bin_list) - 1
for i in bin_list:
    if i != "0" and i != "1":
        print("El numero no es binario")
        show = False
    else:
        dec += int(i) * 2 ** pot
        pot -= 1
if show:   
    print(dec)