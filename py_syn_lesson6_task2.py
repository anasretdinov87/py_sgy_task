print("Введите натуральное число: ")

dividers_count = 0

x = int(input())
for i in range (1, x + 1):
    if x % i == 0:
        dividers_count += 1

print("Количество натуральных делителей числа равно: " + str(dividers_count))