#writelines - которая записывает последовательность строк в файл

fl = open("_writelines.txt", "w", encoding="utf-8")

lst = [f"{i}. ______\n" for i in range(1,11)]
fl.writelines(lst)
fl.close()