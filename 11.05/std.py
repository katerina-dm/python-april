import sys #это библиотека

sys.stdout.write("Hello world !")

fl = open("std.txt", "w", encoding="utf-8")

print("Hello from print!", file=fl)

fl.close()