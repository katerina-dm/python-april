#есть ли в числе повторяющие числа отдельно

number1 = 124110
number2 = 123456

ls1 = str(number1)
if len(ls1) ==len(set(ls1)):
    print("Повторов нет")
else:
    print("Повторы есть")

ls2 = str(number2)
if len(ls2) ==len(set(ls2)):
    print("Повторов нет")
else:
    print("Повторы есть")
