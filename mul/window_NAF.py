def wNAF(w, scalar):
    z = []
    mod = 2 ** w
    while scalar > 0:
        r = 0
        if scalar % 2 == 1:
            r = scalar % mod
            if r > mod / 2:
                r = r - mod

        z.insert(0, r)
        scalar -= r
        scalar //= 2
    return z

# sliding window method를 구현하기 위해
# 연습삼아 sliding window에서 사용하는 wNAF를 구현
"""
def sliding_wNAF(w, scalar):
    naf = wNAF(2, scalar)
    z = []

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
        i += t

        while t > 0:
            if t == 1:
                z.append(u)
                break
            z.append(0)
            t -= 1

    i = 0
    while z[i] == 0:
        i += 1
    z = z[i:]
    return z
"""