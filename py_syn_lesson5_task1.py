print("Введите целое число")
num = int(input())

if num == 0:
    print("Нулевое число")
elif (num % 2 == 0) and (num > 0):
    print("Положительное четное число")
elif (num % 2 == 0) and (num < 0):
    print("Отрицательное четное число")
elif (num % 2 != 0) and (num > 0):
    print("Положительное нечетное число")
else:
    print("Отрицательное нечетное число")