'''На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).'''

n = int(input())
asd = [[*range(1, i+1)] for i in range(1, n+2)]

def pascal(n):
    for i in range(1, n+1):
        for j in range(1, i):
            asd[i][j] = asd[i-1][j] + asd[i-1][j-1]
        asd[i][i] = 1
    print(asd[n])
    
pascal(n)