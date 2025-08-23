class Hero:
    def __init__(self,name, health):
        self.name = name
        self.health = health

#Создаем опиисние класса
    def __str__(self):
        return f"Герой {self.name}, Здоровье {self.health}"
#Добавить метод экземпляра
    def take_damage(self,damage):
        if damage > 0:
            print (f"{self.name} получил {damage} урона") 

        self.health -= damage
        if self.health <= 0:
            print (f"{self.name} ушел") 
        
hero1 = Hero("Арагорн", 100)
hero1.take_damage(25)
print(hero1)