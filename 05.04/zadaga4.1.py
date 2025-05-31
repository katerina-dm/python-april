def is_lucky_number(number):
    #123 456
    left = number // 1000
    right = number % 1000

    #123
    sum_left = (left // 100) + ((left // 10 ) % 10) + (left % 10)
    sum_right = (right // 100) + ((right // 10 ) % 10) + (right % 10)

#другая запись без else
    #if sum_left == sum_right :
        #return True
    #return False

#еще способ
    return sum_left == sum_right
        

print(is_lucky_number(123456))
print(is_lucky_number(123420))



#Способ 3
def is_lucky_number(number):
    ls = [int(i) for i in str(number)] 
    return sum(ls[: 3]) == sum(ls[3 : ])
        

print(is_lucky_number(123456))
print(is_lucky_number(123420))
