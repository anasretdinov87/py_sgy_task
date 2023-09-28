check_count = True
while check_count:
    print("Введите количество чисел (1 <= N <= 100000)")
    n = int(input())
    if n >= 1 and n <= 100000:
        check_count = False

check_nums = True
while check_nums:    
    nums_arr = []
    print(f"Введите через пробел числа, количество - {n} (Числа не должны превышать 2*10e9 по модулю):")
    nums_arr = input().split(' ')
    check_errors = True
    if len(nums_arr) < n:
        print("Ошибка. Недостаточно чисел. Повторите ввод.")
        check_errors = False
    else:
        for i in range(len(nums_arr)):
            if abs(int(nums_arr[i])) > 2*10e9:
                print(f"Ошибка. Число номер {i + 1} по модулю превышает 2*10е9. Повторите ввод")
                check_errors = False
                break
    if check_errors:
        check_nums = False
diff_nums = set(nums_arr)
print(f"Количество различных чисел - {len(diff_nums)}")
