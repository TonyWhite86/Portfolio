"""Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos."""

def time_conver(dia: int, hora: int, minu: int, seg: int):
    dia = dia*(24*60*60*1000)
    hora = hora*60*60*1000
    minu = minu*60*1000
    seg = seg*1000
    milis = dia + hora + minu + seg
    return(milis)

print(time_conver(1,1,1,1))