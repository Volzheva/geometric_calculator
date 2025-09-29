from geometric_calculator import *
from math import acos, degrees
import turtle as t
t.shape('classic')
t.speed(1)
t.pensize(5)
n = 20


class DrawerSquare(Square):

    @property
    def draw(self):
        for _ in range(2):
            t.forward(self.side * n)
            t.left(90)
            t.forward(self.side * n)
            t.left(90)
        return f'Фигура нарисована.'


class DrawerRectangle(Rectangle):

    @property
    def draw(self):
        for _ in range(2):
            t.forward(self.length * n)
            t.left(90)
            t.forward(self.width * n)
            t.left(90)
        return f'Фигура нарисована.'


class DrawerCircle(Circle):

    @property
    def draw(self):
        t.circle(self.radius * (n / 2))
        return f'Фигура нарисована.'


class DrawerTriangle(Triangle):

    @property
    def draw(self):
        cos_injection_3 = ((self.side_2 ** 2 + self.side_3 ** 2) - self.side_1 ** 2) / (2 * self.side_2 * self.side_3)
        injection_3 = degrees(acos(cos_injection_3))

        cos_injection_2 = ((self.side_1 ** 2 + self.side_3 ** 2) - self.side_2 ** 2) / (2 * self.side_1 * self.side_3)
        injection_2 = degrees(acos(cos_injection_2))

        cos_injection_1 = ((self.side_2 ** 2 + self.side_1 ** 2) - self.side_3 ** 2) / (2 * self.side_2 * self.side_1)
        injection_1 = degrees(acos(cos_injection_1))

        t.forward(self.side_2 * n)
        t.left(180 - injection_1)
        t.forward(self.side_1 * n)
        t.left(180 - injection_2)
        t.forward(self.side_3 * n)
        t.left(180 - injection_3 + 90)
        return f'Фигура нарисована.'


class DrawerTrapezoid(Trapezoid):

    @property
    def draw(self):
        sides = [self.side_1, self.side_2, self.side_3, self.side_4]
        sides.sort()
        b = sides[-1]
        a = sides[-2]
        c = sides[-3]
        t.forward(b * 20)
        t.left(105)
        t.forward(c * 20)
        t.left(75)
        t.forward(a * 20)
        t.home()
        return f'Фигура нарисована.'


class DrawerRhombus(Rhombus):

    @property
    def draw(self):
        t.left(180 - self.injection)
        t.forward(self.side * 20)
        t.left(180 - self.injection)
        t.forward(self.side * 20)
        t.left(self.injection)
        t.forward(self.side * 20)
        t.left(180 - self.injection)
        t.forward(self.side * 20)
        return f'Фигура нарисована.'


class DrawerCube(Cube):

    @property
    def draw(self):
        for _ in range(2):
            t.forward(self.side * 20)
            t.left(90)
            t.forward(self.side * 20)
            t.left(90)
        t.left(30)
        t.forward(self.side * 10)
        t.right(30)
        for _ in range(2):
            t.forward(self.side * 20)
            t.left(90)
            t.forward(self.side * 20)
            t.left(90)
        t.forward(self.side * 20)
        t.right(150)
        t.forward(self.side * 10)
        t.left(180)
        t.forward(self.side * 10)
        t.left(60)
        t.forward(self.side * 20)
        t.right(240)
        t.forward(self.side * 10)
        t.left(180)
        t.forward(self.side * 10)
        t.left(150)
        t.forward(self.side * 20)
        t.left(30)
        t.forward(self.side * 10)
        t.left(180)
        t.forward(self.side * 10)
        return f'Фигура нарисована.'


class DrawerParallelepiped(Parallelepiped):

    @property
    def draw(self):
        for _ in range(2):
            t.forward(self.length * 20)
            t.left(90)
            t.forward(self.width * 20)
            t.left(90)
        t.left(30)
        t.forward(self.length * 10)
        t.right(30)
        for _ in range(2):
            t.forward(self.length * 20)
            t.left(90)
            t.forward(self.width * 20)
            t.left(90)
        t.forward(self.length * 20)
        t.right(150)
        t.forward(self.length * 10)
        t.left(180)
        t.forward(self.length * 10)
        t.left(60)
        t.forward(self.width * 20)
        t.right(240)
        t.forward(self.length * 10)
        t.left(180)
        t.forward(self.length * 10)
        t.left(150)
        t.forward(self.length * 20)
        t.left(30)
        t.forward(self.length * 10)
        t.left(180)
        t.forward(self.length * 10)
        return f'Фигура нарисована.'


