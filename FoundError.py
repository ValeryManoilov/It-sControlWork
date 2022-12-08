# НАЙДИ ОШИБКУ
import math


class Shape:
    def __init__(self, position=0, scale=0, color=''):
        self._position = position
        self._scale = scale
        self._color = color
    # Все геттеры и сеттеры

    def set_position(self, x):
        self._position = x

    def get_position(self):
        return self._position

    def set_scale(self, x):
        self._scale = x

    def get_scale(self):
        return self._scale

    def set_color(self, x):
        self._color = x

    def get_color(self):
        return self._color

    def info(self):
        print(f'Координаты: {self._position}\nРазмер: {self._scale}\nЦвет: {self._color}')

    def area(self):
        print(f'Площадь фигуры: ', end='')
# Прямоугольник


class Rectangle(Shape):
    def __init__(self, position=0, scale=0, color='', side1=0, side2=0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
    # Все геттеры и сеттеры

    def set_position(self, x):
        self._position = x

    def get_position(self):
        return self._position

    def set_scale(self, x):
        self._scale = x

    def get_scale(self):
        return self._scale

    def set_color(self, x):
        self._color = x

    def get_color(self):
        return self._color

    def set_side1(self, x):
        self.__side1 = x

    def get_side1(self):
        return self.__side1

    def set_side2(self, x):
        self.__side2 = x

    def get_side2(self):
        return self.__side2

    def info(self):
        super().info()
        print(f'Фигура: Прямоугольник\nПервая сторона: {self.__side1}\nВторая сторона: {self.__side2}')

    def area(self):
        super().area()
        print(f'{self.__side1 * self.__side2}\n')
# Трапеция


class Trapezoid(Shape):
    def __init__(self, position=0, scale=0, color='', side1=0, side2=0, h=0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__h = h
    # Все геттеры и сеттеры

    def set_position(self, x):
        self._position = x

    def get_position(self):
        return self._position

    def set_scale(self, x):
        self._scale = x

    def get_scale(self):
        return self._scale

    def set_color(self, x):
        self._color = x

    def get_color(self):
        return self._color

    def set_side1(self, x):
        self.__side1 = x

    def get_side1(self):
        return self.__side1

    def set_side2(self, x):
        self.__side2 = x

    def get_side2(self):
        return self.__side2

    def set_h(self, x):
        self.__h = x

    def get_h(self):
        return self.__h

    def info(self):
        super().info()
        print(f'Фигура: Трапеция\nПервая сторона: {self.__side1}\nВторая сторона: {self.__side2}\nВысота: {self.__h}')

    def area(self):
        super().area()
        print(f'{((self.__side1 + self.__side2)/2)*self.__h}\n')
# Круг


class Circle(Shape):
    def __init__(self, position=0, scale=0, color='', radius=0):
        super().__init__()
        self.__radius = radius
    # Все геттеры и сеттеры

    def set_position(self, x):
        self._position = x

    def get_position(self):
        return self._position

    def set_scale(self, x):
        self._scale = x

    def get_scale(self):
        return self._scale

    def set_color(self, x):
        self._color = x

    def get_color(self):
        return self._color

    def set_radius(self, x):
        self.__radius = x

    def get_radius(self):
        return self.__radius

    def info(self):
        super().info()
        print(f'Фигура: Круг\nРадиус окружности: {self.__radius}')

    def area(self):
        super().area()
        print(f'{math.pi * (self.__radius**2)}')


# Прямоугольник
Rectan = Rectangle()
Rectan.set_position([200, 300])
Rectan.get_position()
Rectan.set_color('Красный')
Rectan.get_color()
Rectan.set_scale(3)
Rectan.get_scale()
Rectan.set_side1(6)
Rectan.get_side1()
Rectan.set_side2(10)
Rectan.get_side2()
Rectan.info()
Rectan.area()
# Трапеция
Trapez = Trapezoid()
Trapez.set_position([75, 100])
Trapez.get_position()
Trapez.set_color('Зеленый')
Trapez.get_color()
Trapez.set_scale(5)
Trapez.get_scale()
Trapez.set_side1(3)
Trapez.get_side1()
Trapez.set_side2(5)
Trapez.get_side2()
Trapez.set_h(2)
Trapez.get_h()
Trapez.info()
Trapez.area()
# Круг
Circ = Circle()
Circ.set_position([200, 300])
Circ.get_position()
Circ.set_color('Синий')
Circ.get_color()
Circ.set_scale(3)
Circ.get_scale()
Circ.set_radius(6)
Circ.get_radius()
Circ.info()
Circ.area()
