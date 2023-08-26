'''На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.'''
'''w w w o r l d g g g g r e a t t e c c h e m g g p w w'''
ls1 = input().split()
asd = []
qwe = []


for i in range(len(ls1)):
    if ls1[i] in asd:
        continue
    else:
        asd = []
        for j in range(i, len(ls1)):
            if ls1[i] == ls1[j]:
                asd += [ls1[j]]
            else:
                break
        qwe += [asd]

print(qwe)