class DrawerSphere(Sphere):

    @property
    def draw(self):
        t.circle(self.radius * (n / 2))

        a = self.radius * (n / 4)
        b = self.radius * (n / 1.66)

        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 90)
        t.circle(b, 90)
        t.circle(a, 45)

        a = self.radius * (n / 8)
        b = self.radius * (n / 1.53)

        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 90)
        t.circle(b, 90)
        t.circle(a, 45)
        return f'Фигура нарисована.'


class DrawerPyramid(Pyramid):

    @property
    def draw(self):
        cos_injection_1 = ((self.width ** 2 + self.side ** 2) - self.width ** 2) / (2 * self.width * self.side)
        injection_1 = degrees(acos(cos_injection_1))

        t.forward(self.side * n)
        t.left(180 - injection_1)
        t.forward(self.width * n)
        x = t.pos()
        t.home()
        t.left(30)
        t.forward(self.side * n / 3)
        y = t.pos()
        t.right(30)
        t.forward(self.side * n)
        t.right(150)
        t.forward(self.side * n / 3)
        t.home()
        t.left(30)
        t.forward(self.side * n / 3)
        t.right(30)
        t.forward(self.side * n)
        t.goto(x)
        t.goto(y)
        t.home()
        return f'Фигура нарисована.'


class DrawerCylinder(Cylinder):

    @property
    def draw(self):
        a = self.radius * (n / 8)
        b = self.radius * (n / 1.66)

        t.right(90)
        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 45)
        x = t.pos()
        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 45)
        t.home()
        t.left(90)
        t.forward(self.height * n)
        t.circle(-a, 45)
        t.circle(-b, 90)
        t.circle(-a, 45)
        t.goto(x)
        t.back(self.height * n)
        t.circle(-a, 45)
        t.circle(-b, 90)
        t.circle(-a, 45)
        t.home()
        return f'Фигура нарисована.'


class DrawerCone(Cone):

    @property
    def draw(self):
        d = self.radius * 2
        cos_injection_3 = ((self.generatrix ** 2 + self.generatrix ** 2) - d ** 2) / (
                    2 * self.generatrix * self.generatrix)
        injection_3 = degrees(acos(cos_injection_3))

        cos_injection_2 = ((d ** 2 + self.generatrix ** 2) - self.generatrix ** 2) / (2 * d * self.generatrix)
        injection_2 = degrees(acos(cos_injection_2))

        cos_injection_1 = ((self.generatrix ** 2 + d ** 2) - self.generatrix ** 2) / (2 * self.generatrix * d)
        injection_1 = degrees(acos(cos_injection_1))

        t.left(180 - injection_1)
        t.forward(self.generatrix * n)
        t.left(180 - injection_3)
        t.forward(self.generatrix * n)
        t.left(90 - injection_2)
        a = self.radius * n / 8
        b = self.radius * (n / 0.738)

        t.circle(a, 45)
        t.circle(b, 90)
        t.circle(a, 90)
        t.circle(b, 90)
        t.circle(a, 45)
        return f'Фигура нарисована.'

'''
q = DrawerSquare(6.6)
print(q.title)
print(q.perimeter)
print(q.area)
print(q.draw)
'''
'''
w = DrawerRectangle(5, 8)
print(w.title)
print(w.perimeter)
print(w.area)
print(w.draw)
'''
'''
e = DrawerCircle(5)
print(e.title)
print(e.perimeter)
print(e.area)
print(e.draw)
'''
'''
r = DrawerTriangle(4, 7, 10)
print(r.title)
print(r.perimeter)
print(r.area)
print(r.draw)
'''
'''
y = DrawerTrapezoid(8, 12, 6.6, 5.5)
print(y.title)
print(y.perimeter)
print(y.area)
print(y.draw)
'''
'''
u = DrawerRhombus(8.3, 115.2)
print(u.title)
print(u.perimeter)
print(u.area)
print(u.draw)
'''
'''
o = DrawerCube(7.8)
print(o.title)
print(o.perimeter)
print(o.area)
print(o.volume)
print(o.draw)
'''
'''
f = DrawerParallelepiped(5, 8, 10)
print(f.title)
print(f.perimeter)
print(f.area)
print(f.volume)
print(f.draw)
'''
'''
g = DrawerSphere(5)
print(g.title)
print(g.perimeter)
print(g.area)
print(g.volume)
print(g.draw)
'''
'''
h = DrawerPyramid(8, 16)
print(h.title)
print(h.area)
print(h.perimeter)
print(h.volume)
print(h.draw)
'''
'''
j = DrawerCylinder(5.9, 10.8)
print(j.title)
print(j.area)
print(j.perimeter)
print(j.volume)
print(j.draw)
'''
'''
k = DrawerCone(3.9, 15.2)
print(k.title)
print(k.area)
print(k.perimeter)
print(k.volume)
print(k.draw)
'''