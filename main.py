import random
from ecc_class import *
from inv import *
from sqr_mul import *

if __name__ == "__main__":
    if (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
        print("Wrong Elliptic Curve!")
        exit(-1)

    G = Point(5, 22)
    if G.val_check():
        print("Generator is {}".format(G.get_point()))
    else:
        print("Wrong Generator!")
        exit(-1)

    P = G
    point_list = []
    while True:
        point_list.append(P)
        if P.idt_check():
            break
        P = P + G
    
    n = len(point_list)
    print("order: {}".format(n))

    print("KEY GENERATING....")
    while True:
        d = random.randrange(1, n)
        print("private key : {}".format(d))
        sqr_P = sqr_mul(d, G)
        if sqr_P.idt_check():
            continue
        if sqr_P.val_check() is False:
            continue
        break

    P = sqr_P
    print("Your public key : {}"
          .format(sqr_P.get_point()))

    ## Elgamal Encryption
    # print("Elgamal Encryption example")
    # M = Point(10, 5)
    # print("Message is {}".format(M.get_point()))
    # k = random.randrange(1, p)
    # c_1 = sqr_mul(k, G)
    # c_2 = sqr_mul(k, P)
    # c_2.x += M.x
    # c_2.y += M.y
    #
    # c_3 = sqr_mul(d, c_1)
    # M_check = Point(c_2.x - c_3.x, c_2.y - c_3.y)
    # print("Message is " + M_check.get_point())