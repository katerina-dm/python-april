class Shape:
    pass

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass

class Cirele(Shape):
    pass

class Square(Rectangle):
    pass

class Iso_triangle(Triangle):
    pass

class Idu_triangle(Triangle):
    pass
#функция проверяет подкласс класса
print(issubclass(Square,Rectangle))