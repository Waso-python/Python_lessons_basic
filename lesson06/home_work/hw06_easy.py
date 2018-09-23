import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class triangle:

    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3




# метод
    def trisquare(self): #Площадь треугольника
        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        s = ((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
        return s

    def triheight(self):
        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        d3 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

        h1 = 2 * self.trisquare() / d1
        h2 = 2 * self.trisquare() / d2
        h3 = 2 * self.trisquare() / d3
        return (h1,h2,h3)



    def triperimeter(self):
        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        d3 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

        return d1+d2+d3

tri = triangle((4,2),(2,4),(1,2))
print("Площадь треугольника",tri.trisquare())
print("Высоты треугольника",tri.triheight())
print("Периметр треугольника",tri.triperimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezoid:

    def __init__(self, point1, point2, point3, point4):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.p4 = point4

# метод
    def is_trapezoid(self):
        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        x4 = self.p4[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        y4 = self.p4[1]
        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        d3 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        return d1 == d3

    def trap_side(self):

        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        x4 = self.p4[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        y4 = self.p4[1]
        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        d3 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        return (d1,d2,d3,d4)

    def trap_perimeter(self):
        x1 = self.p1[0]
        x2 = self.p2[0]
        x3 = self.p3[0]
        x4 = self.p4[0]
        y1 = self.p1[1]
        y2 = self.p2[1]
        y3 = self.p3[1]
        y4 = self.p4[1]
        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        d3 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        return d1+d2+d3+d4

    def trap_squre(self):
        if self.is_trapezoid():
            x1 = self.p1[0]
            x2 = self.p2[0]
            x3 = self.p3[0]
            x4 = self.p4[0]
            y1 = self.p1[1]
            y2 = self.p2[1]
            y3 = self.p3[1]
            y4 = self.p4[1]
            d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            d3 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
            d4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
            s = ((d2+d4)/2)*math.sqrt(d1**2-(d4-d2)**2/4)
            return s






trap = trapezoid((2,3),(3,7),(8,7),(9,3))
if trap.is_trapezoid():
    print("Судя по координатам эта трапеция - равнобедренная")
else:  print("Судя по координатам это не равнобедренная трапеция")
print("Длина сторон трапеции - ", trap.trap_side())
print("Периметр трапеции - ", trap.trap_perimeter())
if trap.trap_squre():
    print ("Площадь равнобедренной трапеции - ", trap.trap_squre())
else:
    print("Не посчитали площадь, трапеция не равнобедренная")
