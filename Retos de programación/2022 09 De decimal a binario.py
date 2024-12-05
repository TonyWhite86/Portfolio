"""Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente."""

input_num = int(input("Escribe el número que quieres pasar a binario: "))
bin_num = ""

if input_num == 0:
    bin_num += "0"
while input_num >= 1:
    if input_num % 2 == 0:
        bin_num += "0"
        input_num = int(input_num / 2)
    else:
        bin_num += "1"
        input_num = int(input_num / 2)

str_inv = ""
lenght = len(bin_num) - 1

for i in range(0, lenght + 1):
    str_inv += bin_num[lenght - i]
        
print(str_inv)