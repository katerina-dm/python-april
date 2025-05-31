# "r" - для чтения
# encoding="utf-8" - кодировка
#read - считывает полностью все

fl = open("text.txt", "r", encoding="utf-8")
print(fl.read(5))
print(fl.read(5))
print(fl.read(10))
fl.close() #команда закрыть
  