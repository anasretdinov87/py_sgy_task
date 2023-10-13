import random

def pl(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

check_m = True
while check_m:
    print("Введите размерность m:")
    m = input()
    if not m.isnumeric():
        print("Ошибка. Необходимо ввести целое положительное число. Повторите ввод.")
        continue
    m = int(m)
    check_m = False
check_n = True  
while check_n:
    print("Введите размерность n:")
    n = input()
    if not n.isnumeric():
        print("Ошибка. Необходимо ввести целое положительное число. Повторите ввод.")
        continue
    n = int(n)
    check_n = False

matrix1 = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        matrix1[i][j] = random.randrange(-200, 201)
pl(matrix1)
