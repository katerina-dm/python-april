# класс Animal это родительский класс, на этом примере
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("Zzzz")

#Это класс наследуется от Animal
class Cat(Animal):
    def say(self):
        print("Мяу")

#создаем еще класс от Animal
class Dog(Animal):
    def say(self):
        print("Гав")


_animal = Animal("Животное", 10)
_cat = Cat("Леопольд", 45)
_dog = Dog("Шарик", 12)

print(_animal.name)
print(_cat.name)

_animal.sleep()
_cat.sleep()

_cat.say()
_dog.say()