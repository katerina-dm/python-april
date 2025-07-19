class Car:
    count = 0
    def __init__(self, name, pover):
        Car.count += 1  #прибавляет одну машину
        self.name = name
        self.pover = pover
        self.serial_number = Car.count
        

    def __str__(self):
        return f"Имя - {self.name}\nМощность - {self.pover}\nКоличесво созданных машин - {self.count}\nСерийный номер - {self.serial_number}"

car1 = Car("Тесла", 500)
car2 = Car("Мерседес", 350)
print(car1)
print(car2)

