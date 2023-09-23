print("Введите число N")
n = int(input())

zero_count = 0

for i in range(n):
    print("Введите число " + str(i + 1) + ":")
    num = int(input())
    if num == 0:
        zero_count += 1

print("Количество введеных нулей: " + str(zero_count))