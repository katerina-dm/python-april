def safe_dif(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
   

print(safe_dif(10,2))
print(safe_dif(10,0))