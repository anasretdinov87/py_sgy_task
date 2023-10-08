def fact(n):
    fact_arr = []
    for i in range(n, 0, -1):
       res = i
       for j in range(i - 1, 0, -1):
            res = res * j
       fact_arr.append(res)  
    print(fact_arr)  

check_num = True
while check_num:
    print("Введите натуральное целое число")
    n = input()
    check_num = False
    if not n.isnumeric():
        check_num = True
        print("Ошибка. Введено не число. Повторите ввод")
        continue
    n = int(n)

fact(n)