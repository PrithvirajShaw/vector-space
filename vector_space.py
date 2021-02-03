class v_R2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x2 = self.x + 2 * other.x
        y2 = self.y + 2 * other.y
        return x2, y2

    def __mul__(self, other):
        x2 = 2 * self.x * other
        y2 = 2 * self.y * other
        return x2, y2

    def __str__(self):
        print(f"({x}, {y})")


s1 = v_R2(3, 2)
s2 = v_R2(4, 5)

print(s1+s2)
print(s1*2)