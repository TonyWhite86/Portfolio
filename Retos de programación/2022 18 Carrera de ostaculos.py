"""Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
- Un array que sólo puede contener String con las palabras "run" o "jump"
- Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
- Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
- Si hace "jump" en "_" (suelo), se variará la pista por "x".
- Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista."""

def race(action, track):
    track_list = list()
    finish = False
    finish_list = list()
    for i in track:
        track_list.append(i)

    if len(track_list) != len(action):
        print("Los movimientos no concuerdan con la pista")  
    else:
        for ind , x in enumerate(action):
            if (x == "run" and track_list[ind] == "_") or (x == "jump" and track_list[ind] == "|"):
                finish_list.append(True)
            elif x == "run" and track_list[ind] == "|":
                finish_list.append(False)
                track_list[ind] = "/"
            elif x == "jump" and track_list[ind] == "_":
                finish_list.append(False)
                track_list[ind] = "x"
        if False in finish_list:
            finish = False
        else:
            finish = True        
    
    return (finish, action, track_list) #== track_end

print(race(["jump","run","run","run"], "|__|"))