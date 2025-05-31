#Подстчет символов в строке

s = input("введите любой текст:  ")
dct = {}


# Hello
for ch in s.split("\n"):
    dct[ch] = dct.get(ch, 0) + 1

print(dct)
