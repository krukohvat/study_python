'''
Напишите программу, которая транспонирует квадратную матрицу.
'''
n = int(input())
in_lst = [[j for j in input().split()] for k in range(n)]
for i in range(n):
	for j in range(n):
		print(in_lst[j][i], end=' ')
	print()