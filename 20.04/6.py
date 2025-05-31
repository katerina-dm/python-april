num1 = 123456789
num2 = 4560

st1 = set(str(num1))
st2 = set(str(num2))

if st2.issubset(st1):
    print(f"{num2} является подмножеством {num1}")
else:
    print(f"{num2} не является подмножеством {num1}")
