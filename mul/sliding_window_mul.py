from ecc_class import Point
from window_NAF import wNAF

def sliding_window_mul(w, scalar, G):
    naf = wNAF(2, scalar)
    result = Point(0, 0)

    jump = G + G
    P = []
    tmp = G
    for i in range((2 ** w - (-1) ** w) // 3):
        P.append(tmp)
        tmp = tmp + jump

    i = 0
    while i < len(naf):
        t = 1
        u = 0
        if naf[i] != 0:
            t = w
            if i + t - 1 >= len(naf):
                t = len(naf) - i
            while naf[i + t - 1] == 0:
                t -= 1
            for j in range(t):
                u *= 2
                u += naf[i + j]

        for j in range(t):
            result = result + result

        if u > 0:
            result = result + P[(u - 1) // 2]
        elif u < 0:
            # P__i = Point(P[(-u - 1) // 2].x, -P[(-u - 1) // 2].y)
            P__i = P[(-u - 1) / 2].neg()
            result = result + P__i

        i += t

    return result
