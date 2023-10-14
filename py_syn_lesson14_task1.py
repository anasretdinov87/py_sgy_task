my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def ls_recur(n):
    if n == len(my_list):
        print('Конец списка')
        return
    print(str(my_list[n]) + ' ')
    ls_recur(n + 1)

ls_recur(0)


