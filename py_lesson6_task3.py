print("Введите число A: ")
a = int(input())

b = 0
while b < a:
    print("Введите число B большое чем " + str(a))
    b = int(input())

print("Четные числа на заданном отрезке: ")
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end = ' ')
