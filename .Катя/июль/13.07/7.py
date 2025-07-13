class Car:
    def __init__(self, mark, color,year):
        self.mark = mark
        self.color = color
        self.year = year
    

    #метод экземпляра класса
    def drive(self):
        print("Машина поехала")

    @classmethod
    def description(cls):
        print("Это класс для создания автомобиля")
        print(cls)
    
    #создали экземпляр класса с помощью другого контруктора 
    @classmethod
    def audi(cls, color, year):
        return cls("audi", color, year)

    @staticmethod
    def st():
        print("Привет это статический метод")


    def __str__(self):
        return f"Марка = {self.mark}\nЦвет - {self.color}\nГод выпуска - {self.year}"
    
car1 = Car("BMW", "Black", 1981)
car2 = Car("audi", "White", 1950)
print(car1)
print()
print(car2)
car1.drive()

Car.description()

Car.st()
car1.st()