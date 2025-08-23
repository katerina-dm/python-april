# Persion
# 3 параметра -  name, surname, fullname (name,surname) - должны задать
# реализвать метод доступа к name surname fullname (get)
# реализвать метод изменения к name, surname 

class Persion:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__fullname = surname + " " + name

    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname
    
    def get_fullname(self):
        return self.__fullname

    def set_name(self,new_name):
        self.__name = new_name
        self.__fullname = self.__name + " " + self.__surname
    
    def set_surname(self,new_surname):
        self.__surname = new_surname
        self.__fullname = self.__name + " " + self.__surname


c1 = Persion( "Имя", "Фамилия")
print(c1.get_fullname())

c1.set_name("Вася")
print(c1.get_fullname())
