'''На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.'''

ls1 = input().split()
n = int(input())

def chunked(ls1, n):
    asd = []
    qwe = []
    while True:
        if len(ls1) == 0:
            break
        elif len(ls1) < n:
            for i in range(len(ls1)):
                asd += [ls1[0]]
                del ls1[0]
            qwe += [asd]
            asd = []
        else:
            for i in range(n):
                asd += [ls1[0]]
                del ls1[0]
            qwe += [asd]
            asd = []
    print(qwe)

chunked(ls1, n)
