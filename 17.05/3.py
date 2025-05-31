#try и except - блок выведения ошибок

print("Введите любое число: ")
count_mistakes = 0
try:
    number = int(input())
    print(number * 2)
except:
    count_mistakes +-1
    print("Введены некорректные данные")

