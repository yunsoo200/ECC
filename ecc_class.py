from inv import inv

a = 4
b = 20
p = 29

class Point:
    #   무한원점: (0, 0)
    
    def __init__(self, x, y):
        #   점 생성 시 좌표에 반드시 mod p 연산 수행
        self.x = x % p
        self.y = y % p

    def get_point(self):
        return "({}, {})".format(self.x, self.y)

    #   타원곡선 위의 점인지 확인
    def val_check(self):
        val = (self.x ** 3 + a * self.x + b) % p
        if val == (self.y ** 2) % p:
            return True
        else:
            return False

    #   점이 무한원점인지 확인
    def idt_check(self):
        if self.x == 0:
            if self.y == 0:
                return True
        else:
            return False

    def neg(self):
        self.y = p - self.y
        return self

    def __add__(self, other):
        #   P + Q 에서 P or Q가 무한원점일 때, 다른 피연산자를 출력
        if self.idt_check():
            return other
        elif other.idt_check():
            return self

        #   doubling P
        if (self.x == other.x) and (self.y == other.y):
            # y좌표가 0일 경우, 접선이 y축과 평행 -> 접점이 존재하지 않음
            if self.y == 0:
                return Point(0, 0)

            m = (3 * self.x ** 2 + a) * inv(p, 2 * self.y)

            x = (m ** 2 - 2 * self.x) % p
            y = (m * (self.x - x) - self.y) % p

        #   addition P, Q
        else:
            # P와 Q의 x좌표가 같으면 연산결과는 무한원점
            if other.x == self.x:
                return Point(0, 0)

            m = (other.y - self.y) * inv(p, other.x - self.x)

            x = (m ** 2 - self.x - other.x) % p
            y = (m * (self.x - x) - self.y) % p

        result = Point(x, y)
        if result.val_check() is False:
            print("Wrong addition")
            exit(-1)
        return result