"""Funcion del juego de piedra papel o tijera"""


def rps(p1, p2):
    if (
        (p1 == "tijera" and p2 == "papel")
        or (p1 == "papel" and p2 == "piedra")
        or (p1 == "piedra" and p2 == "scissors")
    ):
        return "Jugador 1 gano!"
    elif (
        (p2 == "tijera" and p1 == "papel")
        or (p2 == "papel" and p1 == "piedra")
        or (p2 == "piedra" and p1 == "tijera")
    ):
        return "Jugador 2 Gano!"
    else:
        return "Empate! Intentelo otra vez"


def rps2(p1, p2):
    mano = {"roca": 0, "papel": 1, "tijera": 2}
    resultado = ["Empate!", "Jugador 1 gano!", "Jugadir 2 gano!"]
    return resultado[mano[p1] - mano[p2]]


a = "tijera"
b = "papel"

print(rps(a, b))
