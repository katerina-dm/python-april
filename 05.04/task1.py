lst = [0.3, 0.76, 1.22, 0.05, 1.5] 
#lst = [30, 76, 122, 5, 15] 
#lst = [30%, 76%, 122%, 5%, 15%]
 
#lst = list(map(lambda x:str(int(x * 100)) +"%", lst))
lst = list(map(lambda x: f"{int(x * 100)}%", lst)) #f форматная строка
print(lst)

ls = ["30%", "76%", "122%", "5%", "15%"]
#ls = list(map(lambda x: int(x[: -1]) /100, lst))
ls = list(map(lambda x: int(x.rstrip("%")) /100, lst))
print(ls)