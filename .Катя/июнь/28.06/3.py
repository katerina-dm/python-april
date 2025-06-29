dct = {
    "a": 1,
    "b": 2,
    "c": 3
}
dct["d"] = 4
keys = list(dct.keys())
values = list(dct.values())

print(f"Список ключей: {keys}")
print(f"Список значений: {values} ")

new_dct = {}

for k,v in dct.items():
    new_dct[v] = k

print(new_dct)