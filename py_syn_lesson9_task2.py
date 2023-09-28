count_num1_check = True
while count_num1_check:
    print("Введите через пробел первый список чисел (До 100000 чисел):")
    nums1_arr = []
    nums1_arr = input().split(' ')
    if len(nums1_arr) > 100000:
        print("Ошибка. Превышен лимит количества чисел. Повторите ввод.")
    else:
        count_num1_check = False

nums1_set = set(nums1_arr)

count_num2_check = True
while count_num2_check:
    print("Введите через пробел второй список чисел (До 100000 чисел):")
    nums2_arr = []
    nums2_arr = input().split(' ')
    if len(nums2_arr) > 100000:
        print("Ошибка. Превышен лимит количества чисел. Повторите ввод.")
    else:
        count_num2_check = False

nums2_set = set(nums2_arr)

both  = len(nums1_set.intersection(nums2_arr))

print(f"Количество чисел содержащихся в обоих списках равно - {both}")
