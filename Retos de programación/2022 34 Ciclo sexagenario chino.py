"""Crea un función, que dado un año, indique el elemento 
 y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 - El ciclo sexagenario se corresponde con la combinación de los elementos
  madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
  conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
  (en este orden).
 - Cada elemento se repite dos años seguidos.
 - El último ciclo sexagenario comenzó en 1984 (Madera Rata)."""
 
def chinese_year(year: int) -> str:
    if year < 604:
        return("El ciclo sexagenario comenzo en en el año 604")
    else:
        elements = ['Madera', 'Fuego', 'Tierra', 'Metal', 'Agua']
        animals = ['Rata', 'Buey', 'Tigre', 'Conejo', 'Dragón', 'Serpiente', 
                    'Caballo', 'Oveja', 'Mono', 'Gallo', 'Perro', 'Cerdo']
        start_year = 1984 
        element = elements[(year - start_year) // 2 % 5] # Se divide entre 2 para que cada elemento se repita dos años seg
                                                        #se obtiene el resto de la div entre 5 para movernos dentro de elements que tiene 5 posiciones
        animal = animals[(year - start_year) % 12] # Se obtiene el resto de la div entre 12 para movernos dentro de animals que tiene 12 posiciones
    return f'{year}: {element}, {animal}'

print(chinese_year(1987))
