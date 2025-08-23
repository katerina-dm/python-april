def dref_line(len_line, direction, symbol):
    if direction == 'vertical' :
        print(f"{symbol}\n" * len_line) #\n - перенос строки
    elif  direction == 'horizontal':
        print(symbol * len_line)
    else:
        print("Wrong direction")
       
dref_line(10, 'vertical', " * ")    
dref_line(10, 'horizontal', " * ")    