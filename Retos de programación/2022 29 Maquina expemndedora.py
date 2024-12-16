"""Simula el funcionamiento de una máquina expendedora creando una operación
 que reciba dinero (array de monedas) y un número que indique la selección
 del producto.
 - El programa retornará el nombre del producto y un array con el dinero
   de vuelta (con el menor número de monedas).
 - Si el dinero es insuficiente o el número de producto no existe,
   deberá indicarse con un mensaje y retornar todas las monedas.
 - Si no hay dinero de vuelta, el array se retornará vacío.
 - Para que resulte más simple, trabajaremos en céntimos con monedas
   de 5, 10, 50, 100 y 200.
 - Debemos controlar que las monedas enviadas estén dentro de las soportadas."""
 
# Genero un dict con los productos que contiene la maquina
product_machin = {
    "1": 50,"2": 10,"3": 200,"4": 5,"5": 100,
    "6": 50,"7": 10,"8": 200,"9": 100,"10": 5,
    "11": 50,"12": 200,"13": 5,"14": 10,"15": 100,
    "16": 50,"17": 5,"18": 200,"19": 10,"20": 100
}
money = 0
# Leo las monedas que introduce el cliente
coins_str = input("Introduce las monedas separando cada una por una coma: ")
# Tras leer el str de monedas las separo, paso a int y ordeno
coins = coins_str.split(",")
for i in range(0,len(coins)):
    coins[i] = int(coins[i])
    money += coins[i]# Sumo ya todas las monedas
coins.sort()
print(coins)
# Comprobar que la moneda esta permitida
"""coins_set = set(coins)
for i in coins_set:
    if i != (5,10,50,100,200):
        print("La moneda introducida no es valida")"""
# Leo que producto quiere el cliente
product = input("Escribe el numero del producto que quieres: ")
# Compruebo que el dinero es suficiente y que existe el producto
if product not in product_machin:
    print("Producto inexistente")
    print(coins)
elif money - product_machin[product] < 0:
    print("Dinero insuficiente")
    print(coins)
else: # El producto existe y hay dinero
    cambio_int = money - product_machin[product]
    print(cambio_int)
    cambio = list()
    while cambio_int > 5:
        if cambio_int > 200:
            cambio.append(200)
            cambio_int -= 200
        elif cambio_int < 200 and cambio_int > 100:
            cambio.append(100)
            cambio_int -= 100
        elif cambio_int < 100 and cambio_int > 50:
            cambio.append(50)
            cambio_int -= 50
        elif cambio_int < 50 and cambio_int > 10:
            cambio.append(10)
            cambio_int -= 10
    if cambio_int > 0:
            cambio.append(5)
            cambio_int -= 5
    cambio.sort()
    print(cambio)
    print("Gracias por su compra")