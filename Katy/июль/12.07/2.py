import datetime

dt = datetime.date(2025, 7, 12)

#преобразуем в строчку двумя способами

s1 = str(dt)
s2 = repr(dt) # второй способ для машины, т.е.компа

print(s1)
print(s2)

a = datetime.date(2025, 7, 12)