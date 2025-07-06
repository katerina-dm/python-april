# Persion
# 3 параметра -  name, surname, fullname (name,surname) - должны задать
# реализвать метод доступа к name surname fullname (get)
# реализвать метод изменения к name, surname 

class Persion:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__fullname = surname + " " + name
   
    @property
    def name(self):
        return self.__name
   
    @property
    def surname(self):
        return self.__surname
    @property
    def fullname(self):
        return self.__fullname

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        self.__fullname = self.__name + " " + self.__surname
    
    @surname.setter
    def surname(self,new_surname):
        self.__surname = new_surname
        self.__fullname = self.__name + " " + self.__surname


c1 = Persion( "Имя", "Фамилия")
print(c1.fullname)

c1.name = "Вася"
print(c1.fullname)
