from ecc_class import Point

def sqr_mul(scalar, G):
    bin_scalar = bin(scalar)[2:]

    result = Point(0, 0)
    for i in bin_scalar:
        result = result + result
        if i == "1":
            result = result + G

    return result
