# НАЙДИ ОШИБКУ
import math
class Shape:
	def __init__(self, Position = 0, Scale = 0, Color = ''):
		self._Position = Position
		self._Scale = Scale
		self._Color = Color
	# Все геттеры и сеттеры
	def set_Position(self, x):
		self._Position = x
	def get_Position(self):
		return self._Position
	def set_Scale(self, x):
		self._Scale = x
	def get_Scale(self):
		return self._Scale
	def set_Color(self, x):
		self._Color = x
	def get_Color(self):
		return self._Color
	
	def info(self):
		print(f'Координаты: {self._Position}\nРазмер: {self._Scale}\nЦвет: {self._Color}')

	def area(self):
		print(f'Площадь фигуры')
# Прямоугольник
class Rectangle(Shape):
	def __init__(self, Position = 0, Scale = 0, Color = '', side1 = 0, side2 = 0):
		super().__init__()
		self.__side1 = side1
		self.__side2 = side2
	# Все геттеры и сеттеры
	def set_Position(self, x):
		self._Position = x
	def get_Position(self):
		return self._Position
	def set_Scale(self, x):
		self._Scale = x
	def get_Scale(self):
		return self._Scale
	def set_Color(self, x):
		self._Color = x
	def get_Color(self):
		return self._Color
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
	def __init__(self, Position = 0, Scale = 0, Color = '', side1 = 0, side2 = 0, h = 0):
		super().__init__()
		self.__side1 = side1
		self.__side2 = side2	
		self.__h = h
	# Все геттеры и сеттеры
	def set_Position(self, x):
		self._Position = x
	def get_Position(self):
		return self._Position
	def set_Scale(self, x):
		self._Scale = x
	def get_Scale(self):
		return self._Scale
	def set_Color(self, x):
		self._Color = x
	def get_Color(self):
		return self._Color
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
	def __init__(self, Position = 0, Scale = 0, Color = '', radius = 0):
		super().__init__()
		self.__radius = radius
	# Все геттеры и сеттеры
	def set_Position(self, x):
		self._Position = x
	def get_Position(self):
		return self._Position
	def set_Scale(self, x):
		self._Scale = x
	def get_Scale(self):
		return self._Scale
	def set_Color(self, x):
		self._Color = x
	def get_Color(self):
		return self._Color
	def set_radius(self, x):
		self.__radius = x
	def get_radius(self):
		return self.__radius

	def info(self):
		super().info()
		print(f'Фигура: Круг\nРадиус окружности: {self.__radius}')
	def area(self):
		super().area()
		print(f'{math.pi * (self.__radius**2)}\n')

# Прямоугольник
Rectan = Rectangle()
Rectan.set_Position([200, 300])
Rectan.get_Position()
Rectan.set_Color('Красный')
Rectan.get_Color()
Rectan.set_Scale(3)
Rectan.get_Scale()
Rectan.set_side1(6)
Rectan.get_side1()
Rectan.set_side2(10)
Rectan.get_side2()
Rectan.info()
Rectan.area()
# Трапеция
Trapez = Trapezoid()
Trapez.set_Position([75, 100])
Trapez.get_Position()
Trapez.set_Color('Зеленый')
Trapez.get_Color()
Trapez.set_Scale(5)
Trapez.get_Scale()
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
Circ.set_Position([200, 300])
Circ.get_Position()
Circ.set_Color('Синий')
Circ.get_Color()
Circ.set_Scale(3)
Circ.get_Scale()
Circ.set_radius(6)
Circ.get_radius()
Circ.info()
Circ.area()