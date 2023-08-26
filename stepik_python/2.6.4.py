'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end".

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
spis = []
qwe = []
res = []
#create matrix
while True:
    stroka = input()
    if stroka == 'end':
        break
    else:
        spis += [[int(i) for i in stroka.split()]]

for i in range(len(spis)):
    for j in range(len(spis[i])):
        if (i+1 == len(spis)) and (j+1 == len(spis[i])):
            qwe += [spis[i-1][j] + spis[-(i+1)][j] + spis[i][j-1] + spis[i][-(j+1)]]
        elif i+1 == len(spis):
            qwe += [spis[i-1][j] + spis[-(i+1)][j] + spis[i][j-1] + spis[i][j+1]]
        elif j+1 == len(spis[i]):
            qwe += [spis[i-1][j] + spis[i+1][j] + spis[i][j-1] + spis[i][-(j+1)]]
        else:
            qwe += [spis[i-1][j] + spis[i+1][j] + spis[i][j-1] + spis[i][j+1]]
    res += [qwe]
    qwe = []

#print result
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print()
