""" Создайте класс "Круг", который имеет атрибуты радиус и цвет, и
методы вычисления площади и длины окружности. Создайте несколько
объектов этого класса и вызовите его методы для каждого объекта. """

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius
circle1 = Circle(1, 'red')
circle2 = Circle(2, 'blue')
circle3 = Circle(3, 'green')

print(f'Circle 1: Radius: {circle1.radius}, Color: {circle1.color}, Area: {circle1.area():.2f}, Circumference: {circle1.circumference():.2f}')
print(f'Circle 2: Radius: {circle2.radius}, Color: {circle2.color}, Area: {circle2.area():.2f}, Circumference: {circle2.circumference():.2f}')
print(f'Circle 3: Radius: {circle3.radius}, Color: {circle3.color}, Area: {circle3.area():.2f}, Circumference: {circle3.circumference():.2f}')