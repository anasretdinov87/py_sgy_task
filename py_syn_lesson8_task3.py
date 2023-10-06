import math

weight_check = True
while weight_check:
    print("Введите максимальную массу груза лодки (1 <= m <= 10e6):")
    m = int(input())
    if m >= 1 and m <= 10e6:
        weight_check = False

count_check = True
while count_check:
    print("Введите количество рыбаков (1 <= n <= 100):")
    n = int(input())
    if n >= 1 and n <= 100:
        count_check = False

weight_arr = []
for i in range(n):
    num_check = True
    while num_check:
        print(f"Введите вес путешественника №{i + 1} (1<=Ai<={m})")
        num = int(input())
        if num <= m and num >= 1:
            num_check = False
            weight_arr.append(num)


is_sorted = True
counter = 1
iter = 0
for i in range(len(weight_arr)):
    for j in range(len(weight_arr) - 1):
        iter += 1
        if weight_arr[j] < weight_arr[j + 1]:
            is_sorted = False
            temp = weight_arr[j]
            weight_arr[j] = weight_arr[j + 1]
            weight_arr[j + 1] = temp
    counter += 1
    if is_sorted:
        break
    else:
        is_sorted = True

boats_free_weight_arr = [m] * n
boats_free_place = [2] * n

for i in range(len(weight_arr)):
    for j in range(len(boats_free_place)):
        if boats_free_place[j] > 0:
            if boats_free_weight_arr[j] >= weight_arr[i]:
                boats_free_weight_arr[j] = boats_free_weight_arr[j] - weight_arr[i]
                boats_free_place[j] -= 1
                break

boats_needed = 0
for i in range(len(boats_free_place)):
        if boats_free_place[i] != 2:
            boats_needed += 1

print(f"Необходимое минимальное число лодок: {boats_needed}")
