from ecc_class import Point
from window_NAF import wNAF

def naf_mul(scalar, G):
    z = wNAF(2, scalar)

    result = Point(0, 0)

    for i in z:
        result = result + result
        if i == 1:
            result = result + G
        elif i == -1:
            result = result + G.neg()

    return result

# print(naf_mul(26, Point(5, 22)))