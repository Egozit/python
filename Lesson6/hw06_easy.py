import math, functools
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print('Задача №1')


class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[
            1]) ** 2)
        self.BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[
            1]) ** 2)
        self.CA = math.sqrt((self.A[0] - self.C[0]) ** 2 + (self.A[1] - self.C[
            1]) ** 2)

    @property
    def square(self):
        return 0.5 * math.fabs((self.C[0] - self.A[0]) * (self.B[1] - self.A[1]
                        ) - (self.C[1] - self.A[1]) * (self.B[0] - self.A[0]))

    def hight(self, side):
        p = (self.AB + self.BC + self.CA) / 2
        return 2 * math.sqrt(p * (p - self.AB) * (p - self.CA) * (p - self.BC)
                             ) / side

    @property
    def perimetr(self):
        return self.AB + self.BC + self.CA


triangle = Triangle((1, 0), (2, 4), (4, 5))
print('Square = ', triangle.square)
print("Высота к стороне АБ = ", triangle.hight(triangle.AB))
print('Perimetr = ', triangle.perimetr)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print()
print('Задача №2')


class Trapezium:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    @property
    def check_coord(self):
        if math.sqrt((self.C[0] - self.A[0]) ** 2 + (self.C[1] - self.A[
                1]) ** 2) == math.sqrt((self.D[0] - self.B[0]) ** 2 + (
                self.D[1] - self.B[1]) ** 2):
            return 'Трапеция равнобедренная'

    def length(self, side):
        do = {
            'AB': math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[
                1]) ** 2),
            'BC': math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[
                1]) ** 2),
            'CD': math.sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[
                1]) ** 2),
            'DA': math.sqrt((self.A[0] - self.D[0]) ** 2 + (self.A[1] - self.D[
                1]) ** 2)
        }
        return do.get(side)

    @property
    def perimetr(self):
        return functools.reduce(lambda itm, mem: mem + itm, [self.length('AB')
                + self.length('BC') + self.length('CD') + self.length('DA')])

    @property
    def hight(self):
        return math.sqrt(self.length('AB') ** 2 - (((self.length('DA') -
        self.length('BC')) ** 2 + self.length('AB') ** 2 - self.length('CD')
                ** 2) / (2 * (self.length('DA') - self.length('BC')))) ** 2)


trapezium = Trapezium((0, 0), (1, 3), (4, 3), (5, 0))
print(trapezium.check_coord)
print('Length of AB', trapezium.length('AB'))
print('Length of BC', trapezium.length('BC'))
print('Length of CD', trapezium.length('CD'))
print('Length of DA', trapezium.length('DA'))
print('Perimetr = ', trapezium.perimetr)
print('Hight = ', trapezium.hight)
