num1 = 123
num2 = 445

if set(str(num1)) & set(str(num2)):
    print("Пересечение есть")
else:
    print("Пересечения нет")