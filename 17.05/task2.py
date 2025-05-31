fale_name = input("введите название файла для чтения: ")

try:
    s = open(fale_name,"r", encoding="utf-8")
    print(s.read())
except:
    print("Файл не найден")