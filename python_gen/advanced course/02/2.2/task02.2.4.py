'''
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

Формат входных данных
На вход программе подается строка текста из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.
'''
spisok = [int(i) for i in input().split()]
sp1 = []
sp1.append(spisok[-1])
for i in range(len(spisok)-1):
    sp1.append(spisok[i])
print(*sp1)