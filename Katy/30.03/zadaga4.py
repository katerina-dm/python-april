def is_lucky_number(number):
    #123 456
    left = number // 1000
    right = number % 1000

    #123
    sum_left = (left // 100) + ((left // 10 ) % 10) + (left % 10)
    sum_right = (right // 100) + ((right // 10 ) % 10) + (right % 10)

    if sum_left == sum_right :
        return True
    else:
        return False

print(is_lucky_number(123456))
print(is_lucky_number(123420))



#Способ 2
def is_lucky_number(number):
    number = str(number) # переводим в строку
    ls = [int(i) for i in number] # переводим в целое число
    
    if sum(ls[: 3]) == sum(ls[3 : ]):
        return True
    else:
        return False

print(is_lucky_number(123456))
print(is_lucky_number(123420))
