'''Роскомнадзор запретил букву а 🌶️🌶️
Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".'''
restrictor = input() + ' запретил букву'
letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in letters:    
    if i in restrictor:
        print(restrictor, i)   
        restrictor = restrictor.replace(i, '').strip().replace('  ', ' ')