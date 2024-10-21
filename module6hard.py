import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, sides):
        self.__sides = sides
        self.__color = rgb
        self.filled = False


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return "Ошибка! Введены неверные значения!"

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return "Ошибка! Неверный диапазон значений!"

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        return all(isinstance(value, int) and value >= 0 for value in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, radius):
        super().__init__(rgb, radius)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, side1, side2, side3):
        super().__init__(rgb, side1, side2, side3)

    def get_square(self):
        sides = self.get_sides()
        P = sum(sides) / 2
        return math.sqrt(P * (P - sides[0]) * (P - sides[1]) * (P - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, side_length):
        super().__init__(rgb, [side_length] * self.sides_count)
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
