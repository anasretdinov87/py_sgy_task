count_check = True

while count_check:
    print("Введите количество элементов массива (1 <= n <= 10000):")
    n = int(input())
    if n >= 1 and n <= 10000:
        count_check = False
arr = []
for i in range(n):
    num_check = True
    while num_check:
        print(f"Введите элемент {i+1} (Число по модулю < 10e5):")
        num = int(input())
        if abs(num) < 10e5:
            num_check = False
            arr.append(num)
arr.reverse()
print("Перевернутый массив:")
print(arr)