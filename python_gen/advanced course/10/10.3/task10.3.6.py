'''
Самое редкое слово 
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.'''

stroka = [i.strip('.,!?:;-') for i in input().lower().split()]
result = {}
for i in stroka:
    result[i] = result.get(i, 0) + 1
min_list = []
for i in result.items():
    if min(result.values()) in i:
        min_list += [i[0]]
print(min(min_list))