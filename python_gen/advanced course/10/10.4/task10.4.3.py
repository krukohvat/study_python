'''
Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.'''
print("YES" if sorted([i for i in input().lower().strip('.,!?:;-') if i.isalpha()]) == sorted([i for i in input().lower().strip('.,!?:;-') if i.isalpha()]) else "NO")