#примнение декараторов

from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diametr = 2 * radius
        self.__area = pi * radius **2

#декараторы мрименяются через @
#метод get  - @property
    @property
    def radius(self):
        return self.__radius
    
    # метод изменения радиуса
#   @radius.setter - вместо set
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius
        self.__diametr = 2 * new_radius
        self.__area = pi * new_radius **2

    @property
    def diametr(self):
        return self.__diametr
    
    @property
    def area(self):
        return self.__area
    
c1 = Circle(2)
print(f"Радиус круга равен {c1.radius}\nДиаметр равен {c1.diametr}\nПлощадь круга равна {c1.area}")

c1.radius = 5
print()
print(f"Радиус круга равен {c1.radius}\nДиаметр равен {c1.diametr}\nПлощадь круга равна {c1.area}")