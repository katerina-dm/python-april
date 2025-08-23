
def draw_triangle(h, chr): # высота и символ
    for i in range(h//2): #h//2 совочисленное деление
        print(chr * (i+1))
    for i in range(h//2, -1, -1):#второй минус 1 это шаг на 1
        print(chr * (i+1))

height = int(input("введите высоту треугольника  "))
symbol = input("введите символ  ")
draw_triangle(height, symbol)
