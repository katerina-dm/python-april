class Auto:
    def __init__(self, mark):
        self.mark = mark

#Создаем опиисние класса
    def __str__(self):
        return f"Автомобиль марки {self.mark}"

car = Auto("BMW")
print(car.mark)
print(car)