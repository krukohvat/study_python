'''
В службе по дорожному движению решили оптимизировать процесс создания автомобильных номеров: вместо человека генерацию автомобильных номеров поручили некоторой GPT (модели машинного обучения). Как мы знаем, искусственный интеллект еще сыроват и делает много ошибок, поэтому его результаты следует тщательно проверять. Корректный автомобильный номер (в России) имеет следующий формат:

Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером. Программа должна вывести "YES" (без кавычек), если искусственный интеллект справился со своей задачей, или "NO" (без кавычек) в противном случае. В нашей задаче корректным автомобильным номером будем считать следующие форматы:

<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы "АВЕКМНОРСТУХ".
'''
nomer = input()
if (9<=len(nomer)<=10) and (nomer[0] in 'АВЕКМНОРСТУХ') and (nomer[4] in 'АВЕКМНОРСТУХ') and (nomer[5] in 'АВЕКМНОРСТУХ') and (nomer[6] == '_') and (nomer[1:4].isdigit()) and (nomer[7:].isdigit()):
    print("YES")
else:
    print("NO")