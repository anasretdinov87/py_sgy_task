nums_check = True
while nums_check:
    print("Введите последовательность чисел через пробел:")
    nums_arr = []
    nums_arr = input().split(' ')
    for i in range(len(nums_arr)):
        nums_check = False
        if not nums_arr[i].replace('-','').replace('.','').isdigit():
            print("Ошибка. Введено не число. Повторите ввод.")
            nums_check = True
            break

result_arr = []
s = set()
for i in range(len(nums_arr)):
    if i == 0:
        result_arr.append("NO")
        s.add(nums_arr[i])
        continue
    if nums_arr[i] in s:
        result_arr.append("YES")
    else:
        result_arr.append("NO")
        s.add(nums_arr[i])
print(result_arr)


