"""Crea una función que ordene y retorne una matriz de números.
 - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
  o de mayor a menor."""
  
def orden(input_list: list, direction: str):
    if direction == "Asc":
        modi_list = input_list.sort()
      
    elif direction == "Des":
        modi_list = input_list.sort(reverse = True)
      
    return(input_list)

print(orden([2,1,3,5,7,4], "Des"))