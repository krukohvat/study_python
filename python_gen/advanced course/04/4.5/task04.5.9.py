'''
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n^2 (то есть все числа разные) так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
'''
n = int(input())
mx = [[int(j) for j in input().split()] for i in range(n)]
sum_i = 0
sum_j = 0
sum_ii = 0
sum_not_ii = 0
flag = True
while flag:
    for i in range(n):
        for j in range(n):
            a = mx[i][j]
            for k in range(i, n):
                for l in range(j+1, n):
                    if (a == mx[k][l]) or (a not in range(1, 1+n**2)):
                        flag = False
                        break
    for i in range(1):
        for j in range(n):
            sum_not_ii += mx[n-j-1][j]
            sum_ii += mx[j][j]
    if sum_ii != sum_not_ii:
        flag = False
    else:
        for i in range(n):
            for j in range(n):
                sum_j += mx[j][i]
            sum_i = sum(mx[i])
            if sum_i != sum_j != sum_ii:
                flag = False
            sum_j = 0  
    break

if flag == True:
    print('YES')
else:
    print('NO')