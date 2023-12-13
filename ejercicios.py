"""funcion que define si es numero par o impar"""


def even_or_odd(num):
    """funcion que define si es numero par o impar"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


a = 2

print(even_or_odd(a))
