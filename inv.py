def inv(p, d):
    d = d % p
    x, y = egcd(p, d)
    return y % p

def egcd(p, d):
    if d == 1:
        return 0, 1
    x, y = egcd(d, p % d)
    return y, x - (p // d) * y