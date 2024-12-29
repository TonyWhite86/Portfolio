"""Implementa uno de los algoritmos de ordenación más famosos:
 el "Quick Sort", creado por C.A.R. Hoare.
 - Entender el funcionamiento de los algoritmos más utilizados de la historia
   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
   donde trabajaremos y entenderemos los más famosos de la historia."""
   
def quick_sort(lista):
    # Caso lista con 0 o 1 elemento
    if len(lista) <= 1:
        return lista
    # Elijo el ultimo elemento como pivote
    pivote = lista[-1]
    # Divido la lista en dos partes
    menor = [x for x in lista[:-1] if x <= lista[-1]]
    mayor = [x for x in lista[:-1] if x > lista[-1]]
    # Llamo recursivamente a quick_sort con las dos partes
    return quick_sort(menor) + [pivote] + quick_sort(mayor)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))