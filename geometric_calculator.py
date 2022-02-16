from pythonProject.geometric_initial_shape import *
from math import pi, sqrt, sin, radians


class Square(FlatShape):
    side: float

    title = 'Квадрат. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, side: float):
        super().__init__(side=side)

    @property
    def area(self):
        print(f'Площадь квадрата равна - ', end='')
        return self.side ** 2

    @property
    def perimeter(self):
        print(f'Периметр квадрата равен - ', end='')
        return self.side * 4


class Rectangle(FlatShape):
    length: float
    width: float

    title = 'Прямоугольник. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, length: float, width: float):
        super().__init__(length=length, width=width)

    @property
    def area(self):
        print(f'Площадь прямоугольника равна - ', end='')
        return self.length * self.width

    @property
    def perimeter(self):
        print(f'Периметр прямоугольника равен - ', end='')
        return (self.length + self.width) * 2


class Circle(FlatShape):
    radius: float

    title = 'Круг. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, radius: float):
        super().__init__(radius=radius)

    @property
    def area(self):
        print(f'Площадь круга равна - ', end='')
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        print(f'Длина окружности круга равна - ', end='')
        return self.radius * 2 * pi


class Triangle(FlatShape):
    side_1: float
    side_2: float
    side_3: float

    title = 'Треугольник. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, side_1: float, side_2: float, side_3: float):
        if side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3) and side_3 < (side_2 + side_1):
            super().__init__(side_1=side_1, side_2=side_2, side_3=side_3)
        else:
            print(f'Введите корректные данные сторон треугольника. Треугольник существует только тогда, когда '
                  f'сумма двух его сторон больше третьей. Требуется сравнить каждую сторону с суммой двух других.')

    @property
    def area(self):
        print(f'Площадь треугольника равна - ', end='')
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        h = (2 * sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))) / self.side_1
        return (self.side_1 * h) / 2

    @property
    def perimeter(self):
        print(f'Периметр треугольника равен - ', end='')
        return self.side_1 + self.side_2 + self.side_3


class Trapezoid(FlatShape):
    side_1: float
    side_2: float
    side_3: float
    side_4: float

    title = 'Трапеция. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, side_1: float, side_2: float, side_3: float, side_4: float):
        sides = sorted([side_1, side_2, side_3, side_4])
        b, a, c, d = sides[-1], sides[-2], sides[-3], sides[-4]
        if a < (b + c + d) and b < (a + c + d) and c < (a + b + d) and d < (a + b + c):
            super().__init__(side_1=side_1, side_2=side_2, side_3=side_3, side_4=side_4)
        else:
            print(f'Введите корректные данные сторон трапеции (четырехуголника). Для того, чтобы четырехугольник '
                  f'существовал, необходимо, чтобы длина одной из его сторон была меньше, чем сумма длин трех '
                  f'остальных сторон, иначе будет невозможно замкнуть периметр.')

    @property
    def area(self):
        sides = sorted([self.side_1, self.side_2, self.side_3, self.side_4])
        b, a, c, d = sides[-1], sides[-2], sides[-3], sides[-4]
        print(f'Площадь трапеции равна - ', end='')
        h = sqrt(c ** 2 - (1 / 4) * ((((c ** 2 - d ** 2) / (b - a)) + b - a) ** 2))
        return ((a + b) / 2) * h

    @property
    def perimeter(self):
        print(f'Периметр трапеции равен - ', end='')
        return self.side_1 + self.side_2 + self.side_3 + self.side_4


class Rhombus(Square):
    side: float

    title = 'Ромб. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "draw" - рисует фигуру.'

    def __init__(self, side: float, injection: float):
        if 0 < injection < 90 or 90 < injection < 180:
            super().__init__(side=side)
            self.injection = injection
        else:
            print(f'Введите размер угла у ромба. Угол может быть больше ноля и меньше 90 градусов или быть больше 90 '
                  f'и меньше 180 градусов.')

    @property
    def area(self):
        print(f'Площадь ромба равна - ', end='')
        return (self.side ** 2) * sin(radians(self.injection))

    @property
    def perimeter(self):
        print(f'Периметр ромба равен - ', end='')
        return self.side * 4


