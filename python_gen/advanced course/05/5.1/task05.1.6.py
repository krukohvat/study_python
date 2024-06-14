'''Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.'''
n = int(input())
mx1 = [[int(j) for j in input().split()] for i in range(n)]
mx2 = [i[:] for i in mx1]
for i in range(n):
    for j in range(n):
        mx2[i][j] = mx1[j][i]
flag = True
for i in range(n):
    mx1[i].sort(reverse=True)
    mx2[i].sort(reverse=True)
for i in range(n):
    for j in range(n):
        if (mx1[i][j] not in range(1, n+1)) or (j+mx1[i][j] != n) or (j+mx2[i][j] != n):
            flag = False
            print("NO")
            break
    if flag == False:
        break
else:
    print("YES")