lst = [1, 2, 3, 4, 5] 

lst = list(map(lambda x: f"{int(x + 10)}", lst))
print(lst)