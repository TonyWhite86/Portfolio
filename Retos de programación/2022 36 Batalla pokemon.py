"""Crea un programa que calcule el daño de un ataque durante
 una batalla Pokémon.
 - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
  (buscar su efectividad)
 - El programa recibe los siguientes parámetros:
 - Tipo del Pokémon atacante.
 - Tipo del Pokémon defensor.
 - Ataque: Entre 1 y 100.
 - Defensa: Entre 1 y 100."""

def battle(attacker: str, defender: str, attack: int, defense: int) -> float:
    effectiveness = {
        "Agua": {"Fuego": 2, "Planta": 0.5, "Eléctrico": 1}, # Efectividad de los tipos de pokémon
        "Fuego": {"Agua": 0.5, "Planta": 2, "Eléctrico": 1},
        "Planta": {"Agua": 2, "Fuego": 0.5, "Eléctrico": 1},
        "Eléctrico": {"Agua": 1, "Fuego": 1, "Planta": 1}
    }
    if attack > 100 or attack < 1 or defense > 100 or defense < 1: # Validación de los valores de ataque y defensa
        return "Los valores de ataque y defensa deben estar entre 1 y 100"
    if attacker not in effectiveness or defender not in effectiveness: # Validación de los tipos de pokémon
        return "Los tipos de pokémon son incorrectos"
    damage = 50 * (attack / defense) * effectiveness[attacker][defender] # Cálculo del daño
    return damage

print(battle("Agua", "Fuego", 80, 50))