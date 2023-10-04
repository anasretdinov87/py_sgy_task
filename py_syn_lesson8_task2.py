def shift(ls):    
    if len(ls) == 1:        
        return ls
    else:
        tmp = ls[-1]
        for i in range(int(len(ls))-1, 0, -1):            
           ls[i]=ls[i-1]
        ls[0] = tmp    
        return ls

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
        print(f"Введите элемент {i+1} (Число 1 <= Ai <= 10e9):")
        num = int(input())
        if num <= 10e9 and num >= 1:
            num_check = False
            arr.append(num)

print("N чисел: ")
print(arr) 
print("Измененный массив:")         
print(shift(arr))
