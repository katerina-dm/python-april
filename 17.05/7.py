s = open("1.txt","w", encoding="utf-8")

s.write("Добрый вечер дамы и господа")
try:
    print(s.read())
except Exception as e:
    print(e)
finally:  # служит для закрытия файла
    s.close()
    print("Файл закрыт")