from ecc_class import Point
from window_NAF import wNAF

def fixed_window_mul(w, scalar, G):
    z = bin(scalar)
    z = z[2:]

    start = len(z) - 1
    k = []
    while start >= 0:
        k_i = 0
        end = start - w + 1
        if end < 0:
            end = 0

        for i in range(start - end + 1):
            k_i *= 2
            k_i += int(z[end + i])

        k.insert(0, k_i)
        start = end - 1

    P_i = []
    P = G
    for i in range(len(k)):
        P_i.insert(0, P)
        for j in range(w):
            P = P + P

    result = Point(0, 0)
    Q = Point(0, 0)

    j = 2 ** w - 1
    while j > 0:
        for i in range(len(k)):
            if k[i] == j:
                Q = Q + P_i[i]
        result = result + Q
        j -= 1

    return result