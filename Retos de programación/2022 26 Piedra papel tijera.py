"""Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2"."""

def win(winner_list: list):
    player_1 = int()
    player_2 = int()
    reg = {
        "R": "S",
        "S": "P",
        "P": "R"
    }
    for i in winner_list:
        play_1, play_2 = i
        if reg[play_1] == play_2:
            player_1 += 1  
        elif reg[play_2] == play_1:
            player_2 += 1 
    if player_1 == player_2:
        winner = "Empate"
    elif player_1 > player_2:
        winner = "Player 1" 
    else:
        winner = "Player 2"
    print(player_1,player_2)
    return(winner)

print(win([("R","S"), ("S","R"), ("P","S")]))