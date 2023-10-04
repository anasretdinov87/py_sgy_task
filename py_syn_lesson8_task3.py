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



one_place_weight = m / 2
one_boat_needed = 0

for i in range(len(weight_arr)):
    if weight_arr[i] > one_place_weight:
        one_boat_needed += 1
boats_needed = math.ceil(((len(weight_arr)) - one_boat_needed) / 2)
boats_needed += one_boat_needed 
print(f"Необходимое минимальное число лодок: {boats_needed}")

