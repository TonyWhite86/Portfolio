"""¡La Tierra Media está en guerra! En ella lucharán razas leales
 a Sauron contra otras bondadosas que no quieren que el mal reine
 sobre sus tierras.
 Cada raza tiene asociado un "valor" entre 1 y 5:
 - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
   Númenóreanos (4), Elfos (5)
 - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
   Huargos (3), Trolls (5)
 Crea un programa que calcule el resultado de la batalla entre
 los 2 tipos de ejércitos:
 - El resultado puede ser que gane el bien, el mal, o exista un empate.
   Dependiendo de la suma del valor del ejército y el número de integrantes.
 - Cada ejército puede estar compuesto por un número de integrantes variable
   de cada raza.
 - Tienes total libertad para modelar los datos del ejercicio.
 Ej: 1 Peloso pierde contra 1 Orco
     2 Pelosos empatan contra 1 Orco
     3 Pelosos ganan a 1 Orco"""
     
def battle(good: dict, evil: dict) -> str:
    # Definimos los valores de cada raza
    good_values = {"Pelosos": 1, "Sureños buenos": 2, "Enanos": 3, "Númenóreanos": 4, "Elfos": 5}
    evil_values = {"Sureños malos": 2, "Orcos": 2, "Goblins": 2, "Huargos": 3, "Trolls": 5}
    # Inicializamos las variables para almacenar el poder de cada ejército
    good_power = 0
    evil_power = 0
    # Calculamos el poder de cada ejército
    for trop , amount in good.items():
        if trop in good_values:
            good_power += good_values[trop] * amount
        else:
            print(f"La tropa '{trop}' no existe en el ejército del bien y no será considerada.")
    for trop , amount in evil.items():
        if trop in evil_values:
            evil_power += evil_values[trop] * amount
        else:
            print(f"La tropa '{trop}' no existe en el ejército del mal y no será considerada.")
    # Comparamos los poderes de cada ejército y damos un ganador
    if good_power > evil_power:
        return (f"El bien gana con un poder de {good_power} contra {evil_power}")
    elif good_power < evil_power:
        return (f"El mal gana con un poder de {evil_power} contra {good_power}")
    elif good_power == evil_power:
        return (f"Empate con un poder de {good_power} contra {evil_power}")
    
ejercito_bien = {"Pelosos": 9, "Enanos": 5, "Elfos": 5, "Númenóreanos": 8, "Sureños buenos": 1, "Hobbits": 2}
ejercito_mal = {"Orcos": 10, "Goblins": 15, "Huargos": 2, "Trolls": 3, "Sureños malos": 1, "Nazgûl": 2}

resultado = battle(ejercito_bien, ejercito_mal)
print(resultado)