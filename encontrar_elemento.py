def encontrarPalabra(lista):
    for i in lista:
        if i == "palabra":
            return "Encontre la palabra en la posicion " + str(lista.index(i))


a = ["we", "werewr", "palabra"]

print(encontrarPalabra(a))


def encontrarPalabra2(lista):
    return f'Encontre la palabra en la posicion {lista.index("needle")}'
