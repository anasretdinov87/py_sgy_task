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

matrix2 = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        matrix2[i][j] = random.randrange(-200, 201)

matrix_sum = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]

print('Матрица 1:')
pl(matrix1)
print()
print('Матрица 2:')
print()
pl(matrix2)
print()
print('Результат сложение:')
pl(matrix_sum)
