"""ARRAY"""


def sum_array(x):
    """Funcion que suma un array"""
    res = 0
    if x is None:
        return 0
    else:
        for i in range(len(x)):
            res += x[i]
        return res


def sum_array2(x):
    """Funcion que suma un array"""
    return sum(x)


a = []
print(sum_array2(a))
