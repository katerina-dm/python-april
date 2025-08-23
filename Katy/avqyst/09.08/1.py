#патер слушатель

class Publisher:
    def __init__(self):
        self.subscribers = [] #подписчики
    
    def subscribe(self, odj): #подписаться
        self.subscribers.append(odj)
    
    def unsubscribe(self, odj): #отписаться
        self.subscribers.remove(odj)

    def notify(self, data: dict): #уведомление
        for sub in self.subscribers:
            sub.update(data)

#реализуем класс подписчика
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, data: dict):
        print(f"Подписчик {self.name} получил уведомление: {data["type"]} id {data["id"]}")

order = Publisher()

kitchen = Subscriber("Кухня")
count = Subscriber("Бухгалтерия")

order.subscribe(kitchen)
order.subscribe(count)

order.notify({"type": "заказ", "id": "001", "phone": "8-800-555-35-35"})