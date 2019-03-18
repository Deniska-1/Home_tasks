class Vector(list):

    def __init__(self, *args, val = None):
        self.val = val or []
        for i in args:
            self.val.append(i)

    def __eq__(self, vector2):
        return self.val == vector2.val

    def __sub__(self, vector2):
        arg = []
        if len(self.val) == len(vector2.val):
            for i, j in [(self.val[x], vector2.val[y]) for x in range(len(self.val)) for y in range(len(self.val)) if x == y]:
                arg.append(i - j)
        else:
            print('Vectors have different lengths!')
            return False
        return Vector(*arg)

    def __add__(self, vector2):
        arg = []
        if len(self.val) == len(vector2.val):
            for i, j in zip(self.val, vector2.val):
                arg.append(i + j)
        else:
            print('Vectors have different lengths!')
            return False
        return Vector(*arg)

    def __mul__(self, number):
        arg = []
        for i in self.val:
            arg.append(i * number)
        return Vector(*arg)


v1 = Vector(2,3)
v2 = Vector(1,3)
print(v1 == v2)
v3 = v1 - v2
print(v3.val)
v4 = v1 + v2
print(v4.val)
v5 = v1 * 2
print(v5.val)