def fact(n):
    res = 1
    for i in range(n , 0, -1):
        res = res * i
    return res


def fact_list(n):
    fact_arr = []
    n_fact = fact(n)
    for i in range(n_fact, 0, -1):
       res = fact(i)
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

fact_list(n)
