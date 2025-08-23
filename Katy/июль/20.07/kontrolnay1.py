class Hero:
    def __init__(self,name, health):
        self.name = name
        self.health = health


#Создаем опиисние класса
    def __str__(self):
        return f"Герой {self.name}, Здоровье {self.health}"

hero1 = Hero("Арагорн", 100)
print(hero1)
