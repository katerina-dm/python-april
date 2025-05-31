x = (2, 4, 5) #кортеж
y = [4, 5, 2] #список

print(x)
print(y)
print(id(x))
print(id(y))

x = x + (1, )
y.append(1)

print(x)
print(y)
print(id(x))
print(id(y))