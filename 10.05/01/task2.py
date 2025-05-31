fl = open("task2.txt", "w", encoding="utf-8")
for p in range(1,10):
    for i in range(1,11):
        fl.write(f"{p} x {i} = {p*i}\n")
    fl.write("\n")
fl.close()