class Cube(VolumetricShape):
    side: float

    title = 'Куб. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, side: float):
        super().__init__(side=side)

    @property
    def area(self):
        print(f'Площадь куба равна - ', end='')
        return self.side ** 2 * 6

    @property
    def perimeter(self):
        print(f'Периметр куба равен - ', end='')
        return self.side * 12

    @property
    def volume(self):
        print(f'Объем куба равен - ', end='')
        return self.side ** 3


class Parallelepiped(VolumetricShape):
    length: float
    width: float
    height: float

    title = 'Параллелепипед. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, length: float, width: float, height: float):
        super().__init__(length=length, width=width, height=height)

    @property
    def area(self):
        print(f'Площадь параллелепипеда равна - ', end='')
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    @property
    def perimeter(self):
        print(f'Периметр параллелепипеда равен - ', end='')
        return 4 * self.length + 4 * self.width + 4 * self.height

    @property
    def volume(self):
        print(f'Объем параллелепипеда равен - ', end='')
        return self.length * self.width * self.height


class Sphere(VolumetricShape):
    radius: float

    title = 'Cфера. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, radius: float):
        super().__init__(radius=radius)

    @property
    def area(self):
        print(f'Площадь сферы равна - ', end='')
        return 4 * pi * (self.radius ** 2)

    @property
    def perimeter(self):
        print(f'Длина окружности сечения сферы равна - ', end='')
        return self.radius * 2 * pi

    @property
    def volume(self):
        print(f'Объем сферы равен - ', end='')
        return (4 / 3) * pi * (self.radius ** 3)


class Pyramid(VolumetricShape):
    side: float
    width: float

    title = 'Пирамида, правильная, с квадратом в основании. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, side: float, width: float):
        super().__init__(side=side, width=width)

    @property
    def area(self):
        print(f'Площадь поверхности пирамиды равна - ', end='')
        return self.side ** 2 + ((self.side * sqrt(self.width ** 2 - (self.side ** 2 / 4))) / 2)

    @property
    def perimeter(self):
        print(f'Периметр граней пирамиды равен - ', end='')
        return self.side * 4 + self.width * 4

    @property
    def volume(self):
        d = sqrt(self.side ** 2 + self.side ** 2) / 2
        h = sqrt(self.width ** 2 - d ** 2)
        print(f'Объем пирамиды равен - ', end='')
        return (1 / 3) * self.side ** 2 * h


class Cylinder(VolumetricShape):
    radius: float
    height: float

    title = 'Цилиндр. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, radius: float, height: float):
        super().__init__(radius=radius, height=height)

    @property
    def area(self):
        print(f'Площадь поверхности цилиндра равна - ', end='')
        return 2 * pi * self.radius * self.height + 2 * pi * (self.radius ** 2)

    @property
    def perimeter(self):
        print(f'Длина окружности сечения сферы равна - ', end='')
        return self.radius * 2 * pi

    @property
    def volume(self):
        print(f'Объем цилиндра равен - ', end='')
        return pi * (self.radius ** 2) * self.height


class Cone(VolumetricShape):
    radius: float
    generatrix: float

    title = 'Конус. Метод "area" высчитывает площадь, метод "perimeter" - периметр, "volume" - объем, "draw" - рисует фигуру.'

    def __init__(self, radius: float, generatrix: float):
        super().__init__(radius=radius, generatrix=generatrix)

    @property
    def area(self):
        print(f'Площадь поверхности конуса равна - ', end='')
        return (pi * self.radius * self.generatrix) + (pi * (self.radius ** 2))

    @property
    def perimeter(self):
        print(f'Длина окружности основания конуса равна - ', end='')
        return self.radius * 2 * pi

    @property
    def volume(self):
        print(f'Объем конуса равен - ', end='')
        h = sqrt(self.generatrix ** 2 - self.radius ** 2)
        return (pi * (self.radius ** 2) * h) / 3
























