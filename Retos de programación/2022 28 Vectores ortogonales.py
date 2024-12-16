"""Crea un programa que determine si dos vectores son ortogonales.
 - Los dos array deben tener la misma longitud.
 - Cada vector se podría representar como un array. Ejemplo: [1, -2]"""
 
 
vect_1 = input("Escribe el primer vector separndo por comas: ")
vect_2 = input("Escribe el segundo vector separndo por comas: ")
vec_1 = vect_1.split(",")
vec_2 = vect_2.split(",")
prod_esc = 0

if len(vec_1) != len(vec_2):
    print("Los vectores tienen que tener la misma logitud")
else:
    for i in range(0,len(vec_1)):
        prod_esc += int(vec_1[i]) * int(vec_2[i])
        
    if prod_esc != 0:
        print("No son ortogonales")
    else:
        print("Si son ortogonales")
        
