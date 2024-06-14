'''
Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

Формат входных данных
В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.

Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести «Не найдено» (без кавычек).

Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть по ссылке.

Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (':'), следом за которым идёт пробел.'''
coder_dict = [input().split(':') for i in range(int(input()))]
coder_dict = dict([(i[0].lower(), i[1]) for i in coder_dict])
words = [input().lower() for i in range(int(input()))]
for i in words:
    print(coder_dict.get(i, 'Не найдено').strip())