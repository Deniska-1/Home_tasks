class Figure():

    def perimeter(self):
        per = 0
        if self._name == 'Circle':
            return 2 * 3.1415 * self.__dict__['radius']
        else:
            for i in self.__dict__.values():
                per += i
            return per

    def aria_of(self):
        """
        Для треугольника - формула Герона.
        Для трапеции - разница площадей подобных треугольников, с основаниеями на основаниях трапеции.
        """
        if self._name == 'Circle':
            return 3.1415 * self.__dict__['radius'] ** 2
        elif self._name == 'Triangle':
            first_side, second_side, third_side = self.__dict__.values()
            p = (first_side + second_side + third_side) / 2
            return (p * (p - first_side) * (p - second_side) * (p - third_side)) ** (1 / 2)
        elif self._name == 'Rectangle':
            height, base = self.__dict__['left_height'], self.__dict__['top_base']
            return height * base
        elif self._name == 'Square':
            return self.__dict__['left_height'] ** 2
        elif self._name == 'Trapezium':
            bottom_base = self.__dict__['bottom_base']
            top_base = self.__dict__['top_base']
            left_side = self.__dict__['left_side']
            right_side = self.__dict__['right_side']
            c1 = right_side / (1 - top_base / bottom_base)
            d1 = left_side / (1 - top_base / bottom_base)
            p1 = (d1 + c1 + bottom_base) / 2
            p = (d1 + c1 + top_base - left_side - right_side) / 2
            s1 = (p1 * (p1 - d1) * (p1 - c1) * (p1 - bottom_base)) ** (1 / 2)
            s = (p * (p - (d1 - left_side)) * (p - (c1 - right_side)) * (p - top_base)) ** (1 / 2)
            return s1 - s

    def volume(self):
        try:
            v = self.aria_of() * self.__dict__['height']
            return v
        except(Exception) as e:
            return [e, 'This is 2D-figure! This figure doesn\'t have volume!!!']


class Triangle(Figure):
    _name = 'Triangle'

    def __init__(self, first_side, second_side, third_side):
        lst = [
            [first_side > 0],
            [second_side > 0],
            [third_side > 0]
        ]
        lst1 = [
            [(first_side + second_side) > third_side],
            [(second_side + third_side) > first_side],
            [(third_side + first_side) > second_side]
            ]
        for i in lst:
            if not i[0]:
                raise ValueError("Impossible sides!!! Side of triangle must be more than 0!!!")
        for i in lst1:
            if not i[0]:
                raise ValueError("Impossible sides!!! Sum of two sides must be more than third side!!!")
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

class Rectangle(Figure):
    _name = 'Rectangle'

    def __init__(self, height, lengt):
        if height < 0 or lengt < 0:
            raise ValueError("Impossible sides!!! Side of rectangle must be more than 0!!!")
        self.left_height = height
        self.right_height = height
        self.top_base = lengt
        self.bottom_base = lengt


class Square(Figure):
    _name = 'Square'

    def __init__(self, side):
        if side < 0:
            raise ValueError("Impossible sides!!! Side of square must be more than 0!!!")
        self.left_height = side
        self.right_height = side
        self.top_base = side
        self.bottom_base = side


class Trapezium(Figure):
    _name = 'Trapezium'

    def __init__(self, top_base,  bottom_base, left_side, right_side):
        if top_base == bottom_base == left_side == right_side:
            raise ValueError("Impossible sides!!! The sides of trapezium must be different!!!")
        if top_base == bottom_base:
            raise ValueError("Impossible sides!!! Trapezium can't have the same bases!!!")
        lst = [
            [top_base + left_side != bottom_base + right_side],
            [bottom_base + left_side != top_base + right_side]
        ]
        for i in lst:
            if not i[0]:
                raise ValueError("Impossible sides!!! Sum of two sides (base + side) mustn't be the same!!!")
        lst1 = [
            [(left_side + right_side) > (bottom_base - top_base)],
            [((bottom_base - top_base) + left_side) > right_side],
            [((bottom_base - top_base) + right_side) > left_side]
        ]
        for i in lst1:
            if not i[0]:
                raise ValueError("Impossible sides!!! Sides of trapezium aren't closed curve!!!")
        self.left_side = left_side
        self.right_side = right_side
        self.top_base = top_base
        self.bottom_base = bottom_base


class Circle(Figure):
    _name = 'Circle'

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Impossible radius!!! It must be more than 0!!!")
        self.radius = radius



a = Triangle(4, 5, 6)
print(a.perimeter())
b = Rectangle(4, 5)
print(b.perimeter())
c = Square(5)
print(c.perimeter())
d = Trapezium(4, 5, 10, 10.8)
print(d.perimeter())
e = Circle(5)
print(e.perimeter())
print(a.aria_of(), b.aria_of(), c.aria_of(), d.aria_of(), e.aria_of(), sep='      ')
print(a.volume())
print(b.volume())
print(c.volume())
print(d.volume())
print(e.volume())