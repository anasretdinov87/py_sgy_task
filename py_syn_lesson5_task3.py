print("Введите минимальную сумму инвестиции:")
x = int(input())
print("Введите сумму Майкла:")
a = int(input())
print("Введите сумму Ивана:")
b = int(input())

if (a >= x) and (b >= x):
    print(2)
elif (a >= x) and (b < x):
    print("Mike")
elif (a < x) and (b >= x):
    print("Ivan")
elif ((a+b) >= x):
    print(1)
else:
    print(0)